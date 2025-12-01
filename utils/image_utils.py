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
    
    def calculate_histogram(self):
        """
        Calcule l'histogramme de l'image.

        Returns:
            np.ndarray: Un tableau 1D de 256 éléments (pour 8 bits) où 
                        l'indice k contient le nombre de pixels ayant l'intensité k.
        """
        if self.data is None:
            raise ValueError("L'image est vide, impossible de calculer l'histogramme.")

        # NumPy's histogram est très rapide.
        # bins=256 pour les 256 niveaux de gris [0, 255]
        # range=(0, 256) assure que toutes les valeurs sont couvertes
        hist, _ = np.histogram(self.data, bins=256, range=(0, 256))
        
        return hist

    def calculate_metrics(self):
        """
        Calcule les métriques de base (Luminance et Contraste simple).

        Returns:
            dict: Un dictionnaire contenant les métriques calculées.
        """
        if self.data is None:
            raise ValueError("L'image est vide, impossible de calculer les métriques.")
            
        # Utiliser les fonctions NumPy optimisées
        
        # Min et Max pour le Contraste
        min_val = np.min(self.data)
        max_val = np.max(self.data)
        
        # Luminance (Moyenne)
        luminance = np.mean(self.data)
        
        # Contraste (Dynamique simple)
        contrast = max_val - min_val
        
        return {
            'min_val': int(min_val),
            'max_val': int(max_val),
            'luminance': float(luminance),
            'contrast_dynamique': int(contrast)
        }
    
    def __str__(self):
        """ Représentation textuelle de l'objet. """
        if self.data is not None:
            return f"ImagePGM ({self.height}x{self.width}, Max Val: {self.max_val}, Type: {self.data.dtype})"
        return "ImagePGM (Vide)"


def read_pgm(filepath):
    """
    Lit un fichier PGM (formats P2 ou P5) et retourne un objet ImagePGM.
    Gère les lignes de commentaires commençant par '#'.

    Args:
        filepath (str): Chemin vers le fichier PGM.

    Returns:
        ImagePGM: L'objet image rempli avec les données du fichier.
    """
    
    # Ouvrir le fichier en mode lecture binaire ('rb')
    with open(filepath, 'rb') as f:
        # Fonction utilitaire pour lire la prochaine ligne non-vide/non-commentaire
        def read_header_line(f):
            while True:
                line = f.readline().decode('latin-1').strip()
                if line and not line.startswith('#'):
                    return line
        
        # 1. Lire le Magic Number (P2 ou P5)
        magic_number = read_header_line(f)
        if magic_number not in ['P2', 'P5']:
            raise ValueError(f"Format PGM non supporté ou invalide: {magic_number}")

        # 2. Lire les Dimensions (Largeur N, Hauteur M)
        dimensions_line = read_header_line(f).split()
        width = int(dimensions_line[0])
        height = int(dimensions_line[1])
        
        # 3. Lire la Valeur Maximale
        max_val_line = read_header_line(f)
        max_val = int(max_val_line)

        # Vérification standard 8 bits
        if max_val > 255:
            # Pour simplifier les choses, nous nous concentrons sur le 8 bits.
            print(f"Attention : Valeur max ({max_val}) > 255. Traité comme 8 bits (uint8) par défaut.")

        # Créer l'objet ImagePGM pour stocker les données
        img = ImagePGM(height=height, width=width, max_val=max_val)

        # 4. Lire les données de pixels
        
        if magic_number == 'P5':
            # P5 (Binaire) : Lire directement le nombre total d'octets
            # Utilisation de np.fromfile pour une lecture rapide et directe dans le dtype cible
            img.data = np.fromfile(f, dtype=np.uint8, count=width * height).reshape((height, width))
        
        elif magic_number == 'P2':
            # P2 (ASCII) : Lire toutes les valeurs séparées par des espaces
            data_ascii = f.read().decode('latin-1').split()
            img.data = np.array(data_ascii, dtype=np.uint8).reshape((height, width))
            
    return img


def write_pgm(image, filepath):
    """
    Sauvegarde un objet ImagePGM dans un fichier PGM au format binaire P5.

    Args:
        image (ImagePGM): L'objet image à sauvegarder.
        filepath (str): Chemin du fichier de sortie.
    """
    if image.data is None:
        raise ValueError("L'objet ImagePGM ne contient pas de données à sauvegarder.")
        
    # Ouvrir le fichier en mode écriture binaire ('wb')
    with open(filepath, 'wb') as f:
        # Écriture de l'en-tête PGM (format P5)
        # Le b'' est important pour écrire des bytes
        
        # 1. Magic Number
        f.write(b'P5\n')
        
        # 2. Dimensions (Largeur Hauteur)
        header_dims = f"{image.width} {image.height}\n"
        f.write(header_dims.encode('latin-1'))
        
        # 3. Valeur Maximale
        header_max = f"{image.max_val}\n"
        f.write(header_max.encode('latin-1'))
        
        # 4. Écriture des données brutes
        # Utilisation de .tobytes() pour écrire la matrice NumPy directement
        f.write(image.data.tobytes())


def calculate_histogram(image):
    """
    Fonction utilitaire pour calculer l'histogramme d'une image.
    (Appelle la méthode de l'objet ImagePGM)
    """
    return image.calculate_histogram()


def calculate_metrics(image):
    """
    Fonction utilitaire pour calculer les métriques d'une image.
    (Appelle la méthode de l'objet ImagePGM)
    """
    return image.calculate_metrics()