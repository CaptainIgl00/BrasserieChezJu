import httpx
import asyncio
import os
import sys
import json
import time
from dotenv import load_dotenv

# Ajouter le répertoire app au chemin de recherche des modules
sys.path.append('/app')

# Importer la fonction get_valid_token de api.py
from app.api import get_valid_token

async def main():
    load_dotenv('.env.backend')
    
    # Utiliser la fonction get_valid_token pour obtenir un token valide
    token = await get_valid_token()
    print(f"Token: {token[:10]}...")
    
    headers = {'Authorization': f'Bearer {token}'}
    
    async with httpx.AsyncClient() as client:
        try:
            # Vérifier la structure complète d'un plat
            response = await client.get('http://directus:8055/items/dishes/038a2bcf-0d6c-4af1-9af0-b57fbb010805', headers=headers)
            print(f"Status: {response.status_code}")
            print(json.dumps(response.json(), indent=2))
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 