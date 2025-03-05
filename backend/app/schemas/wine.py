from pydantic import BaseModel, Field
from typing import Optional, List, Union, Dict, Any

class WineBase(BaseModel):
    """Schéma de base pour les vins"""
    name: str = Field(..., description="Nom du vin")
    description: Optional[str] = Field(None, description="Description du vin")
    price: float = Field(..., description="Prix du vin")
    category: str = Field(..., description="Catégorie du vin (ex: Rouge, Blanc, Rosé)")
    type: Optional[str] = Field(None, description="Type de vin (ex: Bordeaux, Bourgogne)")
    region: Optional[str] = Field(None, description="Région du vin")
    year: Optional[int] = Field(None, description="Année du vin")
    bottle_size: Optional[str] = Field(None, description="Taille de la bouteille")

class WineCreate(WineBase):
    """Schéma pour la création d'un vin"""
    pass

class WineUpdate(BaseModel):
    """Schéma pour la mise à jour d'un vin"""
    name: Optional[str] = Field(None, description="Nom du vin")
    description: Optional[str] = Field(None, description="Description du vin")
    price: Optional[float] = Field(None, description="Prix du vin")
    category: Optional[str] = Field(None, description="Catégorie du vin (ex: Rouge, Blanc, Rosé)")
    type: Optional[str] = Field(None, description="Type de vin (ex: Bordeaux, Bourgogne)")
    region: Optional[str] = Field(None, description="Région du vin")
    year: Optional[int] = Field(None, description="Année du vin")
    bottle_size: Optional[str] = Field(None, description="Taille de la bouteille")

class WineResponse(WineBase):
    """Schéma pour la réponse d'un vin"""
    id: str = Field(..., description="ID unique du vin")

    class Config:
        from_attributes = True 