#!/usr/bin/env python3
"""
Template de script pour l'initialisation des données dans Directus.
Ce script peut être utilisé comme base pour créer de nouveaux scripts d'initialisation.

Utilisation:
1. Copiez ce fichier et renommez-le selon votre besoin (ex: add_events_data.py)
2. Modifiez les variables COLLECTION_NAME et ITEMS selon vos besoins
3. Adaptez la fonction create_collection_fields() pour définir les champs de votre collection
4. Exécutez le script: python scripts/votre_script.py
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
COLLECTION_NAME = "your_collection_name"

# Données à initialiser
ITEMS = [
    {
        "name": "Item 1",
        "description": "Description de l'item 1"
    },
    {
        "name": "Item 2",
        "description": "Description de l'item 2"
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

def create_collection_fields():
    """Définition des champs de la collection"""
    return [
        {
            "field": "id",
            "type": "integer",
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
                "options": {
                    "placeholder": "Nom de l'item"
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
                    "placeholder": "Description de l'item"
                }
            },
            "schema": {
                "is_nullable": True
            }
        }
        # Ajoutez d'autres champs selon vos besoins
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
                    "icon": "list",
                    "note": f"Collection pour {collection_name}"
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

def add_item(headers, collection_name, item):
    """Ajout d'un item dans la collection"""
    try:
        response = requests.post(
            f"{DIRECTUS_URL}/items/{collection_name}",
            headers=headers,
            json=item
        )
        
        response.raise_for_status()
        logger.info(f"Item {item.get('name', 'sans nom')} ajouté avec succès.")
        return response.json()["data"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de l'ajout de l'item: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return None

def clean_collection(headers, collection_name):
    """Supprime tous les items d'une collection"""
    try:
        # Récupérer tous les items
        response = requests.get(
            f"{DIRECTUS_URL}/items/{collection_name}",
            headers=headers
        )
        
        response.raise_for_status()
        items = response.json()["data"]
        
        # Supprimer chaque item
        for item in items:
            item_id = item["id"]
            delete_response = requests.delete(
                f"{DIRECTUS_URL}/items/{collection_name}/{item_id}",
                headers=headers
            )
            delete_response.raise_for_status()
            logger.info(f"Item {item_id} supprimé.")
        
        logger.info(f"Collection {collection_name} nettoyée avec succès.")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors du nettoyage de la collection: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return False

def upload_image(headers, image_path):
    """Télécharge une image dans Directus et retourne son ID"""
    if not os.path.exists(image_path):
        logger.error(f"L'image {image_path} n'existe pas.")
        return None
    
    try:
        # Déterminer le type MIME de l'image
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            mime_type = 'application/octet-stream'
        
        # Créer un formulaire multipart
        with open(image_path, 'rb') as image_file:
            files = {
                'file': (os.path.basename(image_path), image_file, mime_type)
            }
            
            response = requests.post(
                f"{DIRECTUS_URL}/files",
                headers={"Authorization": headers["Authorization"]},
                files=files
            )
        
        response.raise_for_status()
        image_id = response.json()["data"]["id"]
        logger.info(f"Image {image_path} téléchargée avec succès (ID: {image_id}).")
        return image_id
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors du téléchargement de l'image: {str(e)}")
        if hasattr(e, 'response') and e.response:
            logger.error(f"Détails: {e.response.text}")
        return None

def main():
    """Point d'entrée principal du script"""
    # Authentification
    access_token = login()
    if not access_token:
        logger.error("Impossible de se connecter à Directus. Vérifiez vos identifiants.")
        return
    
    headers = get_headers(access_token)
    
    # Création de la collection
    fields = create_collection_fields()
    if not create_collection(headers, COLLECTION_NAME, fields):
        logger.error("Impossible de créer la collection. Arrêt du script.")
        return
    
    # Nettoyage de la collection (optionnel)
    # Décommentez la ligne suivante si vous souhaitez nettoyer la collection avant d'ajouter de nouveaux items
    # clean_collection(headers, COLLECTION_NAME)
    
    # Ajout des items
    for item in ITEMS:
        add_item(headers, COLLECTION_NAME, item)
    
    logger.info("Script exécuté avec succès!")

if __name__ == "__main__":
    main() 