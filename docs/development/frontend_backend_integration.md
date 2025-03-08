# Intégration Frontend-Backend

Ce document décrit comment intégrer le frontend Nuxt avec le backend FastAPI et Directus pour créer une application complète et cohérente.

## Architecture d'intégration

L'intégration entre le frontend et le backend suit le modèle suivant :

```
Frontend (Nuxt)                 Backend (FastAPI)                 CMS (Directus)
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│               │  HTTP/JSON    │               │  HTTP/JSON    │               │
│  Composables  │◄─────────────►│  API Routes   │◄─────────────►│  Collections  │
│               │               │               │               │               │
└───────┬───────┘               └───────┬───────┘               └───────┬───────┘
        │                               │                               │
┌───────▼───────┐               ┌───────▼───────┐               ┌───────▼───────┐
│               │               │               │               │               │
│  Composants   │               │  Services     │               │  Assets       │
│               │               │               │               │               │
└───────────────┘               └───────────────┘               └───────────────┘
```

## Étapes pour généraliser l'intégration

### 1. Créer des composables pour chaque domaine fonctionnel

Pour chaque domaine fonctionnel de l'application (menu, réservations, événements, etc.), créez un composable Vue dédié dans le dossier `composables/`.

Exemple de structure :
- `useMenu.ts` : Gestion du menu
- `useReservation.ts` : Gestion des réservations
- `useEvents.ts` : Gestion des événements
- `useWines.ts` : Gestion de la carte des vins
- `useGallery.ts` : Gestion de la galerie d'images

Modèle de composable :

```typescript
// composables/useFeature.ts
import { ref, computed } from 'vue'

// Types pour les données
interface FeatureItem {
  id: string
  name: string
  // Autres propriétés...
}

// État réactif
const items = ref<FeatureItem[]>([])
const isLoading = ref(false)
const error = ref<string | null>(null)

// URL de l'API backend
const apiBaseUrl = process.env.NODE_ENV === 'production' 
  ? '/api/v1' 
  : 'http://localhost:8000/api/v1'

export function useFeature() {
  // Fonction pour récupérer les données
  const fetchItems = async () => {
    if (items.value.length > 0) return // Éviter de recharger si déjà chargé
    
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${apiBaseUrl}/feature-items`)
      if (!response.ok) throw new Error(`Erreur HTTP: ${response.status}`)
      
      const data = await response.json()
      items.value = data.items
    } catch (err) {
      console.error('Erreur lors de la récupération des données:', err)
      error.value = err instanceof Error ? err.message : 'Erreur inconnue'
    } finally {
      isLoading.value = false
    }
  }
  
  // Autres fonctions spécifiques à cette fonctionnalité...
  
  return {
    items,
    isLoading,
    error,
    fetchItems,
    // Autres fonctions exposées...
  }
}
```

### 2. Créer des endpoints API dans le backend

Pour chaque domaine fonctionnel, créez des endpoints API dans le backend FastAPI.

Exemple de structure :
- `/api/v1/menu` : Endpoints pour le menu
- `/api/v1/reservations` : Endpoints pour les réservations
- `/api/v1/events` : Endpoints pour les événements
- `/api/v1/wines` : Endpoints pour la carte des vins
- `/api/v1/gallery` : Endpoints pour la galerie d'images

Modèle d'endpoint API :

```python
# backend/app/api/feature.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..schemas.feature import FeatureItem, FeatureItemCreate
from ..services.directus import DirectusService

router = APIRouter()
directus_service = DirectusService()

@router.get("/feature-items", response_model=List[FeatureItem])
async def get_feature_items():
    try:
        items = await directus_service.get_items("feature_items")
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/feature-items/{item_id}", response_model=FeatureItem)
async def get_feature_item(item_id: str):
    try:
        item = await directus_service.get_item("feature_items", item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Autres endpoints...
```

### 3. Créer des collections dans Directus

Pour chaque domaine fonctionnel, créez des collections dans Directus pour stocker les données.

Exemple de collections :
- `menu_categories` : Catégories de menu
- `dishes` : Plats
- `reservations` : Réservations
- `events` : Événements
- `wines` : Vins
- `gallery_images` : Images de la galerie

### 4. Créer des scripts d'initialisation des données

Pour chaque domaine fonctionnel, créez des scripts Python pour initialiser les données dans Directus.

Exemple de scripts :
- `add_menu_data.py` : Initialisation des données du menu
- `add_reservation_data.py` : Initialisation des données de réservation
- `add_event_data.py` : Initialisation des données d'événements
- `add_wine_data.py` : Initialisation des données de la carte des vins
- `add_gallery_data.py` : Initialisation des données de la galerie d'images

Modèle de script :

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

# Données à initialiser
FEATURE_ITEMS = [
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

def create_feature_items_collection(headers):
    """Création de la collection pour les items"""
    # Définition des champs de la collection
    fields = [
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
    ]
    
    # Création de la collection
    return create_collection(headers, "feature_items", fields)

def create_collection(headers, collection_name, fields):
    """Création d'une collection dans Directus"""
    # Vérifier si la collection existe déjà
    response = requests.get(
        f"{DIRECTUS_URL}/collections",
        headers=headers
    )
    
    if response.status_code != 200:
        print(f"Erreur lors de la vérification des collections: {response.text}")
        return False
    
    collections = response.json()["data"]
    if any(collection["collection"] == collection_name for collection in collections):
        print(f"La collection {collection_name} existe déjà.")
        return True
    
    # Créer la collection
    response = requests.post(
        f"{DIRECTUS_URL}/collections",
        headers=headers,
        json={
            "collection": collection_name,
            "meta": {
                "icon": "list",
                "note": f"Collection pour les {collection_name}"
            },
            "schema": {
                "name": collection_name
            },
            "fields": fields
        }
    )
    
    if response.status_code != 200:
        print(f"Erreur lors de la création de la collection: {response.text}")
        return False
    
    print(f"Collection {collection_name} créée avec succès.")
    return True

def add_feature_item(headers, item):
    """Ajout d'un item dans la collection"""
    response = requests.post(
        f"{DIRECTUS_URL}/items/feature_items",
        headers=headers,
        json=item
    )
    
    if response.status_code != 200:
        print(f"Erreur lors de l'ajout de l'item: {response.text}")
        return None
    
    print(f"Item {item['name']} ajouté avec succès.")
    return response.json()["data"]

def main():
    """Point d'entrée principal du script"""
    # Authentification
    access_token = login()
    if not access_token:
        print("Impossible de se connecter à Directus. Vérifiez vos identifiants.")
        return
    
    headers = get_headers(access_token)
    
    # Création de la collection
    if not create_feature_items_collection(headers):
        print("Impossible de créer la collection. Arrêt du script.")
        return
    
    # Ajout des items
    for item in FEATURE_ITEMS:
        add_feature_item(headers, item)
    
    print("Script exécuté avec succès!")

if __name__ == "__main__":
    main()
```

### 5. Créer des composants Vue pour afficher les données

Pour chaque domaine fonctionnel, créez des composants Vue pour afficher les données.

Exemple de composants :
- `MenuGrid.vue` : Affichage du menu
- `ReservationForm.vue` : Formulaire de réservation
- `EventsList.vue` : Liste des événements
- `WineList.vue` : Carte des vins
- `GalleryGrid.vue` : Galerie d'images

Modèle de composant :

```vue
<template>
  <div class="feature-component">
    <div v-if="isLoading" class="loading-container">
      <div class="loading-spinner"></div>
    </div>
    
    <div v-else-if="error" class="error-container">
      <p class="error-message">{{ error }}</p>
    </div>
    
    <div v-else class="items-grid">
      <div v-for="item in items" :key="item.id" class="item-card">
        <h3 class="item-title">{{ item.name }}</h3>
        <p v-if="item.description" class="item-description">{{ item.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useFeature } from '~/composables/useFeature'

const { items, isLoading, error, fetchItems } = useFeature()

onMounted(() => {
  fetchItems()
})
</script>

<style scoped>
.feature-component {
  @apply w-full max-w-4xl mx-auto py-8;
}

.loading-container {
  @apply flex justify-center items-center py-12;
}

.loading-spinner {
  @apply w-10 h-10 border-4 border-orange-500/30 border-t-orange-500 rounded-full;
  animation: spin 1s linear infinite;
}

.error-container {
  @apply bg-red-500/10 border border-red-500/30 rounded-lg p-4 my-4;
}

.error-message {
  @apply text-red-500 text-center;
}

.items-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-6;
}

.item-card {
  @apply bg-black/50 backdrop-blur-sm border border-orange-500/20 rounded-lg p-6 transition-all duration-300 hover:border-orange-500/50;
}

.item-title {
  @apply text-xl font-bold text-orange-500 mb-2;
}

.item-description {
  @apply text-gray-300;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
```

## Bonnes pratiques d'intégration

### 1. Utiliser des types TypeScript

Définissez des interfaces TypeScript pour toutes les données échangées entre le frontend et le backend. Cela garantit la cohérence des données et facilite le développement.

### 2. Gérer les erreurs

Implémentez une gestion des erreurs robuste à tous les niveaux (frontend, backend, scripts).

### 3. Mettre en cache les données

Utilisez des stratégies de mise en cache pour améliorer les performances, comme le stockage des données déjà chargées dans les composables.

### 4. Utiliser des états de chargement

Affichez des indicateurs de chargement pendant les opérations asynchrones pour améliorer l'expérience utilisateur.

### 5. Normaliser les URLs d'images

Assurez-vous que les URLs des images sont correctement normalisées pour fonctionner dans tous les environnements (développement, production).

### 6. Utiliser des transactions

Utilisez des transactions pour les opérations qui modifient plusieurs entités, afin de garantir l'intégrité des données.

### 7. Documenter les API

Documentez clairement les endpoints API et les paramètres attendus pour faciliter l'intégration.

## Exemple complet d'intégration

Voici un exemple complet d'intégration pour la fonctionnalité "Événements" :

1. **Composable** (`useEvents.ts`)
2. **Endpoints API** (`backend/app/api/events.py`)
3. **Collection Directus** (`events`)
4. **Script d'initialisation** (`add_event_data.py`)
5. **Composant Vue** (`EventsList.vue`)

Cette approche peut être appliquée à toutes les fonctionnalités de l'application pour créer une intégration cohérente et maintenable entre le frontend et le backend. 