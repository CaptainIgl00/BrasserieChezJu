from PIL import Image
import os
from pathlib import Path

def optimize_image(input_path, output_path, max_size_mb=0.5, quality_start=95):
    """
    Optimise une image en la redimensionnant si nécessaire et en ajustant sa qualité
    pour atteindre une taille cible tout en maintenant une bonne qualité visuelle.
    
    Args:
        input_path: Chemin de l'image source
        output_path: Chemin où sauvegarder l'image optimisée
        max_size_mb: Taille maximale souhaitée en MB (défaut: 0.5MB)
        quality_start: Qualité de compression initiale (défaut: 95%)
    """
    # Ouvrir l'image
    img = Image.open(input_path)
    
    # Convertir en RGB si nécessaire (pour les PNG)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # Redimensionner si l'image est très grande
    max_dimension = 2000  # Taille maximale pour la plus grande dimension
    if max(img.size) > max_dimension:
        ratio = max_dimension / max(img.size)
        new_size = tuple(int(dim * ratio) for dim in img.size)
        img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    # Créer le dossier de sortie si nécessaire
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Sauvegarder avec compression progressive
    quality = quality_start
    while quality > 50:  # On ne descend pas en dessous de 50% de qualité
        img.save(output_path, 'JPEG', quality=quality, optimize=True, progressive=True)
        file_size = os.path.getsize(output_path) / (1024 * 1024)  # Taille en MB
        
        if file_size <= max_size_mb:
            break
            
        quality -= 5  # Réduire la qualité progressivement
    
    return file_size, quality

def process_directory(input_dir, output_dir, max_size_mb=0.5):
    """
    Traite tous les fichiers images dans un dossier.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Extensions d'images supportées
    image_extensions = {'.jpg', '.jpeg', '.png'}
    
    for file_path in input_path.rglob('*'):
        if file_path.suffix.lower() in image_extensions:
            # Créer le même chemin relatif dans le dossier de sortie
            relative_path = file_path.relative_to(input_path)
            output_file = output_path / relative_path
            
            # Assurer que le dossier de sortie existe
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Optimiser l'image
            original_size = os.path.getsize(file_path) / (1024 * 1024)
            new_size, final_quality = optimize_image(
                str(file_path),
                str(output_file.with_suffix('.jpg')),  # Toujours sauvegarder en JPG
                max_size_mb
            )
            
            print(f"Traitement de {relative_path}:")
            print(f"  Taille originale: {original_size:.2f}MB")
            print(f"  Nouvelle taille: {new_size:.2f}MB")
            print(f"  Qualité finale: {final_quality}%")
            print(f"  Réduction: {((original_size - new_size) / original_size * 100):.1f}%")
            print("---")

if __name__ == "__main__":
    # Dossiers à traiter
    folders_to_process = {
        "public/images/instagram": "public/images/instagram_optimized"
    }
    
    # Taille maximale souhaitée par image en MB
    target_size_mb = 0.5
    
    print(f"Début de l'optimisation des images...")
    print(f"Taille cible par image: {target_size_mb}MB")
    print("---")
    
    for input_dir, output_dir in folders_to_process.items():
        print(f"\nTraitement du dossier: {input_dir}")
        print(f"Destination: {output_dir}")
        print("---")
        process_directory(input_dir, output_dir, target_size_mb)
    
    print("\nOptimisation terminée!") 