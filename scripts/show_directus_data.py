#!/usr/bin/env python3
import requests
import os
import json
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv('.env.backend')

# Configuration
DIRECTUS_URL = os.getenv('DIRECTUS_PUBLIC_URL', 'http://localhost:8055')
DIRECTUS_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@example.com')
DIRECTUS_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin_password_123')

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

def get_collections(headers):
    """Récupérer la liste des collections"""
    url = f"{DIRECTUS_URL}/collections"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        collections = response.json()['data']
        return collections
    else:
        print(f"Erreur lors de la récupération des collections: {response.status_code}")
        print(response.text)
        return []

def get_items(headers, collection):
    """Récupérer les éléments d'une collection"""
    url = f"{DIRECTUS_URL}/items/{collection}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        items = response.json()['data']
        return items
    else:
        print(f"Erreur lors de la récupération des éléments de {collection}: {response.status_code}")
        print(response.text)
        return []

def show_collection_data(headers, collection_name):
    """Afficher les données d'une collection"""
    print(f"\n=== Collection: {collection_name} ===")
    items = get_items(headers, collection_name)
    
    if not items:
        print("Aucun élément trouvé ou erreur lors de la récupération")
        return
    
    print(f"Nombre d'éléments: {len(items)}")
    
    # Afficher les 5 premiers éléments (ou tous s'il y en a moins de 5)
    for i, item in enumerate(items[:5]):
        print(f"\nÉlément {i+1}:")
        print(json.dumps(item, indent=2, ensure_ascii=False))
    
    if len(items) > 5:
        print(f"\n... et {len(items) - 5} autres éléments")

def main():
    """Fonction principale"""
    print("Affichage des données Directus pour Brasserie Chez Ju")
    print("===================================================")
    
    # Se connecter à Directus
    access_token = login()
    if not access_token:
        return
    
    headers = get_headers(access_token)
    
    # Récupérer la liste des collections
    collections = get_collections(headers)
    
    if not collections:
        print("Aucune collection trouvée ou erreur lors de la récupération")
        return
    
    print("\nCollections disponibles:")
    for collection in collections:
        print(f"- {collection['collection']}")
    
    # Collections à afficher (exclure les collections système de Directus)
    user_collections = [c['collection'] for c in collections if not c['collection'].startswith('directus_')]
    
    # Afficher les données de chaque collection
    for collection in user_collections:
        show_collection_data(headers, collection)

if __name__ == "__main__":
    main() 