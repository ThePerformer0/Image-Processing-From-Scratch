# 📁 TP 1 : Représentation, Lecture et Analyse Basique de l'Image

## 🎯 Objectifs

* Définir la structure de données pour une image.
* Implémenter la lecture/écriture du format PGM (crucial pour le traitement d'image sans compression).
* Calculer les métriques fondamentales : Histogramme, Luminance et Contraste.

## 1. Structure de l'Image

La classe `ImagePGM` est définie dans `../utils/image_utils.py`. Elle utilise un `numpy.ndarray` de type `uint8` pour stocker efficacement les niveaux de gris.

## 2. Lecture et Écriture PGM (À faire)

Le fichier `main.py` de ce TP contiendra les fonctions `read_pgm` et `write_pgm`.

## 3. Exécution

```bash
# Assurez-vous d'avoir une image .pgm dans le dossier 'images/'
python main.py chemin/vers/votre/image.pgm
```

## ❓ Questions de Compréhension (Réponses)

### 1\. Quelle est la différence fondamentale entre la **résolution spatiale** et la **résolution tonale** ?

  * **Résolution Spatiale :** Définit le **nombre de pixels** (la taille de la grille $M \times N$). Elle impacte la finesse des détails.
  * **Résolution Tonale :** Définit le **nombre de niveaux d'intensité** (la profondeur de bits, ex: 256 niveaux pour 8 bits). Elle impacte la précision des nuances de couleur ou de gris.

### 2\. Pourquoi le format **JPEG est généralement déconseillé pour le traitement d'images** après une opération, et pourquoi PGM/PPM sont-ils souvent préférés ?

  * **JPEG** utilise une **compression avec perte** (lossy compression) basée sur la Transformée en Cosinus Discrète (DCT). Chaque fois qu'une image est modifiée et réenregistrée en JPEG, elle subit une nouvelle dégradation (artefacts, perte d'information).
  * **PGM/PPM** (Portable Graymap/PixMap) utilisent une **représentation brute et sans perte** (lossless) des données. Le fichier est une représentation exacte de la matrice de pixels, garantissant qu'aucune information n'est perdue lors de la lecture ou de l'écriture répétée, ce qui est essentiel pour un traitement numérique précis.

### 3\. Si une image 8 bits (0 à 255) a une luminance de 128 et une dynamique (valeur\_min, valeur\_max) de [50, 200], comment décririez-vous le contraste de cette image ?

  * **Luminance (Moyenne) :** 128 est exactement le milieu de l'échelle [0, 255]. L'image est donc parfaitement **neutre** en termes de luminosité globale.
  * **Contraste (Dynamique) :** La dynamique est de $200 - 50 = 150$ niveaux. Puisque l'étendue maximale est $255 - 0 = 255$, l'image n'utilise que $\frac{150}{255} \approx 58.8\%$ de la gamme tonale possible. On peut donc dire que cette image a un **contraste modéré à faible** et pourrait bénéficier d'un **étirement de dynamique** (voir TP 2).