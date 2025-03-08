# Scripts de gestion des données

Ce document décrit les scripts utilisés pour gérer les données de l'application Brasserie Chez Ju, notamment pour l'initialisation et la mise à jour des données dans le CMS Directus.

## Script `add_menu_data.py`

### Objectif
Ce script permet d'initialiser ou de mettre à jour les données du menu dans Directus. Il crée les collections nécessaires, télécharge les images et ajoute les catégories et plats du menu.

### Fonctionnalités
- Authentification auprès de l'API Directus
- Création des collections pour les catégories de menu et les plats
- Téléchargement et association des images aux plats
- Ajout des catégories de menu
- Ajout des plats avec leurs détails (nom, description, prix, etc.)

### Utilisation
```bash
python scripts/add_menu_data.py
```

### Structure du code
- **login()** : Authentification auprès de l'API Directus
- **get_headers()** : Génération des en-têtes HTTP avec le token d'authentification
- **create_collection()** : Création d'une collection dans Directus
- **upload_image()** : Téléchargement d'une image dans Directus
- **add_menu_category()** : Ajout d'une catégorie de menu
- **add_dish()** : Ajout d'un plat
- **create_menu_categories_collection()** : Création de la collection pour les catégories de menu
- **create_dishes_collection()** : Création de la collection pour les plats
- **clean_categories()** : Nettoyage des catégories existantes
- **main()** : Point d'entrée principal du script

## Bonnes pratiques pour les scripts de données

### 1. Idempotence
Les scripts doivent être idempotents, c'est-à-dire qu'ils peuvent être exécutés plusieurs fois sans créer de duplications ou d'erreurs. Cela implique de vérifier l'existence des données avant de les créer.

### 2. Gestion des erreurs
Les scripts doivent gérer correctement les erreurs et fournir des messages clairs pour faciliter le débogage.

### 3. Journalisation
Utiliser la journalisation pour suivre l'exécution du script et identifier les problèmes potentiels.

### 4. Configuration externalisée
Utiliser des variables d'environnement ou des fichiers de configuration pour les paramètres qui peuvent changer selon l'environnement.

### 5. Transactions
Utiliser des transactions lorsque cela est possible pour garantir l'intégrité des données.

## Création de nouveaux scripts

Pour créer un nouveau script de gestion de données, suivez ces étapes :

1. Créez un nouveau fichier Python dans le dossier `scripts/`
2. Importez les modules nécessaires (requests, os, json, etc.)
3. Chargez les variables d'environnement avec `load_dotenv('.env.backend')`
4. Définissez les fonctions nécessaires pour interagir avec l'API Directus
5. Créez une fonction `main()` comme point d'entrée
6. Testez le script dans un environnement de développement avant de l'utiliser en production

## Exemple de template pour un nouveau script

```python
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
    """Authentification auprès de l'API Directus"""
    response = requests.post(
        f"{DIRECTUS_URL}/auth/login",
        json={
            "email": DIRECTUS_EMAIL,
            "password": DIRECTUS_PASSWORD
        }
    )
    
    if response.status_code != 200:
        print(f"Erreur d'authentification: {response.text}")
        return None
    
    return response.json()["data"]["access_token"]

def get_headers(access_token):
    """Génération des en-têtes HTTP avec le token d'authentification"""
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

def main():
    """Point d'entrée principal du script"""
    # Authentification
    access_token = login()
    if not access_token:
        print("Impossible de se connecter à Directus. Vérifiez vos identifiants.")
        return
    
    headers = get_headers(access_token)
    
    # Logique principale du script
    print("Script exécuté avec succès!")

if __name__ == "__main__":
    main() 