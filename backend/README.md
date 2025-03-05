# Backend Brasserie Chez Ju

Ce backend est construit avec FastAPI et Directus pour gérer le contenu du site web de la Brasserie Chez Ju.

## Architecture

- **FastAPI**: API REST pour exposer les données au frontend
- **Directus**: CMS headless pour gérer les contenus (images, textes, etc.)
- **PostgreSQL**: Base de données relationnelle

## Installation et démarrage

### Prérequis

- Docker et Docker Compose
- Un fichier `.env` avec les variables d'environnement nécessaires

### Démarrage

```bash
# À la racine du projet
cp .env.backend .env
# Modifier les valeurs dans .env selon vos besoins
docker-compose -f docker-compose.backend.yml up -d
```

## Structure du projet

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── categories.py
│   │       │   ├── dishes.py
│   │       │   ├── menu.py
│   │       │   └── wines.py
│   │       └── api.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   ├── schemas/
│   │   ├── category.py
│   │   ├── dish.py
│   │   ├── wine.py
│   │   └── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt
```

## API Endpoints

### Menu

- `GET /api/v1/menu/complete`: Récupérer le menu complet avec toutes les catégories et leurs plats
- `GET /api/v1/menu/wines`: Récupérer la carte des vins complète
- `GET /api/v1/menu/daily-specials`: Récupérer les suggestions du jour

### Catégories

- `GET /api/v1/categories`: Récupérer toutes les catégories
- `GET /api/v1/categories/{category_id}`: Récupérer une catégorie par son ID
- `POST /api/v1/categories`: Créer une nouvelle catégorie
- `PATCH /api/v1/categories/{category_id}`: Mettre à jour une catégorie
- `DELETE /api/v1/categories/{category_id}`: Supprimer une catégorie

### Plats

- `GET /api/v1/dishes`: Récupérer tous les plats
- `GET /api/v1/dishes/{dish_id}`: Récupérer un plat par son ID
- `POST /api/v1/dishes`: Créer un nouveau plat
- `PATCH /api/v1/dishes/{dish_id}`: Mettre à jour un plat
- `DELETE /api/v1/dishes/{dish_id}`: Supprimer un plat

### Vins

- `GET /api/v1/wines`: Récupérer tous les vins
- `GET /api/v1/wines/{wine_id}`: Récupérer un vin par son ID
- `POST /api/v1/wines`: Créer un nouveau vin
- `PATCH /api/v1/wines/{wine_id}`: Mettre à jour un vin
- `DELETE /api/v1/wines/{wine_id}`: Supprimer un vin

## Interface d'administration Directus

L'interface d'administration Directus est accessible à l'adresse suivante:

```
https://admin.brasseriechezju.com
```

Utilisez les identifiants définis dans le fichier `.env` pour vous connecter. 