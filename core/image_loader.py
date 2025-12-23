import numpy as np
from PIL import Image
import os

class ImageLoader:
    """
    Gère le chargement et la sauvegarde des images.
    Fait l'interface entre le système de fichiers et les matrices NumPy.
    """

    @staticmethod
    def load(filepath: str) -> np.ndarray:
        """
        Charge une image depuis un chemin et la convertit en matrice Niveaux de Gris.
        
        Args:
            filepath (str): Chemin complet vers l'image.
            
        Returns:
            np.ndarray: Matrice 2D (uint8) représentant l'image.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Fichier introuvable : {filepath}")

        try:
            # 1. Ouverture avec Pillow (gère tous les formats : jpg, png, etc.)
            with Image.open(filepath) as img:
                # 2. Conversion explicite en Niveaux de Gris ('L' = Luminance)
                img_gray = img.convert('L')
                
                # 3. Transformation en matrice NumPy
                # dtype=uint8 est CRUCIAL pour économiser la mémoire (0-255)
                matrix = np.array(img_gray, dtype=np.uint8)
                
                return matrix
        except Exception as e:
            raise ValueError(f"Erreur lors du chargement de l'image : {e}")

    @staticmethod
    def save(matrix: np.ndarray, filepath: str):
        """
        Sauvegarde une matrice NumPy en fichier image.
        
        Args:
            matrix (np.ndarray): La matrice de pixels.
            filepath (str): Chemin de destination.
        """
        try:
            # 1. Conversion de NumPy vers Objet Image Pillow
            img = Image.fromarray(matrix)
            
            # 2. Sauvegarde (le format est déduit de l'extension du fichier)
            img.save(filepath)
            print(f"Image sauvegardée : {filepath}")
        except Exception as e:
            print(f"Erreur sauvegarde : {e}")