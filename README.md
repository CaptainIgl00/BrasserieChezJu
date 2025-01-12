# Brasserie Chez Ju - Site Web

Site web de la Brasserie Chez Ju, un restaurant traditionnel situé à Carcassonne. Développé avec Nuxt 3 et déployé sur une VM Alpine Linux.

## Technologies

- **Frontend**: Nuxt 3, Vue.js, TailwindCSS
- **Déploiement**: Docker, GitHub Actions
- **Serveur**: Nginx, Alpine Linux

## Fonctionnalités

- Page d'accueil avec présentation du restaurant
- Menu interactif avec catégories
- Section équipe
- Galerie d'images
- Intégration Instagram
- Formulaire de contact
- Design responsive

## Installation locale

```bash
# Installer les dépendances
npm install

# Lancer en mode développement
npm run dev

# Build pour la production
npm run build
```

## Déploiement Docker

Le projet utilise Docker pour le déploiement. Pour lancer l'application :

```bash
# Build et démarrage
docker-compose up -d

# Vérifier le statut
docker-compose ps

# Arrêter les conteneurs
docker-compose down
```

## Structure du projet

```
├── components/          # Composants Vue réutilisables
├── pages/              # Pages de l'application
├── public/             # Assets statiques
│   ├── images/         # Images du site
│   └── fonts/          # Polices personnalisées
├── nginx/              # Configuration Nginx
└── docker-compose.yml  # Configuration Docker
```

## Déploiement automatique

Le déploiement est automatisé via GitHub Actions. À chaque push sur la branche `main` :
1. Build de l'image Docker
2. Push sur Docker Hub
3. Déploiement sur la VM Alpine Linux
