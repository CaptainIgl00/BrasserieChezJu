from fastapi import APIRouter, HTTPException, Depends, status, Query
from typing import List, Optional
import httpx
from app.core.config import settings
from app.schemas.dish import DishResponse, DishCreate, DishUpdate

router = APIRouter()

# Client HTTP pour communiquer avec Directus
async def get_directus_client():
    async with httpx.AsyncClient(base_url=settings.DIRECTUS_URL, timeout=30.0) as client:
        client.headers.update({"Authorization": f"Bearer {settings.DIRECTUS_TOKEN}"})
        yield client

@router.get("/", response_model=List[DishResponse])
async def get_dishes(
    client: httpx.AsyncClient = Depends(get_directus_client),
    category_id: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Récupérer tous les plats, avec filtrage optionnel par catégorie
    """
    try:
        params = {
            "limit": limit,
            "offset": offset
        }
        
        if category_id:
            params["filter"] = f'{{"category": {{"_eq": "{category_id}"}}}}'
        
        if sort:
            params["sort"] = sort
            
        response = await client.get("/items/dishes", params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
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

@router.get("/{dish_id}", response_model=DishResponse)
async def get_dish(
    dish_id: str,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Récupérer un plat par son ID
    """
    try:
        response = await client.get(f"/items/dishes/{dish_id}")
        response.raise_for_status()
        data = response.json()
        return data.get("data")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plat non trouvé"
            )
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erreur Directus: {e.response.text}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur serveur: {str(e)}"
        )

@router.post("/", response_model=DishResponse, status_code=status.HTTP_201_CREATED)
async def create_dish(
    dish: DishCreate,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Créer un nouveau plat
    """
    try:
        response = await client.post("/items/dishes", json=dish.model_dump())
        response.raise_for_status()
        data = response.json()
        return data.get("data")
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

@router.patch("/{dish_id}", response_model=DishResponse)
async def update_dish(
    dish_id: str,
    dish: DishUpdate,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Mettre à jour un plat
    """
    try:
        response = await client.patch(
            f"/items/dishes/{dish_id}", 
            json=dish.model_dump(exclude_unset=True)
        )
        response.raise_for_status()
        data = response.json()
        return data.get("data")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plat non trouvé"
            )
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erreur Directus: {e.response.text}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur serveur: {str(e)}"
        )

@router.delete("/{dish_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dish(
    dish_id: str,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Supprimer un plat
    """
    try:
        response = await client.delete(f"/items/dishes/{dish_id}")
        response.raise_for_status()
        return None
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plat non trouvé"
            )
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erreur Directus: {e.response.text}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur serveur: {str(e)}"
        ) 