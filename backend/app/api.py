from fastapi import APIRouter, HTTPException, status, Response
import httpx
from typing import List, Dict, Any, Optional
import os
import json
import time
from dotenv import load_dotenv
import logging

# Charger les variables d'environnement depuis le fichier .env.backend
load_dotenv("/app/.env.backend")

router = APIRouter()
logger = logging.getLogger(__name__)

# URL de Directus
DIRECTUS_URL = os.getenv("DIRECTUS_URL", "http://directus:8055")
DIRECTUS_PUBLIC_URL = os.getenv("DIRECTUS_PUBLIC_URL", "http://localhost:8055")
DIRECTUS_EMAIL = os.getenv("ADMIN_EMAIL", "admin@brasseriechezju.com")
DIRECTUS_PASSWORD = os.getenv("ADMIN_PASSWORD", "changeme")
API_HOST = os.getenv("API_HOST", "http://localhost:8000")

# Variables pour le token
directus_token = None
token_expiry = 0

# Fonction pour obtenir un token valide
async def get_valid_token():
    global directus_token, token_expiry
    
    # Si le token existe et est encore valide (avec une marge de 60 secondes)
    if directus_token and token_expiry > time.time() + 60:
        return directus_token
    
    # Sinon, obtenir un nouveau token
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{DIRECTUS_URL}/auth/login",
                json={
                    "email": DIRECTUS_EMAIL,
                    "password": DIRECTUS_PASSWORD
                }
            )
            
            if response.status_code != 200:
                print(f"Erreur lors de la connexion à Directus: {response.text}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Erreur lors de la connexion à Directus"
                )
            
            data = response.json()
            directus_token = data["data"]["access_token"]
            
            # Calculer l'expiration du token (par défaut 15 minutes)
            token_expiry = time.time() + 15 * 60
            
            print(f"Nouveau token obtenu, valide jusqu'à {time.strftime('%H:%M:%S', time.localtime(token_expiry))}")
            return directus_token
    except Exception as e:
        print(f"Erreur lors de l'obtention du token: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de l'obtention du token: {str(e)}"
        )

# Client HTTP pour communiquer avec Directus
async def get_directus_client():
    token = await get_valid_token()
    async with httpx.AsyncClient(base_url=DIRECTUS_URL, timeout=30.0) as client:
        client.headers.update({"Authorization": f"Bearer {token}"})
        yield client

@router.get("/menu/categories", response_model=List[Dict[str, Any]])
async def get_menu_categories():
    """
    Récupérer toutes les catégories de menu depuis Directus
    """
    token = await get_valid_token()
    async with httpx.AsyncClient(timeout=30.0) as client:
        client.headers.update({"Authorization": f"Bearer {token}"})
        
        try:
            response = await client.get(f"{DIRECTUS_URL}/items/menu_categories")
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Erreur lors de la récupération des catégories: {response.text}"
                )
            
            data = response.json()
            return data.get("data", [])
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Erreur de connexion à Directus: {str(exc)}"
            )

@router.get("/menu/dishes", response_model=List[Dict[str, Any]])
async def get_all_dishes():
    """
    Get all dishes from Directus
    """
    try:
        token = await get_valid_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        # Fetch all dishes
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DIRECTUS_URL}/items/dishes",
                headers=headers
            )
            
            if response.status_code != 200:
                logger.error(f"Failed to fetch dishes: {response.text}")
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
            dishes_data = response.json().get("data", [])
            
            # Transform the data
            dishes = []
            for dish in dishes_data:
                image_url = None
                if dish.get("image"):
                    # Utiliser notre propre endpoint pour les images avec URL absolue
                    image_url = f"{API_HOST}/api/v1/assets/{dish['image']}"
                
                dishes.append({
                    "id": dish.get("id", ""),
                    "name": dish.get("name", ""),
                    "description": dish.get("description", ""),
                    "price": str(dish.get("price", "")),
                    "portion": dish.get("portion"),
                    "category": dish.get("category", ""),
                    "image": image_url
                })
            
            return dishes
    except Exception as e:
        logger.error(f"Error fetching dishes: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching dishes: {str(e)}")

@router.get("/menu/dishes/category/{category_name}", response_model=List[Dict[str, Any]])
async def get_dishes_by_category(category_name: str):
    """
    Get dishes by category from Directus
    """
    try:
        token = await get_valid_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        # Fetch dishes by category
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DIRECTUS_URL}/items/dishes?filter[category][_eq]={category_name}",
                headers=headers
            )
            
            if response.status_code != 200:
                logger.error(f"Failed to fetch dishes by category: {response.text}")
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
            dishes_data = response.json().get("data", [])
            
            # Transform the data
            dishes = []
            for dish in dishes_data:
                image_url = None
                if dish.get("image"):
                    # Utiliser notre propre endpoint pour les images avec URL absolue
                    image_url = f"{API_HOST}/api/v1/assets/{dish['image']}"
                
                dishes.append({
                    "id": dish.get("id", ""),
                    "name": dish.get("name", ""),
                    "description": dish.get("description", ""),
                    "price": str(dish.get("price", "")),
                    "portion": dish.get("portion"),
                    "category": dish.get("category", ""),
                    "image": image_url
                })
            
            return dishes
    except Exception as e:
        logger.error(f"Error fetching dishes by category: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching dishes by category: {str(e)}")

@router.get("/menu/complete")
async def get_complete_menu():
    """
    Get the complete menu with all categories and their dishes
    """
    try:
        token = await get_valid_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        # Fetch all categories
        async with httpx.AsyncClient() as client:
            categories_response = await client.get(
                f"{DIRECTUS_URL}/items/menu_categories",
                headers=headers
            )
            
            if categories_response.status_code != 200:
                logger.error(f"Failed to fetch categories: {categories_response.text}")
                raise HTTPException(status_code=categories_response.status_code, detail=categories_response.text)
            
            categories_data = categories_response.json().get("data", [])
            
            # Fetch all dishes
            dishes_response = await client.get(
                f"{DIRECTUS_URL}/items/dishes",
                headers=headers
            )
            
            if dishes_response.status_code != 200:
                logger.error(f"Failed to fetch dishes: {dishes_response.text}")
                raise HTTPException(status_code=dishes_response.status_code, detail=dishes_response.text)
            
            dishes_data = dishes_response.json().get("data", [])
            
            # Transform the data
            menu = []
            for category in categories_data:
                category_dishes = []
                for dish in dishes_data:
                    if dish.get("category") == category.get("name"):
                        image_url = None
                        if dish.get("image"):
                            # Utiliser notre propre endpoint pour les images avec URL absolue
                            image_url = f"{API_HOST}/api/v1/assets/{dish['image']}"
                        
                        category_dishes.append({
                            "id": dish.get("id", ""),
                            "name": dish.get("name", ""),
                            "description": dish.get("description", ""),
                            "price": str(dish.get("price", "")),
                            "portion": dish.get("portion"),
                            "image": image_url
                        })
                
                menu.append({
                    "id": category.get("id", ""),
                    "name": category.get("name", ""),
                    "description": category.get("description", ""),
                    "dishes": category_dishes
                })
            
            return menu
    except Exception as e:
        logger.error(f"Error fetching complete menu: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching complete menu: {str(e)}")

@router.get("/menu/wines")
async def get_wine_menu():
    """
    Get the wine menu with all categories
    """
    try:
        token = await get_valid_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        # Fetch all wines
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DIRECTUS_URL}/items/wines",
                headers=headers
            )
            
            if response.status_code != 200:
                logger.error(f"Failed to fetch wines: {response.text}")
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
            wines_data = response.json().get("data", [])
            
            # Group wines by category
            wine_categories = {}
            for wine in wines_data:
                category = wine.get("category", "Autres")
                if category not in wine_categories:
                    wine_categories[category] = []
                
                image_url = None
                if wine.get("image"):
                    # Utiliser notre propre endpoint pour les images avec URL absolue
                    image_url = f"{API_HOST}/api/v1/assets/{wine['image']}"
                
                wine_categories[category].append({
                    "id": wine.get("id", ""),
                    "name": wine.get("name", ""),
                    "description": wine.get("description", ""),
                    "price": str(wine.get("price", "")),
                    "type": wine.get("type", ""),
                    "region": wine.get("region", ""),
                    "year": wine.get("year", ""),
                    "bottle_size": wine.get("bottle_size", ""),
                    "image": image_url
                })
            
            # Transform to list of categories with wines
            menu = []
            for category, wines in wine_categories.items():
                menu.append({
                    "name": category,
                    "wines": wines
                })
            
            return menu
    except Exception as e:
        logger.error(f"Error fetching wine menu: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching wine menu: {str(e)}")

@router.get("/menu/daily-specials")
async def get_daily_specials():
    """
    Get the daily specials
    """
    try:
        token = await get_valid_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        # Fetch daily specials
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DIRECTUS_URL}/items/daily_specials",
                headers=headers
            )
            
            if response.status_code != 200:
                logger.error(f"Failed to fetch daily specials: {response.text}")
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
            specials_data = response.json().get("data", [])
            
            # Transform the data
            specials = []
            for special in specials_data:
                image_url = None
                if special.get("image"):
                    # Utiliser notre propre endpoint pour les images avec URL absolue
                    image_url = f"{API_HOST}/api/v1/assets/{special['image']}"
                
                specials.append({
                    "id": special.get("id", ""),
                    "name": special.get("name", ""),
                    "description": special.get("description", ""),
                    "price": str(special.get("price", "")),
                    "date": special.get("date", ""),
                    "image": image_url
                })
            
            return specials
    except Exception as e:
        logger.error(f"Error fetching daily specials: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching daily specials: {str(e)}")

@router.get("/assets/{asset_id}")
async def get_asset(asset_id: str):
    """
    Proxy pour récupérer les assets de Directus
    """
    try:
        token = await get_valid_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        # Récupérer l'asset depuis Directus
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DIRECTUS_URL}/assets/{asset_id}",
                headers=headers
            )
            
            if response.status_code != 200:
                logger.error(f"Failed to fetch asset: {response.text}")
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
            # Retourner l'image avec le bon Content-Type
            content_type = response.headers.get("Content-Type", "application/octet-stream")
            return Response(content=response.content, media_type=content_type)
    except Exception as e:
        logger.error(f"Error fetching asset: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching asset: {str(e)}") 