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