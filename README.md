# Brasserie Chez Ju

Site web de la Brasserie Chez Ju, un restaurant traditionnel français.

## Architecture du projet

Le projet est composé de deux parties principales :

1. **Frontend** : Application Nuxt 3 avec TailwindCSS
2. **Backend** : API FastAPI + CMS Directus avec PostgreSQL

### Frontend (Nuxt 3)

Le frontend est une application Nuxt 3 qui utilise TailwindCSS pour le style. Il est conçu pour être responsive et offrir une expérience utilisateur optimale sur tous les appareils.

### Backend (FastAPI + Directus)

Le backend est composé de deux éléments principaux :

- **FastAPI** : API REST qui expose les données au frontend
- **Directus** : CMS headless qui permet de gérer facilement le contenu (images, textes, etc.)
- **PostgreSQL** : Base de données relationnelle

## Installation et démarrage

### Prérequis

- Docker et Docker Compose
- Node.js 18+ et npm/yarn

### Frontend

```bash
# Installation des dépendances
npm install

# Démarrage du serveur de développement
npm run dev

# Construction pour la production
npm run build
```

### Backend

```bash
# Copier le fichier d'environnement
cp .env.backend .env

# Modifier les valeurs dans .env selon vos besoins
nano .env

# Démarrer les services backend
docker-compose -f docker-compose.backend.yml up -d
```

## Déploiement

Le projet est configuré pour être déployé avec Docker et Traefik comme reverse proxy. Le fichier `docker-compose.yml` à la racine du projet contient la configuration pour le déploiement du frontend, tandis que `docker-compose.backend.yml` contient la configuration pour le déploiement du backend.

```bash
# Déploiement du frontend
docker-compose up -d

# Déploiement du backend
docker-compose -f docker-compose.backend.yml up -d
```

Pour plus de détails sur le déploiement, consultez le [Guide de déploiement](docs/deployment/deployment_guide.md).

## Structure du projet

```
/
├── app.vue                  # Point d'entrée de l'application Nuxt
├── components/              # Composants Vue réutilisables
│   ├── layout/              # Composants de mise en page
│   ├── menu/                # Composants liés au menu
│   └── home/                # Composants de la page d'accueil
├── composables/             # Composables Vue (hooks)
├── pages/                   # Pages de l'application
├── public/                  # Fichiers statiques
├── backend/                 # Code du backend FastAPI
│   ├── app/                 # Application FastAPI
│   │   ├── api/             # Endpoints API
│   │   ├── core/            # Configuration et utilitaires
│   │   ├── models/          # Modèles de données
│   │   ├── schemas/         # Schémas Pydantic
│   │   └── main.py          # Point d'entrée de l'API
│   ├── Dockerfile           # Dockerfile pour le backend
│   └── requirements.txt     # Dépendances Python
├── docker-compose.yml       # Configuration Docker pour le frontend
├── docker-compose.backend.yml # Configuration Docker pour le backend
└── .env.backend             # Variables d'environnement pour le backend
```

## Interface d'administration

L'interface d'administration Directus est accessible à l'adresse suivante :

```
https://admin.brasseriechezju.com
```

Elle permet de gérer facilement le contenu du site, notamment :

- Les catégories de menu
- Les plats et leurs images
- La carte des vins
- Les suggestions du jour

## Développement

### Frontend

Le frontend utilise Nuxt 3 avec les fonctionnalités suivantes :

- Composables pour la gestion de l'état et les appels API
- Composants Vue réutilisables
- TailwindCSS pour le style
- Optimisation des images avec @nuxt/image

### Backend

Le backend utilise FastAPI avec les fonctionnalités suivantes :

- Architecture en couches (API, services, modèles)
- Validation des données avec Pydantic
- Documentation automatique avec Swagger UI
- Intégration avec Directus pour la gestion du contenu

## Documentation

Pour plus d'informations sur le projet, consultez la documentation suivante :

- [Vue d'ensemble de l'architecture](docs/architecture/overview.md) - Description détaillée de l'architecture du projet
- [Intégration Frontend-Backend](docs/development/frontend_backend_integration.md) - Guide pour intégrer le frontend et le backend
- [Scripts de gestion des données](docs/scripts/data_management.md) - Documentation sur les scripts d'automatisation
- [Guide de déploiement](docs/deployment/deployment_guide.md) - Instructions détaillées pour le déploiement

## Licence

Ce projet est sous licence privée. Tous droits réservés.
