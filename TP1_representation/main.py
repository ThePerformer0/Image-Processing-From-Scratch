import os
import sys
import numpy as np

# Importer la classe et les fonctions utilitaires
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

# On importe les fonctions et la classe directement depuis le module ajouté
from image_utils import ImagePGM, read_pgm, write_pgm, calculate_histogram, calculate_metrics

def main():
    """
    Programme principal du TP1.
    1. Lit une image PGM.
    2. Sauvegarde une copie pour validation.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <chemin_vers_image.pgm>")
        sys.exit(1)
        
    input_filepath = sys.argv[1]
    output_filepath = os.path.join(os.path.dirname(input_filepath), 
                                   "copy_" + os.path.basename(input_filepath))
    
    # --- A. Lecture PGM ---
    print(f"Chargement de l'image : {input_filepath}")
    try:
        input_image = read_pgm(input_filepath)
        print(input_image)
        
        # Vérification rapide de la lecture
        if input_image.data is not None:
            print(f"Lecture réussie. Min/Max des pixels : ({np.min(input_image.data)}, {np.max(input_image.data)})")
        
        # --- B. Écriture PGM ---
        print(f"\nSauvegarde de la copie vers : {output_filepath}")
        write_pgm(input_image, output_filepath)
        print("Sauvegarde réussie.")
        
        # --- C. Double Validation (Lecture/Écriture) ---
        # Lire la copie et vérifier que les matrices sont identiques
        copied_image = read_pgm(output_filepath)
        
        if np.array_equal(input_image.data, copied_image.data):
            print("\nValidation croisée : La matrice lue et la matrice réécrite sont IDENTIQUES. (SUCCÈS)")
        else:
            print("\nValidation croisée : ATTENTION ! La matrice lue et la matrice réécrite sont DIFFÉRENTES. (ÉCHEC)")

        # --- D. Calcul et Affichage des Métriques (Tâche 3 & 4) ---
        
        # 1. Calcul de l'Histogramme (pour vérification interne)
        histogram = input_image.calculate_histogram()
        print(f"\n[Analyse de l'Histogramme]")
        print(f"  Somme des pixels (vérification) : {np.sum(histogram)}")
        print(f"  Taille totale de l'image : {input_image.height * input_image.width}")
        
        # 2. Calcul des Métriques
        metrics = input_image.calculate_metrics()
        print("\n[Métriques Statistiques]")
        print(f"  Luminance (Moyenne) : {metrics['luminance']:.2f}")
        print(f"  Niveau de Gris Min : {metrics['min_val']}")
        print(f"  Niveau de Gris Max : {metrics['max_val']}")
        print(f"  Contraste (Dynamique) : {metrics['contrast_dynamique']}")

    except Exception as e:
        print(f"\nERREUR lors du traitement du fichier : {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()