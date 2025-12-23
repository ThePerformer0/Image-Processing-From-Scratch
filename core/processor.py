import numpy as np

class ImageProcessor:
    """
    Contient les algorithmes de traitement d'image 'From Scratch'.
    Utilise NumPy pour la performance vectorielle.
    """

    @staticmethod
    def get_stats(image: np.ndarray) -> dict:
        """
        Calcule les statistiques de base de l'image.
        """
        return {
            "dimensions": image.shape, # (Hauteur, Largeur)
            "pixels_total": image.size,
            "min_val": np.min(image),
            "max_val": np.max(image),
            "moyenne_luminance": float(np.mean(image)),
            "std_dev": float(np.std(image)) # Écart-type (contraste RMS)
        }

    @staticmethod
    def inverse(image: np.ndarray) -> np.ndarray:
        """
        Transformation ponctuelle : Négatif de l'image.
        Formule : s = L_max - r
        """
        # NumPy gère l'opération élément par élément automatiquement (Vectorisation)
        return 255 - image
    
    @staticmethod
    def get_histogram(image: np.ndarray) -> np.ndarray:
        """Calcule l'histogramme (fréquence de chaque niveau de gris)."""
        # counts sera un tableau de 256 éléments (pour 0-255)
        counts, _ = np.histogram(image, bins=256, range=(0, 256))
        return counts
    
    @staticmethod
    def apply_gamma(image: np.ndarray, gamma: float) -> np.ndarray:
        # Normalisation, Puissance, Dénormalisation
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        return np.take(table, image)
    
    @staticmethod
    def stretch_contrast(image: np.ndarray) -> np.ndarray:
        """Étirement linéaire de la dynamique (Contrast Stretching)."""
        i_min = np.min(image)
        i_max = np.max(image)
        
        if i_max == i_min: return image # Image unie
        
        # Formule : s = 255 * (r - min) / (max - min)
        stretched = (255 * (image - i_min) / (i_max - i_min)).astype(np.uint8)
        return stretched

    @staticmethod
    def equalize_histogram(image: np.ndarray) -> np.ndarray:
        """Égalisation d'histogramme basée sur la fonction de répartition (CDF)."""
        # 1. Calcul de l'histogramme
        hist, _ = np.histogram(image.flatten(), 256, [0, 256])
        
        # 2. Calcul de la fonction de répartition cumulative (CDF)
        cdf = hist.cumsum()
        
        # 3. Normalisation de la CDF pour qu'elle tienne entre 0 et 255
        # On ignore les valeurs à 0 pour éviter les artefacts
        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        
        # 4. Application de la LUT (Look-Up Table) via la CDF
        return cdf[image]
    
    @staticmethod
    def apply_filter(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Applique un filtre par convolution 2D générique.
        Gère les bords par 'padding' (ajout de bordures noires).
        """
        # 1. Dimensions du noyau
        k_h, k_w = kernel.shape
        pad_h, pad_w = k_h // 2, k_w // 2
        
        # 2. Ajout d'une bordure de zéros (Zero-padding) pour garder la même taille
        padded_img = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
        
        # 3. Préparation de l'image de sortie
        output = np.zeros_like(image, dtype=np.float32)
        
        # 4. Convolution (Somme des produits pondérés)
        # Pour chaque position du noyau
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                # Extraction de la zone d'intérêt (fenêtre de voisinage)
                region = padded_img[i:i+k_h, j:j+k_w]
                # Multiplication élément par élément et somme
                output[i, j] = np.sum(region * kernel)
        
        # 5. Normalisation et conversion en uint8
        # On s'assure que les valeurs restent entre 0 et 255
        return np.clip(output, 0, 255).astype(np.uint8)
    
    @staticmethod
    def blur_gaussian(image: np.ndarray) -> np.ndarray:
        """Filtre de lissage (Flou) - Noyau Gaussien 3x3."""
        kernel = np.array([[1, 2, 1],
                           [2, 4, 2],
                           [1, 2, 1]], dtype=np.float32) / 16.0
        return ImageProcessor.apply_filter(image, kernel)

    @staticmethod
    def detect_edges_sobel(image: np.ndarray) -> np.ndarray:
        """Détection de contours (Sobel)."""
        # Sobel Horizontal
        kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
        # Sobel Vertical
        ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
        
        gx = ImageProcessor.apply_filter(image, kx)
        gy = ImageProcessor.apply_filter(image, ky)
        
        # Norme du gradient : sqrt(gx² + gy²)
        # Simplifié ici par la somme des valeurs absolues pour la rapidité
        return np.clip(np.abs(gx) + np.abs(gy), 0, 255).astype(np.uint8)
    
    @staticmethod
    def filter_median(image: np.ndarray, size: int = 3) -> np.ndarray:
        """Filtre non-linéaire pour supprimer le bruit impulsionnel."""
        pad = size // 2
        padded = np.pad(image, pad, mode='edge')
        output = np.zeros_like(image)
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                # Extraction du voisinage et tri pour trouver la médiane
                window = padded[i:i+size, j:j+size]
                output[i, j] = np.median(window)
        return output

    @staticmethod
    def threshold_otsu(image: np.ndarray) -> np.ndarray:
        """Segmentation automatique par la méthode d'Otsu."""
        hist = ImageProcessor.get_histogram(image)
        total = image.size
        
        current_max = 0
        threshold = 0
        sum_total = np.dot(np.arange(256), hist)
        
        sum_back, weight_back = 0, 0
        
        for t in range(256):
            weight_back += hist[t]
            if weight_back == 0: continue
            
            weight_fore = total - weight_back
            if weight_fore == 0: break
            
            sum_back += t * hist[t]
            mean_back = sum_back / weight_back
            mean_fore = (sum_total - sum_back) / weight_fore
            
            # Variance inter-classe (Formule d'Otsu)
            var_between = weight_back * weight_fore * (mean_back - mean_fore)**2
            
            if var_between > current_max:
                current_max = var_between
                threshold = t
                
        # Application du seuil
        return (image > threshold).astype(np.uint8) * 255

    @staticmethod
    def morpho_operation(image: np.ndarray, op_type: str = "erosion") -> np.ndarray:
        """Opérations morphologiques de base sur image binaire."""
        size = 3
        pad = size // 2
        padded = np.pad(image, pad, mode='constant', constant_values=0)
        output = np.zeros_like(image)
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                window = padded[i:i+size, j:j+size]
                if op_type == "erosion":
                    output[i, j] = np.min(window)
                else: # dilatation
                    output[i, j] = np.max(window)
        return output