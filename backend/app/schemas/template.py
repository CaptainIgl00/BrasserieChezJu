"""
Template de schémas Pydantic pour FastAPI.
Ce fichier peut être utilisé comme base pour créer de nouveaux schémas.

Utilisation:
1. Copiez ce fichier et renommez-le selon votre besoin (ex: events.py)
2. Modifiez les schémas selon vos besoins
3. Importez les schémas dans vos endpoints API
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class TemplateItemBase(BaseModel):
    """
    Schéma de base pour un item template.
    Contient les champs communs à tous les schémas d'item template.
    """
    name: str = Field(..., description="Nom de l'item", example="Item exemple")
    description: Optional[str] = Field(None, description="Description de l'item", example="Ceci est un exemple d'item")
    # Ajoutez d'autres champs selon vos besoins

class TemplateItemCreate(TemplateItemBase):
    """
    Schéma pour la création d'un item template.
    Hérite de TemplateItemBase et ajoute des champs spécifiques à la création.
    """
    # Vous pouvez ajouter des champs supplémentaires spécifiques à la création
    pass

class TemplateItemUpdate(BaseModel):
    """
    Schéma pour la mise à jour d'un item template.
    Tous les champs sont optionnels pour permettre des mises à jour partielles.
    """
    name: Optional[str] = Field(None, description="Nom de l'item", example="Item exemple mis à jour")
    description: Optional[str] = Field(None, description="Description de l'item", example="Ceci est un exemple d'item mis à jour")
    # Ajoutez d'autres champs selon vos besoins

class TemplateItem(TemplateItemBase):
    """
    Schéma complet d'un item template.
    Hérite de TemplateItemBase et ajoute des champs générés par le système.
    """
    id: UUID = Field(..., description="Identifiant unique de l'item")
    created_at: Optional[datetime] = Field(None, description="Date de création")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière mise à jour")
    
    class Config:
        """Configuration du schéma"""
        orm_mode = True  # Permet la conversion automatique des modèles ORM
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Item exemple",
                "description": "Ceci est un exemple d'item",
                "created_at": "2023-01-01T00:00:00",
                "updated_at": "2023-01-02T00:00:00"
            }
        }

class TemplateItemList(BaseModel):
    """
    Schéma pour une liste paginée d'items template.
    """
    items: List[TemplateItem]
    total: int = Field(..., description="Nombre total d'items")
    page: int = Field(..., description="Page actuelle")
    size: int = Field(..., description="Nombre d'items par page")
    pages: int = Field(..., description="Nombre total de pages")
    
    class Config:
        """Configuration du schéma"""
        schema_extra = {
            "example": {
                "items": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "name": "Item exemple 1",
                        "description": "Ceci est un exemple d'item 1",
                        "created_at": "2023-01-01T00:00:00",
                        "updated_at": "2023-01-02T00:00:00"
                    },
                    {
                        "id": "223e4567-e89b-12d3-a456-426614174000",
                        "name": "Item exemple 2",
                        "description": "Ceci est un exemple d'item 2",
                        "created_at": "2023-01-01T00:00:00",
                        "updated_at": "2023-01-02T00:00:00"
                    }
                ],
                "total": 2,
                "page": 1,
                "size": 10,
                "pages": 1
            }
        } 