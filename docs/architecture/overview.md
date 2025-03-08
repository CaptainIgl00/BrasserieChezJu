# Architecture de Brasserie Chez Ju

## Vue d'ensemble

Le projet Brasserie Chez Ju est construit selon une architecture moderne et modulaire, séparant clairement le frontend du backend tout en permettant une communication efficace entre les deux.

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│                 │      │                 │      │                 │
│  Frontend Nuxt  │◄────►│  Backend API    │◄────►│  CMS Directus   │
│                 │      │  (FastAPI)      │      │                 │
└─────────────────┘      └─────────────────┘      └─────────────────┘
                                                          ▲
                                                          │
                                                          ▼
                                                  ┌─────────────────┐
                                                  │                 │
                                                  │  PostgreSQL     │
                                                  │                 │
                                                  └─────────────────┘
```

## Composants principaux

### Frontend (Nuxt 3)

Le frontend est développé avec Nuxt 3, un framework basé sur Vue.js qui offre des fonctionnalités avancées comme le rendu côté serveur (SSR), la génération de sites statiques, et une architecture basée sur des composants.

**Points clés :**
- **Composables** : Utilisation de composables Vue pour encapsuler la logique métier et les appels API
- **Composants** : Organisation modulaire avec des composants réutilisables
- **Pages** : Structure de routage automatique basée sur les fichiers
- **TailwindCSS** : Utilisé pour le styling avec une approche utility-first

### Backend (FastAPI)

Le backend est construit avec FastAPI, un framework Python moderne et performant pour la création d'APIs RESTful.

**Points clés :**
- **Architecture en couches** : Séparation claire entre les routes API, les services et les modèles
- **Validation des données** : Utilisation de Pydantic pour la validation et la sérialisation
- **Documentation automatique** : API documentée automatiquement avec Swagger UI
- **Middleware CORS** : Configuration pour permettre les requêtes cross-origin du frontend

### CMS (Directus)

Directus est utilisé comme CMS headless pour gérer le contenu du site.

**Points clés :**
- **Collections personnalisées** : Structure de données adaptée aux besoins du restaurant
- **API REST** : Exposition des données via une API REST
- **Gestion des assets** : Stockage et transformation des images
- **Interface d'administration** : Interface conviviale pour la gestion du contenu

### Base de données (PostgreSQL)

PostgreSQL est utilisé comme système de gestion de base de données relationnelle.

**Points clés :**
- **Schéma relationnel** : Structure de données optimisée pour les besoins du restaurant
- **Performances** : Base de données robuste et performante
- **Extensibilité** : Possibilité d'ajouter des extensions selon les besoins

## Flux de données

1. Le frontend fait des requêtes HTTP à l'API FastAPI
2. FastAPI traite ces requêtes et interagit avec Directus via son API REST
3. Directus gère les opérations CRUD sur la base de données PostgreSQL
4. Les données sont renvoyées à FastAPI qui les transforme si nécessaire
5. FastAPI renvoie les données au frontend dans un format JSON optimisé

## Scripts d'automatisation

Des scripts Python sont utilisés pour automatiser certaines tâches comme l'initialisation de la base de données ou l'import de données. Ces scripts interagissent directement avec l'API Directus pour maintenir la cohérence des données.

## Déploiement

L'application est déployée à l'aide de Docker et Docker Compose, avec Traefik comme reverse proxy pour gérer le routage et les certificats SSL. 