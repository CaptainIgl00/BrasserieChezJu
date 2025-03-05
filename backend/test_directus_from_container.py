#!/usr/bin/env python3
import os
import httpx
import asyncio
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv('.env.backend')

# Configuration
DIRECTUS_URL = os.getenv('DIRECTUS_URL', 'http://directus:8055')
DIRECTUS_EMAIL = "admin@brasseriechezju.com"  # Email correct
DIRECTUS_PASSWORD = "changeme"  # Mot de passe correct
DIRECTUS_TOKEN = os.getenv('DIRECTUS_TOKEN', 'dev_token_1234567890')

async def test_login():
    """Tester la connexion à Directus avec les identifiants"""
    login_url = f"{DIRECTUS_URL}/auth/login"
    login_data = {
        "email": DIRECTUS_EMAIL,
        "password": DIRECTUS_PASSWORD
    }
    
    print(f"Tentative de connexion à Directus ({DIRECTUS_URL})...")
    print(f"Email: {DIRECTUS_EMAIL}")
    print(f"Mot de passe: {'*' * len(DIRECTUS_PASSWORD)}")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(login_url, json=login_data)
        
        if response.status_code == 200:
            data = response.json()
            access_token = data['data']['access_token']
            
            print("\nConnexion réussie!")
            print(f"\nToken d'accès: {access_token}")
            
            print("\nPour utiliser ce token, ajoutez-le à votre fichier .env.backend:")
            print(f"DIRECTUS_TOKEN={access_token}")
            
            return access_token
        else:
            print(f"\nErreur de connexion: {response.status_code}")
            print(f"Réponse: {response.text}")
            return None
    except httpx.RequestError as e:
        print(f"\nErreur de connexion: {e}")
        return None

async def test_token():
    """Tester la connexion à Directus avec le token"""
    server_info_url = f"{DIRECTUS_URL}/server/info"
    headers = {
        "Authorization": f"Bearer {DIRECTUS_TOKEN}"
    }
    
    print(f"Tentative de connexion à Directus avec le token...")
    print(f"URL: {server_info_url}")
    print(f"Token: {DIRECTUS_TOKEN}")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(server_info_url, headers=headers)
        
        if response.status_code == 200:
            print("\nConnexion avec token réussie!")
            print(f"Réponse: {response.json()}")
            return True
        else:
            print(f"\nErreur de connexion avec token: {response.status_code}")
            print(f"Réponse: {response.text}")
            return False
    except httpx.RequestError as e:
        print(f"\nErreur de connexion avec token: {e}")
        return False

async def main():
    print("=== Test de connexion à Directus ===")
    
    # Tester la connexion avec les identifiants
    token = await test_login()
    
    # Tester la connexion avec le token
    if not token:
        print("\n=== Test avec le token existant ===")
        await test_token()

if __name__ == "__main__":
    asyncio.run(main()) 