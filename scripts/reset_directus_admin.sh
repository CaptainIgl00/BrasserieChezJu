#!/bin/bash

# Réinitialiser le mot de passe de l'administrateur Directus
echo "Réinitialisation du mot de passe de l'administrateur Directus..."

# Exécuter la commande à l'intérieur du conteneur Directus
docker exec -it brasseriechezju_directus_1 npx directus users passwd --email admin@example.com --password admin_password_123

echo "Mot de passe réinitialisé avec succès!"
echo "Email: admin@example.com"
echo "Mot de passe: admin_password_123"
echo ""
echo "Vous pouvez maintenant vous connecter à l'interface d'administration de Directus:"
echo "URL: http://localhost:8055" 