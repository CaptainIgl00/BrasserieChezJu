#!/usr/bin/env python3
import requests
import os
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
    
    try:
        print(f"Tentative de connexion à Directus ({DIRECTUS_URL})...")
        print(f"Email: {DIRECTUS_EMAIL}")
        print(f"Mot de passe: {'*' * len(DIRECTUS_PASSWORD)}")
        
        response = requests.post(login_url, json=login_data)
        
        if response.status_code == 200:
            data = response.json()
            access_token = data['data']['access_token']
            refresh_token = data['data']['refresh_token']
            
            print("\nConnexion réussie!")
            print(f"\nToken d'accès: {access_token}")
            print(f"\nToken de rafraîchissement: {refresh_token}")
            
            print("\nPour utiliser ce token, ajoutez-le à votre fichier .env.backend:")
            print(f"DIRECTUS_TOKEN={access_token}")
            
            return access_token
        else:
            print(f"\nErreur de connexion: {response.status_code}")
            print(f"Réponse: {response.text}")
            
            # Essayer avec l'URL interne de Directus
            print("\nEssai avec l'URL interne de Directus...")
            internal_url = os.getenv('DIRECTUS_URL', 'http://directus:8055')
            login_url_internal = f"{internal_url}/auth/login"
            
            try:
                # Cette requête ne fonctionnera pas depuis l'hôte, mais c'est juste pour montrer l'URL
                print(f"URL interne: {login_url_internal}")
                print("Cette URL ne fonctionne que depuis l'intérieur du réseau Docker.")
                print("\nPour obtenir un token, connectez-vous à l'interface d'administration de Directus:")
                print(f"URL: {DIRECTUS_URL}")
                print(f"Email: {DIRECTUS_EMAIL}")
                print(f"Mot de passe: {DIRECTUS_PASSWORD}")
            except:
                pass
            
            return None
    except requests.RequestException as e:
        print(f"\nErreur de connexion: {e}")
        return None

if __name__ == "__main__":
    login() 