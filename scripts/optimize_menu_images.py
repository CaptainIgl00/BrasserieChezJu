from PIL import Image
import os
from pathlib import Path

def optimize_image(input_path, target_size_mb=1, quality_start=95):
    """
    Optimise une image pour atteindre une taille cible tout en maintenant une bonne qualité visuelle.
    """
    # Vérifier la taille actuelle
    current_size_mb = os.path.getsize(input_path) / (1024 * 1024)
    print(f"\nOptimisation de {input_path}")
    print(f"Taille actuelle: {current_size_mb:.2f}MB")

    # Ouvrir l'image
    img = Image.open(input_path)
    
    # Convertir en RGB si nécessaire
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # Redimensionner si l'image est très grande
    max_dimension = 1600  # Taille maximale réduite pour la plus grande dimension
    original_size = img.size
    if max(img.size) > max_dimension:
        ratio = max_dimension / max(img.size)
        new_size = tuple(int(dim * ratio) for dim in img.size)
        img = img.resize(new_size, Image.Resampling.LANCZOS)
        print(f"Image redimensionnée de {original_size} à {new_size}")
    
    # Sauvegarder avec compression progressive
    quality = quality_start
    temp_path = str(input_path) + '.temp'
    best_quality = quality
    best_size = float('inf')
    
    while quality >= 60:  # On garde une qualité minimum de 60%
        img.save(temp_path, 'JPEG', quality=quality, optimize=True, progressive=True)
        new_size_mb = os.path.getsize(temp_path) / (1024 * 1024)
        
        if new_size_mb <= target_size_mb and quality > best_quality:
            best_quality = quality
            best_size = new_size_mb
            os.replace(temp_path, input_path)
        elif new_size_mb < best_size:
            best_quality = quality
            best_size = new_size_mb
            os.replace(temp_path, input_path)
            
        if new_size_mb <= target_size_mb:
            break
            
        quality -= 5
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    if os.path.exists(temp_path):
        os.remove(temp_path)
        
    print(f"Image optimisée avec succès!")
    print(f"Nouvelle taille: {best_size:.2f}MB")
    print(f"Qualité finale: {best_quality}%")
    print(f"Réduction: {((current_size_mb - best_size) / current_size_mb * 100):.1f}%")

def process_menu_images():
    """
    Traite toutes les images du dossier menu
    """
    menu_dir = Path("public/images/menu")
    
    # Extensions d'images supportées
    image_extensions = {'.jpg', '.jpeg', '.png'}
    
    print("Optimisation de toutes les images du menu...")
    
    for file_path in menu_dir.glob('*'):
        if file_path.suffix.lower() in image_extensions and not file_path.name.endswith('.temp'):
            optimize_image(str(file_path))

if __name__ == "__main__":
    print("Début de l'optimisation des images...")
    process_menu_images()
    print("\nOptimisation terminée!") 