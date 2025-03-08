"""
Template d'endpoint API pour FastAPI.
Ce fichier peut être utilisé comme base pour créer de nouveaux endpoints API.

Utilisation:
1. Copiez ce fichier et renommez-le selon votre besoin (ex: events.py)
2. Modifiez les schémas, les routes et les fonctions selon vos besoins
3. Importez le router dans main.py et incluez-le dans l'application
"""

from fastapi import APIRouter, HTTPException, Depends, Query, Path
from typing import List, Optional
from ..schemas.template import TemplateItem, TemplateItemCreate, TemplateItemUpdate
from ..services.directus import DirectusService

# Créer un router pour ce module
router = APIRouter(
    prefix="/template-items",
    tags=["template-items"],
    responses={404: {"description": "Item not found"}}
)

# Initialiser le service Directus
directus_service = DirectusService()

# Collection Directus correspondante
COLLECTION_NAME = "template_items"

@router.get("/", response_model=List[TemplateItem])
async def get_template_items(
    skip: int = Query(0, description="Nombre d'items à sauter"),
    limit: int = Query(100, description="Nombre maximum d'items à retourner"),
    sort: Optional[str] = Query(None, description="Champ de tri (ex: name, -created_at)")
):
    """
    Récupère tous les items template avec pagination et tri.
    """
    try:
        items = await directus_service.get_items(
            collection=COLLECTION_NAME,
            skip=skip,
            limit=limit,
            sort=sort
        )
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{item_id}", response_model=TemplateItem)
async def get_template_item(
    item_id: str = Path(..., description="ID de l'item à récupérer")
):
    """
    Récupère un item template par son ID.
    """
    try:
        item = await directus_service.get_item(COLLECTION_NAME, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=TemplateItem, status_code=201)
async def create_template_item(
    item: TemplateItemCreate
):
    """
    Crée un nouvel item template.
    """
    try:
        created_item = await directus_service.create_item(COLLECTION_NAME, item.dict())
        return created_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{item_id}", response_model=TemplateItem)
async def update_template_item(
    item: TemplateItemUpdate,
    item_id: str = Path(..., description="ID de l'item à mettre à jour")
):
    """
    Met à jour un item template existant.
    """
    try:
        # Vérifier si l'item existe
        existing_item = await directus_service.get_item(COLLECTION_NAME, item_id)
        if not existing_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        # Mettre à jour l'item
        updated_item = await directus_service.update_item(
            COLLECTION_NAME, 
            item_id, 
            item.dict(exclude_unset=True)
        )
        return updated_item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{item_id}", status_code=204)
async def delete_template_item(
    item_id: str = Path(..., description="ID de l'item à supprimer")
):
    """
    Supprime un item template.
    """
    try:
        # Vérifier si l'item existe
        existing_item = await directus_service.get_item(COLLECTION_NAME, item_id)
        if not existing_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        # Supprimer l'item
        await directus_service.delete_item(COLLECTION_NAME, item_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 