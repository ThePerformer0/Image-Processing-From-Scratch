from core.image_loader import ImageLoader
from core.processor import ImageProcessor

IMAGE_PATH = "images/test.jpg"
OUTPUT_PATH = "images/output_test_inverse.png"

def run_test():
    print("--- Démarrage du Test VisionCore Engine ---")
    
    # 1. Test Chargement
    try:
        print(f"1. Chargement de {IMAGE_PATH}...")
        matrix = ImageLoader.load(IMAGE_PATH)
        print(f"   Succès ! Matrice de type {matrix.dtype} chargée.")
    except Exception as e:
        print(f"   Erreur fatale : {e}")
        return

    # 2. Test Statistiques
    print("2. Calcul des statistiques...")
    stats = ImageProcessor.get_stats(matrix)
    for key, val in stats.items():
        print(f"   - {key}: {val}")

    # 3. Test Traitement (Inversion)
    print("3. Application du filtre Négatif...")
    inverted = ImageProcessor.inverse(matrix)

    # 4. Test Sauvegarde
    print(f"4. Sauvegarde du résultat vers {OUTPUT_PATH}...")
    ImageLoader.save(inverted, OUTPUT_PATH)

    print("--- Test Terminé avec succès ---")

if __name__ == "__main__":
        run_test()