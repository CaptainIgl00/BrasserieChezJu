# Guide de déploiement

Ce document décrit les étapes nécessaires pour déployer l'application Brasserie Chez Ju en production.

## Prérequis

- Un serveur Linux avec Docker et Docker Compose installés
- Un nom de domaine configuré pour pointer vers l'adresse IP du serveur
- Un accès SSH au serveur

## Architecture de déploiement

L'application est déployée à l'aide de Docker et Docker Compose, avec Traefik comme reverse proxy pour gérer le routage et les certificats SSL.

```
┌─────────────────────────────────────────────────────────────────┐
│                           Traefik                               │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
┌───────────────▼───┐ ┌─────────▼─────────┐ ┌───▼───────────────┐
│                   │ │                   │ │                   │
│    Frontend       │ │    Backend API    │ │    Directus       │
│    (Nuxt)         │ │    (FastAPI)      │ │                   │
└───────────────────┘ └───────────────────┘ └───────────────────┘
                                                      │
                                                      │
                                            ┌─────────▼─────────┐
                                            │                   │
                                            │    PostgreSQL     │
                                            │                   │
                                            └───────────────────┘
```

## Étapes de déploiement

### 1. Préparation du serveur

```bash
# Mettre à jour le système
sudo apt update && sudo apt upgrade -y

# Installer Docker si nécessaire
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Installer Docker Compose si nécessaire
sudo curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Créer un utilisateur pour exécuter Docker
sudo useradd -m -s /bin/bash -G docker deployer
```

### 2. Configuration des variables d'environnement

```bash
# Copier les fichiers d'environnement
cp .env.example .env
cp .env.backend.example .env.backend

# Modifier les valeurs selon l'environnement de production
nano .env
nano .env.backend
```

Assurez-vous de définir les variables suivantes dans `.env.backend` :
- `DIRECTUS_PUBLIC_URL` : URL publique de Directus (ex: https://admin.brasseriechezju.com)
- `ADMIN_EMAIL` et `ADMIN_PASSWORD` : Identifiants pour l'administrateur Directus
- `DB_USER`, `DB_PASSWORD` et `DB_NAME` : Informations de connexion à la base de données
- `FRONTEND_URL` : URL du frontend (ex: https://brasseriechezju.com)

### 3. Déploiement du backend

```bash
# Démarrer les services backend
docker-compose -f docker-compose.backend.yml up -d
```

### 4. Initialisation des données

```bash
# Exécuter le script d'initialisation des données du menu
docker-compose -f docker-compose.backend.yml exec fastapi python /app/scripts/add_menu_data.py
```

### 5. Déploiement du frontend

```bash
# Construire l'image Docker du frontend
docker build -t brasseriechezju-frontend .

# Démarrer les services frontend
docker-compose up -d
```

### 6. Vérification du déploiement

```bash
# Vérifier que tous les conteneurs sont en cours d'exécution
docker-compose ps
docker-compose -f docker-compose.backend.yml ps

# Vérifier les logs pour détecter d'éventuelles erreurs
docker-compose logs -f
docker-compose -f docker-compose.backend.yml logs -f
```

## Mise à jour de l'application

### Mise à jour du backend

```bash
# Arrêter les services backend
docker-compose -f docker-compose.backend.yml down

# Récupérer les dernières modifications
git pull

# Redémarrer les services backend
docker-compose -f docker-compose.backend.yml up -d
```

### Mise à jour du frontend

```bash
# Arrêter les services frontend
docker-compose down

# Récupérer les dernières modifications
git pull

# Reconstruire l'image Docker du frontend
docker build -t brasseriechezju-frontend .

# Redémarrer les services frontend
docker-compose up -d
```

## Sauvegarde et restauration

### Sauvegarde de la base de données

```bash
# Créer un répertoire pour les sauvegardes
mkdir -p backups

# Sauvegarder la base de données PostgreSQL
docker-compose -f docker-compose.backend.yml exec postgres pg_dump -U $DB_USER $DB_NAME > backups/database_$(date +%Y%m%d).sql
```

### Sauvegarde des fichiers Directus

```bash
# Sauvegarder les fichiers téléchargés dans Directus
docker run --rm -v brasseriechezju_directus_uploads:/source -v $(pwd)/backups:/destination ubuntu tar -czf /destination/directus_uploads_$(date +%Y%m%d).tar.gz -C /source .
```

### Restauration de la base de données

```bash
# Restaurer la base de données PostgreSQL
cat backups/database_YYYYMMDD.sql | docker-compose -f docker-compose.backend.yml exec -T postgres psql -U $DB_USER $DB_NAME
```

### Restauration des fichiers Directus

```bash
# Restaurer les fichiers téléchargés dans Directus
docker run --rm -v brasseriechezju_directus_uploads:/destination -v $(pwd)/backups:/source ubuntu bash -c "rm -rf /destination/* && tar -xzf /source/directus_uploads_YYYYMMDD.tar.gz -C /destination"
```

## Résolution des problèmes courants

### Problème de connexion à la base de données

Vérifiez les variables d'environnement dans `.env.backend` et assurez-vous que les informations de connexion sont correctes.

```bash
# Vérifier les logs de PostgreSQL
docker-compose -f docker-compose.backend.yml logs postgres
```

### Problème de certificat SSL

Vérifiez les logs de Traefik pour voir si les certificats ont été correctement générés.

```bash
# Vérifier les logs de Traefik
docker-compose logs traefik
```

### Problème d'accès à l'API

Vérifiez que le service FastAPI est en cours d'exécution et que les variables d'environnement sont correctement configurées.

```bash
# Vérifier les logs de FastAPI
docker-compose -f docker-compose.backend.yml logs fastapi
``` 