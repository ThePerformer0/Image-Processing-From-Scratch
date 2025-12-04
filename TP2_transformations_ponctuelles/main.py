import os
import sys
import numpy as np

# Configuration du chemin d'accès
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from image_utils import read_pgm, write_pgm
from image_processing import apply_negative_inversion

def main():
    """
    Programme principal du TP2 : Test de l'inversion négative.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <chemin_vers_image.pgm>")
        sys.exit(1)
        
    input_filepath = sys.argv[1]
    
    try:
        # --- 1. Lecture ---
        input_image = read_pgm(input_filepath)
        print(f"Image lue: {input_image}")
        
        # --- 2. Transformation : Inversion Négative ---
        print("\n[Tâche 1] Application de l'inversion négative...")
        inverted_image = apply_negative_inversion(input_image)
        
        # --- 3. Validation ---
        print(f"Image inversée: {inverted_image}")
        
        # Test mathématique simple : 0 doit devenir 255, 255 doit devenir 0.
        original_min = np.min(input_image.data)
        inverted_max = np.max(inverted_image.data)
        print(f"  Min original ({original_min}) -> Max inversé ({inverted_max})")
        
        # --- 4. Sauvegarde ---
        output_filepath = os.path.join(os.path.dirname(input_filepath), 
                                       "inverted_" + os.path.basename(input_filepath))
        write_pgm(inverted_image, output_filepath)
        print(f"\nSauvegarde réussie : {output_filepath}")

    except Exception as e:
        print(f"\nERREUR lors du traitement du fichier : {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()