#!/usr/bin/env python3
"""
Script d'initialisation des données de vins dans Directus.
Ce script crée la collection 'wines' et y ajoute les vins de la carte.

Utilisation:
1. Assurez-vous que les variables d'environnement sont correctement configurées dans .env.backend
2. Exécutez le script: python scripts/add_wine_data.py
"""

import requests
import os
import json
import logging
from dotenv import load_dotenv

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Charger les variables d'environnement
load_dotenv('.env.backend')

# Configuration
DIRECTUS_URL = os.getenv('DIRECTUS_PUBLIC_URL', 'http://localhost:8055')
DIRECTUS_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@example.com')
DIRECTUS_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin_password_123')

# Nom de la collection à créer
COLLECTION_NAME = "wines"

# Données des vins à initialiser
WINE_ITEMS = [
    # Vins Rouges
    {
        "name": "Cuvée Archibald",
        "domain": "Domaine La Sapinière",
        "region": "AOP Malepère",
        "description": "Cabernet Franc et Merlot aux arômes de fruits mûrs, vanille et menthol. Bouche concentrée, tanins soyeux, finale cacao.",
        "bottle_price": 29,
        "category": "Rouge"
    },
    {
        "name": "Le rouge de L'Azérolle",
        "domain": "Raymond Julien - Domaine Mirausse",
        "region": "AOP Minervois",
        "description": "Cinsault, Grenache et Syrah aux notes de violette et cassis. Frais, fruité et souple en bouche.",
        "glass_price": 4,
        "bottle_price": 19,
        "category": "Rouge"
    },
    {
        "name": "Le Grand Penchant",
        "domain": "Raymond Julien - Domaine Mirausse",
        "region": "AOC Minervois",
        "description": "Syrah et Grenache aux arômes de fruits rouges et épices. Frais, long et tannins fins.",
        "bottle_price": 23,
        "category": "Rouge"
    },
    {
        "name": "Les Nourritures Terrestres",
        "domain": "Damien Baudouy - Domaine Pautard",
        "region": "Vin de France (VDF)",
        "description": "Assemblage typique du Minervois, ce vin dévoile des arômes de fruits rouges mûrs et d'épices. Sa bouche est souple et équilibrée, avec des tanins fins et une belle fraîcheur.",
        "glass_price": 3.5,
        "bottle_price": 17,
        "category": "Rouge"
    },
    {
        "name": "Cuvée Pinot noir",
        "domain": "Domaine Py",
        "region": "IGP Pays d'Oc",
        "description": "Pinot Noir bio aux arômes de cerise et framboise. Bouche lisse, tanins fins, finale persistante.",
        "bottle_price": 24,
        "category": "Rouge"
    },
    {
        "name": "La Pompadour",
        "domain": "Cave de Castelmaure",
        "region": "AOP Corbières",
        "description": "Carignan, Syrah et Grenache noir aux arômes de fruits mûrs et épices. Bouche soyeuse, notes de vanille, belle longueur.",
        "bottle_price": 24,
        "category": "Rouge"
    },
    {
        "name": "Clos des Natices",
        "domain": "Domaine Galy",
        "region": "AOP Cabardès",
        "description": "Syrah et Cabernet Franc aux arômes de fruits frais et vanille. Bouche volumineuse, tanins fins, finale réglisse.",
        "glass_price": 4,
        "bottle_price": 21,
        "category": "Rouge"
    },
    {
        "name": "Cuvée Joseph Mazard",
        "domain": "Domaine Serres-Mazard",
        "region": "AOC Corbières",
        "description": "Syrah, Carignan, Grenache et Mourvèdre aux arômes de fruits noirs, thym et café. Bouche riche et soyeuse, finale réglisse.",
        "bottle_price": 28,
        "category": "Rouge"
    },
    {
        "name": "Château de Villemajou",
        "domain": "Domaine Gérard Bertrand",
        "region": "AOP Corbières Boutenac",
        "description": "Robe grenat profond, arômes de fruits confits, épices et cuir. Bouche ronde, tanins fondus, finale longue.",
        "bottle_price": 39,
        "category": "Rouge"
    },
    
    # Vins Blancs
    {
        "name": "Uby n°4",
        "domain": "Domaine Uby",
        "region": "IGP Côtes de Gascogne",
        "description": "Blanc moelleux issu de Gros et Petit Manseng. Nez exotique, bouche veloutée et crémeuse, finale sur le coing et le citron confit.",
        "glass_price": 4,
        "bottle_price": 20,
        "category": "Blanc"
    },
    {
        "name": "Cuvée Antoine",
        "domain": "Domaine Py",
        "region": "AOC Corbières",
        "description": "Blanc bio alliant Vermentino et Grenache blanc. Nez d'agrumes, bouche vive et subtile, parfait avec poissons et crustacés.",
        "bottle_price": 24,
        "category": "Blanc"
    },
    {
        "name": "Chardonnay",
        "domain": "Domaine Antech",
        "region": "IGP Pays d'Oc",
        "description": "Chardonnay frais et croquant aux arômes floraux et exotiques. Équilibré et minéral, idéal avec poissons et fruits de mer.",
        "glass_price": 3.5,
        "bottle_price": 17,
        "category": "Blanc"
    },
    {
        "name": "Cuvée Marie-Pierre",
        "domain": "Domaine Serres-Mazard",
        "region": "AOC Corbières",
        "description": "Blanc demi-doux aux notes d'agrumes et de fleurs. Frais et léger, il accompagne parfaitement fruits de mer et poissons grillés.",
        "bottle_price": 21,
        "category": "Blanc"
    },
    
    # Vins Rosés
    {
        "name": "Tom et Lilly",
        "domain": "Raymond Julien – Domaine Mirausse",
        "region": "AOP Minervois",
        "description": "Rosé frais et fruité à base de Grenache et Cinsault. Léger, équilibré et rafraîchissant, parfait pour les journées ensoleillées.",
        "glass_price": 3.5,
        "bottle_price": 18,
        "category": "Rosé"
    },
    {
        "name": "Le Rosé",
        "domain": "Domaine La Sapinière",
        "region": "AOP Malepère",
        "description": "Assemblage de Merlot, Grenache et Cabernet Franc. Robe rose-pêche, bouche fruitée et structurée, idéale en apéritif ou avec un repas.",
        "bottle_price": 20,
        "category": "Rosé"
    },
    {
        "name": "Gris Blanc",
        "domain": "Domaine Gérard Bertrand",
        "region": "IGP Pays d'Oc",
        "description": "Rosé très pâle aux notes délicates de petits fruits rouges. Frais, léger et vif, avec une finale subtilement minérale.",
        "bottle_price": 24,
        "category": "Rosé"
    },
    
    # Champagnes
    {
        "name": "Première Bulles",
        "domain": "Sieur d'Arques",
        "region": "AOC Limoux",
        "description": "Élaboré selon la méthode traditionnelle, cet assemblage de Chardonnay, Chenin et Mauzac offre des bulles fines, une bouche onctueuse et une finale toastée.",
        "glass_price": 5,
        "bottle_price": 26,
        "category": "Champagne"
    },
    {
        "name": "Blanquette L'Ancestrale",
        "domain": "Domaine Antech",
        "region": "AOP Limoux",
        "description": "Blanquette douce et pétillante à base de Mauzac, aux arômes de miel, d'acacia et de poire mûre. Finale fruitée et vive sur la pomme et le raisin.",
        "glass_price": 4.5,
        "bottle_price": 22,
        "category": "Champagne"
    },
    {
        "name": "Blanquette Brut nature",
        "domain": "Domaine Antech",
        "region": "AOP Blanquette Limoux",
        "description": "Brut nature frais et léger, dominé par le Mauzac avec une touche de Chenin et Chardonnay. Notes de pomme verte, citron et camomille, avec une finale vive et minérale.",
        "glass_price": 4.5,
        "bottle_price": 23,
        "category": "Champagne"
    },
    {
        "name": "Champagne Taittinger",
        "domain": "",
        "region": "Champagne",
        "description": "Assemblage raffiné de Chardonnay, Pinot Noir et Pinot Meunier. Fines bulles, arômes de fruits frais et brioche, bouche vive et élégante avec une touche miellée.",
        "bottle_price": 70,
        "category": "Champagne"
    }
]

def login():
    """Authentification auprès de l'API Directus"""
    try:
        response = requests.post(
            f"{DIRECTUS_URL}/auth/login",
            json={
                "email": DIRECTUS_EMAIL,
                "password": DIRECTUS_PASSWORD
            }
        )
        
        response.raise_for_status()
        return response.json()["data"]["access_token"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur d'authentification: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return None

def get_headers(access_token):
    """Génération des en-têtes HTTP avec le token d'authentification"""
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

def create_wine_collection_fields():
    """Définition des champs de la collection des vins"""
    return [
        {
            "field": "id",
            "type": "uuid",
            "meta": {
                "hidden": True,
                "readonly": True,
                "interface": "input",
                "special": ["uuid"]
            },
            "schema": {
                "is_primary_key": True,
                "has_auto_increment": False
            }
        },
        {
            "field": "name",
            "type": "string",
            "meta": {
                "interface": "input",
                "display": "formatted-value",
                "display_options": {
                    "bold": True
                },
                "options": {
                    "placeholder": "Nom du vin"
                }
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "description",
            "type": "text",
            "meta": {
                "interface": "input-multiline",
                "options": {
                    "placeholder": "Description du vin"
                }
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "category",
            "type": "string",
            "meta": {
                "interface": "select-dropdown",
                "options": {
                    "choices": [
                        {"text": "Rouge", "value": "Rouge"},
                        {"text": "Blanc", "value": "Blanc"},
                        {"text": "Rosé", "value": "Rosé"},
                        {"text": "Champagne", "value": "Champagne"}
                    ]
                }
            },
            "schema": {
                "is_nullable": False,
                "default_value": "Rouge"
            }
        },
        {
            "field": "region",
            "type": "string",
            "meta": {
                "interface": "input",
                "options": {
                    "placeholder": "Région du vin"
                }
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "domain",
            "type": "string",
            "meta": {
                "interface": "input",
                "options": {
                    "placeholder": "Domaine viticole"
                }
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "year",
            "type": "integer",
            "meta": {
                "interface": "input",
                "options": {
                    "placeholder": "Année du vin"
                }
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "glass_price",
            "type": "float",
            "meta": {
                "interface": "input",
                "options": {
                    "placeholder": "Prix au verre"
                }
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "bottle_price",
            "type": "float",
            "meta": {
                "interface": "input",
                "options": {
                    "placeholder": "Prix de la bouteille"
                }
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "type",
            "type": "string",
            "meta": {
                "interface": "input",
                "options": {
                    "placeholder": "Type de vin (ex: Bordeaux, Bourgogne)"
                }
            },
            "schema": {
                "is_nullable": True
            }
        }
    ]

def collection_exists(headers, collection_name):
    """Vérifie si une collection existe déjà"""
    try:
        response = requests.get(
            f"{DIRECTUS_URL}/collections",
            headers=headers
        )
        
        response.raise_for_status()
        collections = response.json()["data"]
        return any(collection["collection"] == collection_name for collection in collections)
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la vérification des collections: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return False

def create_collection(headers, collection_name, fields):
    """Création d'une collection dans Directus"""
    # Vérifier si la collection existe déjà
    if collection_exists(headers, collection_name):
        logger.info(f"La collection {collection_name} existe déjà.")
        return True
    
    try:
        # Créer la collection
        response = requests.post(
            f"{DIRECTUS_URL}/collections",
            headers=headers,
            json={
                "collection": collection_name,
                "meta": {
                    "icon": "liquor",
                    "note": "Collection pour la carte des vins",
                    "display_template": "{{name}} - {{category}}"
                },
                "schema": {
                    "name": collection_name
                },
                "fields": fields
            }
        )
        
        response.raise_for_status()
        logger.info(f"Collection {collection_name} créée avec succès.")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la création de la collection: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return False

def add_wine(headers, wine):
    """Ajout d'un vin dans la collection"""
    try:
        response = requests.post(
            f"{DIRECTUS_URL}/items/{COLLECTION_NAME}",
            headers=headers,
            json=wine
        )
        
        response.raise_for_status()
        logger.info(f"Vin {wine.get('name', 'sans nom')} ajouté avec succès.")
        return response.json()["data"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de l'ajout du vin: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return None

def clean_collection(headers, collection_name):
    """Supprime tous les vins de la collection"""
    try:
        # Récupérer tous les vins
        response = requests.get(
            f"{DIRECTUS_URL}/items/{collection_name}",
            headers=headers
        )
        
        response.raise_for_status()
        wines = response.json()["data"]
        
        # Supprimer chaque vin
        for wine in wines:
            wine_id = wine["id"]
            delete_response = requests.delete(
                f"{DIRECTUS_URL}/items/{collection_name}/{wine_id}",
                headers=headers
            )
            delete_response.raise_for_status()
            logger.info(f"Vin {wine_id} supprimé.")
        
        logger.info(f"Collection {collection_name} nettoyée avec succès.")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors du nettoyage de la collection: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return False

def main():
    """Point d'entrée principal du script"""
    # Authentification
    access_token = login()
    if not access_token:
        logger.error("Impossible de se connecter à Directus. Vérifiez vos identifiants.")
        return
    
    headers = get_headers(access_token)
    
    # Création de la collection des vins
    fields = create_wine_collection_fields()
    if not create_collection(headers, COLLECTION_NAME, fields):
        logger.error("Impossible de créer la collection des vins. Arrêt du script.")
        return
    
    # Nettoyer la collection existante (optionnel)
    should_clean = input("Voulez-vous supprimer tous les vins existants ? (o/n): ").lower() == 'o'
    if should_clean:
        if not clean_collection(headers, COLLECTION_NAME):
            logger.error("Impossible de nettoyer la collection des vins. Arrêt du script.")
            return
    
    # Ajout des vins
    for wine in WINE_ITEMS:
        add_wine(headers, wine)
    
    logger.info(f"Script exécuté avec succès! {len(WINE_ITEMS)} vins ont été ajoutés.")

if __name__ == "__main__":
    main() 