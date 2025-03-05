from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Dict, Any
import httpx
from app.core.config import settings

router = APIRouter()

# Client HTTP pour communiquer avec Directus
async def get_directus_client():
    async with httpx.AsyncClient(base_url=settings.DIRECTUS_URL, timeout=30.0) as client:
        client.headers.update({"Authorization": f"Bearer {settings.DIRECTUS_TOKEN}"})
        yield client

@router.get("/complete")
async def get_complete_menu(
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Récupérer le menu complet avec toutes les catégories et leurs plats
    """
    try:
        # Récupérer toutes les catégories
        categories_response = await client.get("/items/categories", params={
            "sort": "order",
            "fields": ["id", "name", "description", "order"]
        })
        categories_response.raise_for_status()
        categories_data = categories_response.json().get("data", [])
        
        # Pour chaque catégorie, récupérer les plats associés
        result = []
        for category in categories_data:
            dishes_response = await client.get("/items/dishes", params={
                "filter": f'{{"category": {{"_eq": "{category["id"]}"}}}}',
                "sort": "order",
                "fields": ["id", "name", "description", "price", "image", "portion", "order"]
            })
            dishes_response.raise_for_status()
            dishes_data = dishes_response.json().get("data", [])
            
            # Ajouter les plats à la catégorie
            category_with_dishes = {
                **category,
                "dishes": dishes_data
            }
            result.append(category_with_dishes)
        
        return result
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erreur Directus: {e.response.text}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur serveur: {str(e)}"
        )

@router.get("/wines")
async def get_wine_menu(
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Récupérer la carte des vins complète, organisée par catégorie et type
    """
    try:
        # Récupérer tous les vins
        wines_response = await client.get("/items/wines", params={
            "sort": ["category", "type", "price"],
            "fields": ["id", "name", "description", "price", "category", "type", "region", "year", "bottle_size"]
        })
        wines_response.raise_for_status()
        wines_data = wines_response.json().get("data", [])
        
        # Organiser les vins par catégorie et type
        wine_menu = {}
        for wine in wines_data:
            category = wine.get("category", "Autres")
            wine_type = wine.get("type", "Autres")
            
            if category not in wine_menu:
                wine_menu[category] = {}
            
            if wine_type not in wine_menu[category]:
                wine_menu[category][wine_type] = []
            
            wine_menu[category][wine_type].append(wine)
        
        # Convertir en liste pour la réponse API
        result = []
        for category, types in wine_menu.items():
            category_item = {
                "category": category,
                "types": []
            }
            
            for wine_type, wines in types.items():
                type_item = {
                    "type": wine_type,
                    "wines": wines
                }
                category_item["types"].append(type_item)
            
            result.append(category_item)
        
        return result
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erreur Directus: {e.response.text}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur serveur: {str(e)}"
        )

@router.get("/daily-specials")
async def get_daily_specials(
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Récupérer les suggestions du jour
    """
    try:
        response = await client.get("/items/daily_specials", params={
            "sort": "-date_created",
            "limit": 1,
            "fields": ["id", "date", "starters", "main_courses", "desserts", "formulas"]
        })
        response.raise_for_status()
        data = response.json().get("data", [])
        
        if not data:
            return {
                "date": None,
                "starters": [],
                "main_courses": [],
                "desserts": [],
                "formulas": []
            }
        
        return data[0]
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erreur Directus: {e.response.text}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur serveur: {str(e)}"
        ) 