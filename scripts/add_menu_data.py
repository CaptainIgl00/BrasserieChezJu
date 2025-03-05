#!/usr/bin/env python3
import requests
import os
import json
import mimetypes
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv('.env.backend')

# Configuration
DIRECTUS_URL = os.getenv('DIRECTUS_PUBLIC_URL', 'http://localhost:8055')
DIRECTUS_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@example.com')
DIRECTUS_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin_password_123')

# Chemin vers les images
IMAGES_DIR = "public/images/menu"

# Données des catégories de menu
MENU_CATEGORIES = [
    {
        "name": "Toc toc toc... entrées",
        "description": "Nos entrées fraîches et savoureuses"
    },
    {
        "name": "On se met au vert ?",
        "description": "Nos salades et plats légers"
    },
    {
        "name": "T'as faim de tradition ?",
        "description": "Nos plats traditionnels"
    },
    {
        "name": "Côté Mer",
        "description": "Nos plats de poissons et fruits de mer"
    },
    {
        "name": "Côté Terre",
        "description": "Nos plats de viande et pâtes"
    },
    {
        "name": "Côté Flamme",
        "description": "Nos grillades"
    },
    {
        "name": "Finir en douceur",
        "description": "Nos desserts maison"
    }
]

# Données des plats
DISHES = [
    # Toc toc toc... entrées (starters)
    {
        "name": "Planche de jambon Serrano et jambon blanc truffé",
        "description": "",
        "price": 17.00,
        "image": "planche_charcuterie.jpg",
        "category": "Toc toc toc... entrées"
    },
    {
        "name": "Camembert entier rôti au piment d'Espelette",
        "description": "Servi avec ses mouillettes",
        "price": 14.00,
        "image": "",
        "category": "Toc toc toc... entrées"
    },
    {
        "name": "Tapenade maison et ses toasts grillés",
        "description": "",
        "price": 8.00,
        "image": "tapenade.png",
        "category": "Toc toc toc... entrées"
    },
    {
        "name": "Planche de foie gras mi-cuit du Périgord",
        "description": "1 tranche 15€ ou 2 tranches 24€",
        "price": 15.00,
        "image": "foie_gras.jpg",
        "category": "Toc toc toc... entrées"
    },
    {
        "name": "Filets de sardines fraîches",
        "description": "Marinés au cidre et aux agrumes",
        "price": 14.00,
        "image": "",
        "category": "Toc toc toc... entrées"
    },
    {
        "name": "Soupe de lentilles du Pays d'Oc",
        "description": "Avec ses lardons, croûtons et son œuf fermier mollet",
        "price": 13.00,
        "image": "",
        "category": "Toc toc toc... entrées"
    },
    {
        "name": "La grande planche de Becq à partager",
        "description": "Serrano, jambon truffé, foie gras, camembert rôti, saumon mariné, sardines, tapenade",
        "price": 59.00,
        "image": "",
        "category": "Toc toc toc... entrées"
    },
    
    # On se met au vert ? (salads)
    {
        "name": "Salade César",
        "description": "Poulet pané, tomates, olives, croûtons, parmesan, œuf fermier mollet frit, sauce césar",
        "price": 19.00,
        "image": "",
        "category": "On se met au vert ?"
    },
    {
        "name": "Salade Gourmande",
        "description": "Gésiers, toast de foie gras, œuf fermier mollet frit, tomates, olives",
        "price": 21.00,
        "image": "",
        "category": "On se met au vert ?"
    },
    {
        "name": "Escalopes de saumon mariné à l'aneth",
        "description": "Frites maison et salade",
        "price": 21.00,
        "image": "saumon.png",
        "category": "On se met au vert ?"
    },
    
    # T'as faim de tradition ? (traditional)
    {
        "name": "Cassoulet du chef Becq",
        "description": "Élaboré dans le respect de la tradition, servi avec sa salade",
        "price": 24.00,
        "image": "cassoulet.jpg",
        "category": "T'as faim de tradition ?"
    },
    {
        "name": "Le fameux Welsh de Fred au Maroilles",
        "description": "Œuf poché, frites maison et salade",
        "price": 16.00,
        "image": "welch.jpg",
        "category": "T'as faim de tradition ?"
    },
    
    # Côté Mer (seafood)
    {
        "name": "Filets de bar à la plancha",
        "description": "Toast de tapenade, sauce vierge à la ricotta et roquette",
        "price": 24.00,
        "image": "filet_de_bar.jpg",
        "category": "Côté Mer"
    },
    {
        "name": "Seiches à la plancha",
        "description": "En persillade (500g)",
        "price": 20.00,
        "image": "",
        "category": "Côté Mer"
    },
    
    # Côté Terre (meat)
    {
        "name": "Le Burger de Ju",
        "description": "Steak haché de 180g, oignons confits grenadine, sauce cheddar, tomate, cornichon et servi avec ses frites maison",
        "price": 21.00,
        "image": "burger.png",
        "category": "Côté Terre"
    },
    {
        "name": "Tartare de bœuf",
        "description": "Ses condiments, ses frites maison et sa salade verte - Simple 180g",
        "price": 20.00,
        "image": "",
        "category": "Côté Terre"
    },
    {
        "name": "Tartare de bœuf double",
        "description": "360g",
        "price": 35.00,
        "image": "",
        "category": "Côté Terre"
    },
    {
        "name": "Tagliatelles de Ju",
        "description": "Magret de canard, sauce cèpes et parmesan",
        "price": 23.00,
        "image": "",
        "category": "Côté Terre"
    },
    {
        "name": "Tagliatelles fraîches",
        "description": "Au pesto et parmesan",
        "price": 14.00,
        "image": "",
        "category": "Côté Terre"
    },
    
    # Côté Flamme (grill)
    {
        "name": "Entrecôte grillée",
        "description": "Beurre maître d'hôtel (350 g)",
        "price": 28.00,
        "image": "entrecote.png",
        "category": "Côté Flamme"
    },
    {
        "name": "Magret de canard du Périgord",
        "description": "Grillé fleur de sel de Guérande",
        "price": 26.00,
        "image": "magret.jpg",
        "category": "Côté Flamme"
    },
    {
        "name": "Côte de porc noir de Bigorre",
        "description": "En deux cuissons (500 g)",
        "price": 35.00,
        "image": "cote_porc.png",
        "category": "Côté Flamme"
    },
    {
        "name": "Le demi lapin du Lauragais",
        "description": "Grillé et son aïoli (800 g)",
        "price": 27.00,
        "image": "",
        "category": "Côté Flamme"
    },
    {
        "name": "Côte de bœuf à partager",
        "description": "Demandez l'ardoise. Sauces aux choix: Poivre, cèpes ou roquefort 4€",
        "price": 55.00,
        "image": "",
        "category": "Côté Flamme"
    },
    
    # Finir en douceur (desserts)
    {
        "name": "Plateau de fromage de l'épicerie fine \"Chez Julien\"",
        "description": "",
        "price": 16.00,
        "image": "",
        "category": "Finir en douceur"
    },
    {
        "name": "Moelleux au chocolat",
        "description": "Crème anglaise",
        "price": 7.00,
        "image": "moelleux.png",
        "category": "Finir en douceur"
    },
    {
        "name": "Crème brûlée",
        "description": "Au caramel beurre salé",
        "price": 7.00,
        "image": "creme_brulee.jpg",
        "category": "Finir en douceur"
    },
    {
        "name": "Pavlova aux fruits rouges",
        "description": "Et sa chantilly au pamplemousse",
        "price": 9.00,
        "image": "pavlova.jpg",
        "category": "Finir en douceur"
    },
    {
        "name": "Profiterole XL",
        "description": "Chocolat chaud",
        "price": 9.00,
        "image": "profiteroles.jpg",
        "category": "Finir en douceur"
    },
    {
        "name": "Café ou chocolat liégeois",
        "description": "",
        "price": 9.00,
        "image": "",
        "category": "Finir en douceur"
    },
    {
        "name": "Café ou thé gourmand",
        "description": "",
        "price": 10.00,
        "image": "cafe_gourmand.jpg",
        "category": "Finir en douceur"
    },
    {
        "name": "Glaces",
        "description": "1 boule 3,50€, 2 boules 6€, 3 boules 8€, Supplément chantilly 1,50€",
        "price": 3.50,
        "image": "glace.png",
        "category": "Finir en douceur"
    },
    {
        "name": "Irish coffee ou Colonel",
        "description": "",
        "price": 12.00,
        "image": "",
        "category": "Finir en douceur"
    }
]

def login():
    """Se connecter à Directus et obtenir un token d'accès"""
    login_url = f"{DIRECTUS_URL}/auth/login"
    login_data = {
        "email": DIRECTUS_EMAIL,
        "password": DIRECTUS_PASSWORD
    }
    
    response = requests.post(login_url, json=login_data)
    
    if response.status_code == 200:
        access_token = response.json()['data']['access_token']
        print("Connexion à Directus réussie")
        return access_token
    else:
        print(f"Erreur de connexion: {response.status_code}")
        print(response.text)
        return None

def get_headers(access_token):
    """Préparer les en-têtes pour les requêtes API"""
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

def create_collection(headers, collection_name, fields):
    """Créer une collection dans Directus"""
    print(f"Création de la collection {collection_name}...")
    
    # Vérifier si la collection existe déjà
    check_url = f"{DIRECTUS_URL}/collections/{collection_name}"
    check_response = requests.get(check_url, headers=headers)
    
    if check_response.status_code == 200:
        print(f"La collection {collection_name} existe déjà")
        return True
    
    # Créer la collection
    url = f"{DIRECTUS_URL}/collections"
    collection_data = {
        "collection": collection_name,
        "meta": {
            "icon": "list",
            "note": f"Collection pour {collection_name}",
            "display_template": "{{name}}"
        },
        "schema": {
            "name": collection_name,
            "comment": f"Collection pour {collection_name}"
        },
        "fields": fields
    }
    
    response = requests.post(url, headers=headers, json=collection_data)
    
    if response.status_code == 200:
        print(f"Collection {collection_name} créée avec succès")
        return True
    else:
        print(f"Erreur lors de la création de la collection {collection_name}: {response.status_code}")
        print(response.text)
        return False

def upload_image(headers, image_path):
    """Uploader une image dans Directus"""
    url = f"{DIRECTUS_URL}/files"
    
    # Déterminer le type MIME de l'image
    mime_type, _ = mimetypes.guess_type(image_path)
    
    # Préparer les données du formulaire
    files = {
        'file': (os.path.basename(image_path), open(image_path, 'rb'), mime_type)
    }
    
    # Supprimer l'en-tête Content-Type pour permettre à requests de définir le boundary
    upload_headers = headers.copy()
    upload_headers.pop("Content-Type", None)
    
    response = requests.post(url, headers=upload_headers, files=files)
    
    if response.status_code == 200:
        file_id = response.json()['data']['id']
        print(f"Image {os.path.basename(image_path)} uploadée avec succès (ID: {file_id})")
        return file_id
    else:
        print(f"Erreur lors de l'upload de l'image {os.path.basename(image_path)}: {response.status_code}")
        print(response.text)
        return None

def add_menu_category(headers, category):
    """Ajouter une catégorie de menu"""
    url = f"{DIRECTUS_URL}/items/menu_categories"
    
    response = requests.post(url, headers=headers, json=category)
    
    if response.status_code == 200:
        category_id = response.json()['data']['id']
        print(f"Catégorie {category['name']} ajoutée avec succès (ID: {category_id})")
        return category_id
    else:
        print(f"Erreur lors de l'ajout de la catégorie {category['name']}: {response.status_code}")
        print(response.text)
        return None

def add_dish(headers, dish, image_id):
    """Ajouter un plat"""
    url = f"{DIRECTUS_URL}/items/dishes"
    
    # Préparer les données du plat
    dish_data = {
        "name": dish["name"],
        "description": dish["description"],
        "price": str(dish["price"]),  # Convertir en chaîne pour éviter les problèmes de précision
        "category": dish["category"],
        "image": image_id
    }
    
    response = requests.post(url, headers=headers, json=dish_data)
    
    if response.status_code == 200:
        dish_id = response.json()['data']['id']
        print(f"Plat {dish['name']} ajouté avec succès (ID: {dish_id})")
        return dish_id
    else:
        print(f"Erreur lors de l'ajout du plat {dish['name']}: {response.status_code}")
        print(response.text)
        return None

def create_menu_categories_collection(headers):
    """Créer la collection pour les catégories de menu"""
    fields = [
        {
            "field": "id",
            "type": "uuid",
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
                    "placeholder": "Nom de la catégorie"
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
                    "placeholder": "Description de la catégorie"
                }
            },
            "schema": {
                "is_nullable": True
            }
        }
    ]
    
    return create_collection(headers, "menu_categories", fields)

def create_dishes_collection(headers):
    """Créer la collection pour les plats"""
    fields = [
        {
            "field": "id",
            "type": "uuid",
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
                    "placeholder": "Nom du plat"
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
                    "placeholder": "Description du plat"
                }
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "price",
            "type": "string",
            "meta": {
                "interface": "input",
                "options": {
                    "placeholder": "Prix du plat"
                }
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "category",
            "type": "string",
            "meta": {
                "interface": "select-dropdown",
                "options": {
                    "choices": [
                        {"text": "Toc toc toc... entrées", "value": "Toc toc toc... entrées"},
                        {"text": "On se met au vert ?", "value": "On se met au vert ?"},
                        {"text": "T'as faim de tradition ?", "value": "T'as faim de tradition ?"},
                        {"text": "Côté Mer", "value": "Côté Mer"},
                        {"text": "Côté Terre", "value": "Côté Terre"},
                        {"text": "Côté Flamme", "value": "Côté Flamme"},
                        {"text": "Finir en douceur", "value": "Finir en douceur"}
                    ]
                }
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "image",
            "type": "uuid",
            "meta": {
                "interface": "file-image",
                "special": ["file"]
            },
            "schema": {
                "is_nullable": True
            }
        }
    ]
    
    return create_collection(headers, "dishes", fields)

def clean_categories(headers):
    """Nettoyer les catégories existantes"""
    print("Nettoyage des catégories existantes...")
    
    # Récupérer toutes les catégories
    url = f"{DIRECTUS_URL}/items/menu_categories"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        categories = response.json()['data']
        
        # Supprimer toutes les catégories
        for category in categories:
            delete_url = f"{DIRECTUS_URL}/items/menu_categories/{category['id']}"
            delete_response = requests.delete(delete_url, headers=headers)
            
            if delete_response.status_code == 204:
                print(f"Catégorie {category['name']} supprimée avec succès")
            else:
                print(f"Erreur lors de la suppression de la catégorie {category['name']}: {delete_response.status_code}")
                print(delete_response.text)
        
        return True
    else:
        print(f"Erreur lors de la récupération des catégories: {response.status_code}")
        print(response.text)
        return False

def main():
    """Fonction principale"""
    print("Ajout des données du menu dans Directus pour Brasserie Chez Ju")
    print("===========================================================")
    
    # Se connecter à Directus
    access_token = login()
    if not access_token:
        return
    
    headers = get_headers(access_token)
    
    # Créer les collections
    if not create_menu_categories_collection(headers):
        print("Erreur lors de la création de la collection menu_categories")
        return
    
    if not create_dishes_collection(headers):
        print("Erreur lors de la création de la collection dishes")
        return
    
    # Nettoyer les catégories existantes
    clean_categories(headers)
    
    # Ajouter les catégories de menu
    for category in MENU_CATEGORIES:
        add_menu_category(headers, category)
    
    # Ajouter les plats avec leurs images
    for dish in DISHES:
        image_id = None
        
        # Vérifier si le plat a une image spécifiée
        if dish["image"] and dish["image"].strip():
            # Uploader l'image
            image_path = os.path.join(IMAGES_DIR, dish["image"])
            if os.path.exists(image_path) and os.path.isfile(image_path):
                image_id = upload_image(headers, image_path)
            else:
                print(f"Image {dish['image']} non trouvée dans {IMAGES_DIR} ou n'est pas un fichier")
        
        # Ajouter le plat avec ou sans image
        add_dish(headers, dish, image_id)
    
    print("\nAjout des données terminé!")

if __name__ == "__main__":
    main() 