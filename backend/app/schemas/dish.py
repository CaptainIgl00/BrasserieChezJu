from pydantic import BaseModel, Field
from typing import Optional, List, Union, Dict, Any

class DishBase(BaseModel):
    """Schéma de base pour les plats"""
    name: str = Field(..., description="Nom du plat")
    description: Optional[str] = Field(None, description="Description du plat")
    price: float = Field(..., description="Prix du plat")
    portion: Optional[str] = Field(None, description="Information sur la portion")
    category: str = Field(..., description="ID de la catégorie du plat")
    order: Optional[int] = Field(None, description="Ordre d'affichage du plat")

class DishCreate(DishBase):
    """Schéma pour la création d'un plat"""
    image: Optional[Union[str, Dict[str, Any]]] = Field(None, description="Image du plat (ID Directus ou objet)")

class DishUpdate(BaseModel):
    """Schéma pour la mise à jour d'un plat"""
    name: Optional[str] = Field(None, description="Nom du plat")
    description: Optional[str] = Field(None, description="Description du plat")
    price: Optional[float] = Field(None, description="Prix du plat")
    portion: Optional[str] = Field(None, description="Information sur la portion")
    category: Optional[str] = Field(None, description="ID de la catégorie du plat")
    image: Optional[Union[str, Dict[str, Any]]] = Field(None, description="Image du plat (ID Directus ou objet)")
    order: Optional[int] = Field(None, description="Ordre d'affichage du plat")

class DishResponse(DishBase):
    """Schéma pour la réponse d'un plat"""
    id: str = Field(..., description="ID unique du plat")
    image: Optional[Union[str, Dict[str, Any]]] = Field(None, description="Image du plat (ID Directus ou objet)")

    class Config:
        from_attributes = True 