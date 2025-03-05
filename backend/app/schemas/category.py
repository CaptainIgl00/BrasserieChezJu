from pydantic import BaseModel, Field
from typing import Optional, List

class CategoryBase(BaseModel):
    """Schéma de base pour les catégories"""
    name: str = Field(..., description="Nom de la catégorie")
    description: Optional[str] = Field(None, description="Description de la catégorie")
    order: Optional[int] = Field(None, description="Ordre d'affichage de la catégorie")

class CategoryCreate(CategoryBase):
    """Schéma pour la création d'une catégorie"""
    pass

class CategoryUpdate(BaseModel):
    """Schéma pour la mise à jour d'une catégorie"""
    name: Optional[str] = Field(None, description="Nom de la catégorie")
    description: Optional[str] = Field(None, description="Description de la catégorie")
    order: Optional[int] = Field(None, description="Ordre d'affichage de la catégorie")

class CategoryResponse(CategoryBase):
    """Schéma pour la réponse d'une catégorie"""
    id: str = Field(..., description="ID unique de la catégorie")

    class Config:
        from_attributes = True 