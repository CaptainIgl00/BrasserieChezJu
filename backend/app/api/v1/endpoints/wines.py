from fastapi import APIRouter, HTTPException, Depends, status, Query
from typing import List, Optional
import httpx
from app.core.config import settings
from app.schemas.wine import WineResponse, WineCreate, WineUpdate

router = APIRouter()

# Client HTTP pour communiquer avec Directus
async def get_directus_client():
    async with httpx.AsyncClient(base_url=settings.DIRECTUS_URL, timeout=30.0) as client:
        client.headers.update({"Authorization": f"Bearer {settings.DIRECTUS_TOKEN}"})
        yield client

@router.get("/", response_model=List[WineResponse])
async def get_wines(
    client: httpx.AsyncClient = Depends(get_directus_client),
    category: Optional[str] = None,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Récupérer tous les vins, avec filtrage optionnel par catégorie et type
    """
    try:
        params = {
            "limit": limit,
            "offset": offset
        }
        
        filters = []
        if category:
            filters.append(f'"category": {{"_eq": "{category}"}}')
        if type:
            filters.append(f'"type": {{"_eq": "{type}"}}')
            
        if filters:
            params["filter"] = "{" + ",".join(filters) + "}"
        
        if sort:
            params["sort"] = sort
            
        response = await client.get("/items/wines", params=params)
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

@router.get("/{wine_id}", response_model=WineResponse)
async def get_wine(
    wine_id: str,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Récupérer un vin par son ID
    """
    try:
        response = await client.get(f"/items/wines/{wine_id}")
        response.raise_for_status()
        data = response.json()
        return data.get("data")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vin non trouvé"
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

@router.post("/", response_model=WineResponse, status_code=status.HTTP_201_CREATED)
async def create_wine(
    wine: WineCreate,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Créer un nouveau vin
    """
    try:
        response = await client.post("/items/wines", json=wine.model_dump())
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

@router.patch("/{wine_id}", response_model=WineResponse)
async def update_wine(
    wine_id: str,
    wine: WineUpdate,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Mettre à jour un vin
    """
    try:
        response = await client.patch(
            f"/items/wines/{wine_id}", 
            json=wine.model_dump(exclude_unset=True)
        )
        response.raise_for_status()
        data = response.json()
        return data.get("data")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vin non trouvé"
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

@router.delete("/{wine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_wine(
    wine_id: str,
    client: httpx.AsyncClient = Depends(get_directus_client)
):
    """
    Supprimer un vin
    """
    try:
        response = await client.delete(f"/items/wines/{wine_id}")
        response.raise_for_status()
        return None
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vin non trouvé"
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