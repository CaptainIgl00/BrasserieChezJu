#!/usr/bin/env python3
import requests
import os
import json
import time
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv('.env.backend')

# Configuration
DIRECTUS_URL = os.getenv('DIRECTUS_PUBLIC_URL', 'http://localhost:8055')
DIRECTUS_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@example.com')
DIRECTUS_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin_password_123')

# Collections à supprimer
COLLECTIONS_TO_DELETE = [
    "dishes",
    "menu_categories"
]

def login():
    """Se connecter à Directus et obtenir un token d'accès"""
    login_url = f"{DIRECTUS_URL}/auth/login"
    login_data = {
        "email": DIRECTUS_EMAIL,
        "password": DIRECTUS_PASSWORD
    }
    
    response = requests.post(login_url, json=login_data)
    
    if response.status_code == 200:
        access_token = response.json()['data']['access_token']
        print("Connexion à Directus réussie")
        return access_token
    else:
        print(f"Erreur de connexion: {response.status_code}")
        print(response.text)
        return None

def get_headers(access_token):
    """Préparer les en-têtes pour les requêtes API"""
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

def delete_all_items(headers, collection):
    """Supprimer tous les éléments d'une collection"""
    print(f"Suppression des éléments de la collection {collection}...")
    
    # Récupérer tous les éléments
    url = f"{DIRECTUS_URL}/items/{collection}"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Erreur lors de la récupération des éléments de {collection}: {response.status_code}")
        print(response.text)
        return False
    
    items = response.json()['data']
    
    if not items:
        print(f"Aucun élément à supprimer dans la collection {collection}")
        return True
    
    print(f"Suppression de {len(items)} éléments...")
    
    # Supprimer chaque élément
    for item in items:
        item_id = item['id']
        delete_url = f"{DIRECTUS_URL}/items/{collection}/{item_id}"
        delete_response = requests.delete(delete_url, headers=headers)
        
        if delete_response.status_code == 204:
            print(f"Élément {item_id} supprimé avec succès")
        else:
            print(f"Erreur lors de la suppression de l'élément {item_id}: {delete_response.status_code}")
            print(delete_response.text)
    
    return True

def delete_collection(headers, collection):
    """Supprimer une collection"""
    print(f"Suppression de la collection {collection}...")
    
    # Vérifier si la collection existe
    check_url = f"{DIRECTUS_URL}/collections/{collection}"
    check_response = requests.get(check_url, headers=headers)
    
    if check_response.status_code != 200:
        print(f"La collection {collection} n'existe pas ou erreur lors de la vérification")
        return True
    
    # Supprimer d'abord tous les éléments
    if not delete_all_items(headers, collection):
        return False
    
    # Supprimer la collection
    url = f"{DIRECTUS_URL}/collections/{collection}"
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print(f"Collection {collection} supprimée avec succès")
        return True
    else:
        print(f"Erreur lors de la suppression de la collection {collection}: {response.status_code}")
        print(response.text)
        return False

def delete_unused_files(headers):
    """Supprimer les fichiers non utilisés"""
    print("Suppression des fichiers non utilisés...")
    
    url = f"{DIRECTUS_URL}/files"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Erreur lors de la récupération des fichiers: {response.status_code}")
        print(response.text)
        return False
    
    files = response.json()['data']
    
    if not files:
        print("Aucun fichier à supprimer")
        return True
    
    print(f"Suppression de {len(files)} fichiers...")
    
    # Supprimer chaque fichier
    for file in files:
        file_id = file['id']
        delete_url = f"{DIRECTUS_URL}/files/{file_id}"
        delete_response = requests.delete(delete_url, headers=headers)
        
        if delete_response.status_code == 204:
            print(f"Fichier {file_id} supprimé avec succès")
        else:
            print(f"Erreur lors de la suppression du fichier {file_id}: {delete_response.status_code}")
            print(delete_response.text)
    
    return True

def main():
    """Fonction principale"""
    print("Suppression des données Directus pour Brasserie Chez Ju")
    print("====================================================")
    
    # Se connecter à Directus
    access_token = login()
    if not access_token:
        return
    
    headers = get_headers(access_token)
    
    # Supprimer les collections
    for collection in COLLECTIONS_TO_DELETE:
        delete_collection(headers, collection)
        time.sleep(1)  # Pause pour éviter de surcharger l'API
    
    # Supprimer les fichiers non utilisés
    delete_unused_files(headers)
    
    print("\nSuppression des données terminée!")

if __name__ == "__main__":
    main() 