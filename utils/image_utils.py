import numpy as np

class ImagePGM:
    """
    Classe pour représenter et manipuler une image en niveaux de gris (PGM P5/P2).

    Une image est une matrice de pixels, caractérisée par ses dimensions
    et la valeur d'intensité maximale.
    """
    
    def __init__(self, height=0, width=0, max_val=255):
        """
        Initialise l'objet ImagePGM.
        Si la hauteur et la largeur sont fournies, initialise une matrice de zéros.
        """
        self.width = width
        self.height = height
        self.max_val = max_val
        
        if height > 0 and width > 0:
            # np.uint8 est crucial pour le format PGM 8 bits (0-255)
            self.data = np.zeros((height, width), dtype=np.uint8)
        else:
            self.data = None

    def get_data(self):
        """ Retourne la matrice de pixels (NumPy array). """
        return self.data
    
    def __str__(self):
        """ Représentation textuelle de l'objet. """
        if self.data is not None:
            return f"ImagePGM ({self.height}x{self.width}, Max Val: {self.max_val}, Type: {self.data.dtype})"
        return "ImagePGM (Vide)"

# Test simple (juste pour vérification)
if __name__ == '__main__':
    print("--- Tests de la classe ImagePGM ---")
    
    # Cas Normal (Image 100x150)
    print("\nInitialisation 100x150, 8 bits (par défaut)")
    img_normal = ImagePGM(height=100, width=150)
    
    print(f"  Description: {img_normal}")
    
    # Assertions cruciales pour un PGM 8 bits 
    # oui il y a trop d'alertes mais c'est pour s'assurer que tout est correct 
    assert img_normal.height == 100, "Erreur Hauteur"
    assert img_normal.width == 150, "Erreur Largeur"
    assert img_normal.max_val == 255, "Erreur Valeur Max"
    assert img_normal.data.shape == (100, 150), "Erreur de forme de matrice"
    assert img_normal.data.dtype == np.uint8, "Erreur de type de données (doit être uint8)"
    print("  Résultat: SUCCÈS. Propriétés et type de données corrects.")