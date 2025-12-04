import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from image_utils import ImagePGM

def apply_negative_inversion(input_image: ImagePGM) -> ImagePGM:
    """
    Applique la transformation d'inversion négative à l'image.

    Args:
        input_image: L'objet ImagePGM d'entrée.

    Returns:
        ImagePGM: Une nouvelle image contenant le résultat de l'inversion.
    """
    if input_image.data is None:
        raise ValueError("L'image d'entrée est vide.")

    # 1. Détermination de la valeur maximale L_max (généralement 255)
    L_max = input_image.max_val
    
    # 2. Application de la formule en utilisant les opérations vectorielles NumPy.
    output_data = L_max - input_image.data
    
    # 3. Création et retour de la nouvelle image
    output_image = ImagePGM(input_image.height, input_image.width, L_max)
    output_image.data = output_data.astype(np.uint8)
    
    return output_image

def adjust_brightness_contrast_linear(input_image: ImagePGM, alpha: float, beta: int) -> ImagePGM:
    """
    Applique une transformation linéaire pour ajuster le contraste (alpha) 
    et la luminosité (beta).

    I_out = alpha * I_in + beta

    Args:
        input_image: L'objet ImagePGM d'entrée.
        alpha (float): Facteur de contraste (pente).
        beta (int): Décalage de luminosité (ordonnée à l'origine).

    Returns:
        ImagePGM: Nouvelle image traitée.
    """
    if input_image.data is None:
        raise ValueError("L'image d'entrée est vide.")

    # Convertir temporairement en float64 pour éviter les problèmes d'overflow/underflow
    # lors de l'opération arithmétique (alpha * I_in + beta)
    temp_data = input_image.data.astype(np.float64)
    
    # Application de la transformation linéaire
    output_data_float = alpha * temp_data + beta
    
    # 1. Rognage (Clamping) : S'assurer que les valeurs restent dans [0, L_max]
    # np.clip est la fonction NumPy la plus efficace pour cela.
    L_max = input_image.max_val
    output_data_clipped = np.clip(output_data_float, 0, L_max)
    
    # 2. Conversion finale en uint8
    output_data = output_data_clipped.astype(np.uint8)
    
    # Création et retour de la nouvelle image
    output_image = ImagePGM(input_image.height, input_image.width, L_max)
    output_image.data = output_data
    
    return output_image

# Fichier : utils/image_processing.py (Suite)

def apply_gamma_correction(input_image: ImagePGM, gamma: float) -> ImagePGM:
    """
    Applique la correction Gamma (non-linéaire) à l'image.

    I_out = L_max * (I_in / L_max)^gamma

    Args:
        input_image: L'objet ImagePGM d'entrée.
        gamma (float): Facteur gamma (si < 1.0 : éclaircit, si > 1.0 : assombrit).

    Returns:
        ImagePGM: Nouvelle image traitée.
    """
    if input_image.data is None:
        raise ValueError("L'image d'entrée est vide.")

    L_max = input_image.max_val
    temp_data = input_image.data.astype(np.float64)

    # 1. Normalisation [0, 1] : I_in / L_max
    normalized_data = temp_data / L_max

    # 2. Application de la loi de puissance (Gamma)
    gamma_corrected_data = np.power(normalized_data, gamma)

    # 3. Dénormalisation [0, L_max] et Rognage (Clamping)
    output_data_float = gamma_corrected_data * L_max
    
    # Le rognage est ici principalement pour la sécurité, car la transformation
    # sur une plage [0, 1] garde les valeurs dans cette plage.
    output_data_clipped = np.clip(output_data_float, 0, L_max)
    
    # 4. Conversion finale en uint8
    output_data = output_data_clipped.astype(np.uint8)

    # Création et retour de la nouvelle image
    output_image = ImagePGM(input_image.height, input_image.width, L_max)
    output_image.data = output_data

    return output_image