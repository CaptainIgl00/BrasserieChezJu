#!/bin/bash

# Créer un nouvel utilisateur administrateur dans Directus
echo "Création d'un nouvel utilisateur administrateur dans Directus..."

# Exécuter la commande à l'intérieur du conteneur Directus
docker exec -it brasseriechezju_directus_1 npx directus bootstrap

# Afficher les utilisateurs existants
echo "Utilisateurs existants dans Directus:"
docker exec -it brasseriechezju_directus_1 npx directus users list

echo ""
echo "Vous pouvez maintenant vous connecter à l'interface d'administration de Directus:"
echo "URL: http://localhost:8055" 