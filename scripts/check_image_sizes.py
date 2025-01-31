#!/usr/bin/env python3
import os
from pathlib import Path

def check_image_sizes(max_size_mb=2):
    """
    Vérifie la taille des images dans le projet.
    Retourne False si une image dépasse la taille maximale.
    """
    image_dirs = [
        "public/images/instagram",
        "public/images/staff",
        # Ajoutez d'autres dossiers d'images si nécessaire
    ]
    
    large_images = []
    max_size_bytes = max_size_mb * 1024 * 1024  # Conversion en bytes
    
    for dir_path in image_dirs:
        if not os.path.exists(dir_path):
            continue
            
        for file_path in Path(dir_path).rglob('*'):
            if file_path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.gif'}:
                size = os.path.getsize(file_path)
                if size > max_size_bytes:
                    large_images.append({
                        'path': file_path,
                        'size': size / (1024 * 1024)  # Conversion en MB pour l'affichage
                    })
    
    if large_images:
        print("\n❌ Images trop volumineuses détectées!")
        print(f"La taille maximale autorisée est de {max_size_mb}MB")
        print("\nImages concernées:")
        for img in large_images:
            print(f"- {img['path']}: {img['size']:.2f}MB")
        print("\nSuggestion: Utilisez le script d'optimisation avant de commit:")
        print("python3 scripts/optimize_images.py")
        return False
    
    return True

if __name__ == "__main__":
    # Exit avec un code d'erreur si des images sont trop grandes
    exit(0 if check_image_sizes() else 1) 