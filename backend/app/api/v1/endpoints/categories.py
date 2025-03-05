from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Optional
import httpx
from app.core.config import settings
from app.schemas.category import CategoryResponse, CategoryCreate, CategoryUpdate

router = APIRouter()

# Client HTTP pour communiquer avec Directus
async def get_directus_client():
    async with httpx.AsyncClient(base_url=settings.DIRECTUS_URL, timeout=30.0) as client:
        client.headers.update({"Authorization": f"Bearer {settings.DIRECTUS_TOKEN}"})
        yield client

@router.get("/", response_model=List[CategoryResponse])
async def get_categories(
    client: httpx.AsyncClient = Depends(get_directus_client),
    sort: Optional[str] = None,
    filter: Optional[str] = None
):
    """
    Récupérer toutes les catégories de menu
    """
    try:
        params = {}
        if sort:
            params["sort"] = sort
        if filter:
            params["filter"] = filter
            
        response = await client.get("/items/categories", params=params)
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

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(
    category_id: str,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Récupérer une catégorie par son ID
    """
    try:
        response = await client.get(f"/items/categories/{category_id}")
        response.raise_for_status()
        data = response.json()
        return data.get("data")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Catégorie non trouvée"
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

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category: CategoryCreate,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Créer une nouvelle catégorie
    """
    try:
        response = await client.post("/items/categories", json=category.model_dump())
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

@router.patch("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: str,
    category: CategoryUpdate,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Mettre à jour une catégorie
    """
    try:
        response = await client.patch(
            f"/items/categories/{category_id}", 
            json=category.model_dump(exclude_unset=True)
        )
        response.raise_for_status()
        data = response.json()
        return data.get("data")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Catégorie non trouvée"
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

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: str,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Supprimer une catégorie
    """
    try:
        response = await client.delete(f"/items/categories/{category_id}")
        response.raise_for_status()
        return None
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Catégorie non trouvée"
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