import os
import sys
import numpy as np

# Configuration du chemin d'accès
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from image_utils import read_pgm, write_pgm, calculate_metrics
from image_processing import apply_negative_inversion, adjust_brightness_contrast_linear, apply_gamma_correction

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

        # Exemple 1 : Augmenter la Luminosité (alpha=1.0, beta=50)
        alpha_b = 1.0
        beta_b = 50
        print(f"\n[Tâche 2a] Augmentation de Luminosité (alpha={alpha_b}, beta={beta_b})...")
        brightened_image = adjust_brightness_contrast_linear(input_image, alpha_b, beta_b)
        
        # Vérification mathématique : la luminance devrait augmenter d'environ beta.
        metrics_b = brightened_image.calculate_metrics()
        print(f"  Luminance originale: {input_image.calculate_metrics()['luminance']:.2f}")
        print(f"  Luminance après luminosité: {metrics_b['luminance']:.2f}")
        
        output_filepath_b = os.path.join(os.path.dirname(input_filepath), "brightened_" + os.path.basename(input_filepath))
        write_pgm(brightened_image, output_filepath_b)
        print(f"  Sauvegarde réussie : {output_filepath_b}")

        # Exemple 2 : Augmenter le Contraste (alpha=1.5, beta=0)
        alpha_c = 1.5
        beta_c = 0
        print(f"\n[Tâche 2b] Augmentation de Contraste (alpha={alpha_c}, beta={beta_c})...")
        contrasted_image = adjust_brightness_contrast_linear(input_image, alpha_c, beta_c)
        
        # Vérification mathématique : la dynamique devrait s'étendre
        metrics_c = contrasted_image.calculate_metrics()
        print(f"  Contraste dynamique original: {input_image.calculate_metrics()['contrast_dynamique']}")
        print(f"  Contraste dynamique après contraste: {metrics_c['contrast_dynamique']}")
        
        output_filepath_c = os.path.join(os.path.dirname(input_filepath), "contrasted_" + os.path.basename(input_filepath))
        write_pgm(contrasted_image, output_filepath_c)
        print(f"  Sauvegarde réussie : {output_filepath_c}")

        # Exemple 3 : Gamma < 1.0 (Éclaircissement des tons moyens)
        gamma_val = 0.5
        print(f"\n[Tâche 3] Correction Gamma (gamma={gamma_val})...")
        gamma_image = apply_gamma_correction(input_image, gamma_val)
        
        metrics_g = gamma_image.calculate_metrics()
        print(f"  Luminance originale: {input_image.calculate_metrics()['luminance']:.2f}")
        print(f"  Luminance après Gamma ({gamma_val}): {metrics_g['luminance']:.2f} (Augmentation attendue)")
        
        # Sauvegarde avec gamma dans le nom de fichier
        output_filepath_g = os.path.join(os.path.dirname(input_filepath), 
                                         "gamma_" + str(gamma_val).replace('.', 'p') + "_" + os.path.basename(input_filepath))
        write_pgm(gamma_image, output_filepath_g)
        print(f"  Sauvegarde réussie : {output_filepath_g}")

    except Exception as e:
        print(f"\nERREUR lors du traitement du fichier : {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()