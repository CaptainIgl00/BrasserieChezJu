# TODO - Brasserie Chez Ju

Ce fichier liste les tâches à réaliser pour compléter le développement de l'application Brasserie Chez Ju. **Important** : Effectuez une tâche à la fois pour maintenir la cohérence du projet.

## Fonctionnalités à implémenter

### Carte des vins

- [x] Créer le composable `useWines.ts` pour gérer les données des vins
  - Utiliser le template `useTemplate.ts` comme base
  - Adapter les interfaces pour correspondre au schéma `wine.py`
  - Implémenter les fonctions pour récupérer, filtrer et trier les vins

- [x] Créer le script `add_wine_data.py` pour initialiser les données des vins
  - Utiliser le template `template_data_script.py` comme base
  - Adapter les fonctions pour créer la collection des vins
  - Ajouter les données des vins depuis le composant `WineList.vue`

- [x] Mettre à jour le composant `WineList.vue` pour utiliser le composable `useWines.ts`
  - Remplacer les données statiques par les données dynamiques du composable
  - Ajouter des filtres et des options de tri

### Réservations

- [ ] Créer le schéma `reservation.py` pour définir la structure des réservations
  - Utiliser le template `template.py` comme base
  - Définir les champs nécessaires (date, heure, nombre de personnes, nom, téléphone, etc.)

- [ ] Créer l'endpoint API `reservations.py` pour gérer les réservations
  - Utiliser le template `template.py` comme base
  - Implémenter les routes pour créer, lire, mettre à jour et supprimer des réservations

- [ ] Créer le composable `useReservation.ts` pour gérer les données des réservations
  - Utiliser le template `useTemplate.ts` comme base
  - Adapter les interfaces pour correspondre au schéma `reservation.py`
  - Implémenter les fonctions pour créer et gérer les réservations

- [ ] Créer le script `add_reservation_data.py` pour initialiser la collection des réservations
  - Utiliser le template `template_data_script.py` comme base
  - Adapter les fonctions pour créer la collection des réservations

- [ ] Créer le composant `ReservationForm.vue` pour permettre aux utilisateurs de faire des réservations
  - Utiliser le template `TemplateComponent.vue` comme base
  - Adapter le formulaire pour les réservations
  - Implémenter la validation des données

- [ ] Créer la page `reservation.vue` pour afficher le formulaire de réservation
  - Intégrer le composant `ReservationForm.vue`
  - Ajouter des informations sur les politiques de réservation

### Événements (Composant InstragramFeed.vue)

- [ ] Créer le schéma `event.py` pour définir la structure des événements
  - Utiliser le template `template.py` comme base
  - Définir les champs nécessaires (titre, date, description, image, etc.)

- [ ] Créer l'endpoint API `events.py` pour gérer les événements
  - Utiliser le template `template.py` comme base
  - Implémenter les routes pour créer, lire, mettre à jour et supprimer des événements

- [ ] Créer le composable `useEvents.ts` pour gérer les données des événements
  - Utiliser le template `useTemplate.ts` comme base
  - Adapter les interfaces pour correspondre au schéma `event.py`
  - Implémenter les fonctions pour récupérer et filtrer les événements

- [ ] Créer le script `add_event_data.py` pour initialiser les données des événements
  - Utiliser le template `template_data_script.py` comme base
  - Adapter les fonctions pour créer la collection des événements
  - Ajouter des données d'exemple pour les événements

- [ ] Créer le composant `EventsList.vue` pour afficher les événements
  - Utiliser le template `TemplateComponent.vue` comme base
  - Adapter l'affichage pour les événements
  - Ajouter des filtres par date

- [ ] Créer la page `events.vue` pour afficher les événements
  - Intégrer le composant `EventsList.vue`
  - Ajouter des informations sur les types d'événements proposés

### Galerie d'images

- [ ] Créer le schéma `gallery.py` pour définir la structure des images de la galerie
  - Utiliser le template `template.py` comme base
  - Définir les champs nécessaires (titre, description, image, catégorie, etc.)

- [ ] Créer l'endpoint API `gallery.py` pour gérer les images de la galerie
  - Utiliser le template `template.py` comme base
  - Implémenter les routes pour créer, lire, mettre à jour et supprimer des images

- [ ] Créer le composable `useGallery.ts` pour gérer les données de la galerie
  - Utiliser le template `useTemplate.ts` comme base
  - Adapter les interfaces pour correspondre au schéma `gallery.py`
  - Implémenter les fonctions pour récupérer et filtrer les images

- [ ] Créer le script `add_gallery_data.py` pour initialiser les données de la galerie
  - Utiliser le template `template_data_script.py` comme base
  - Adapter les fonctions pour créer la collection de la galerie
  - Ajouter des données d'exemple pour les images

- [ ] Créer le composant `GalleryGrid.vue` pour afficher les images de la galerie
  - Utiliser le template `TemplateComponent.vue` comme base
  - Adapter l'affichage pour les images
  - Ajouter des filtres par catégorie

- [ ] Créer la page `gallery.vue` pour afficher la galerie d'images
  - Intégrer le composant `GalleryGrid.vue`
  - Ajouter des informations sur les catégories d'images

### Page de contact

- [ ] Créer le schéma `contact.py` pour définir la structure des messages de contact
  - Utiliser le template `template.py` comme base
  - Définir les champs nécessaires (nom, email, téléphone, message, etc.)

- [ ] Créer l'endpoint API `contact.py` pour gérer les messages de contact
  - Utiliser le template `template.py` comme base
  - Implémenter les routes pour créer et lire des messages de contact

- [ ] Créer le composable `useContact.ts` pour gérer les données de contact
  - Utiliser le template `useTemplate.ts` comme base
  - Adapter les interfaces pour correspondre au schéma `contact.py`
  - Implémenter les fonctions pour envoyer des messages de contact

- [ ] Créer le script `add_contact_data.py` pour initialiser la collection des messages de contact
  - Utiliser le template `template_data_script.py` comme base
  - Adapter les fonctions pour créer la collection des messages de contact

- [ ] Créer le composant `ContactForm.vue` pour permettre aux utilisateurs d'envoyer des messages
  - Utiliser le template `TemplateComponent.vue` comme base
  - Adapter le formulaire pour les messages de contact
  - Implémenter la validation des données

- [ ] Créer la page `contact.vue` pour afficher le formulaire de contact
  - Intégrer le composant `ContactForm.vue`
  - Ajouter des informations de contact (adresse, téléphone, email, etc.)
  - Ajouter une carte Google Maps

## Améliorations générales

- [ ] Ajouter une page d'administration pour gérer les données
  - Créer une interface d'administration simple pour les données
  - Implémenter l'authentification pour l'accès à l'administration

- [ ] Améliorer la gestion des erreurs
  - Ajouter des messages d'erreur plus détaillés
  - Implémenter des mécanismes de retry pour les appels API

- [ ] Optimiser les performances
  - Implémenter la mise en cache des données
  - Optimiser le chargement des images

- [ ] Améliorer l'accessibilité
  - Ajouter des attributs ARIA
  - Améliorer la navigation au clavier

- [ ] Ajouter des tests
  - Ajouter des tests unitaires pour les composables
  - Ajouter des tests d'intégration pour les API
  - Ajouter des tests end-to-end pour les fonctionnalités principales 