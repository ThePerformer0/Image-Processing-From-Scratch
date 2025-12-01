# 📁 TP 1 : Représentation, Lecture et Analyse Basique de l'Image

## 🎯 Objectifs

* Définir la structure de données pour une image (`ImagePGM`).
* Implémenter la lecture/écriture du format **PGM (P2 et P5)** pour un traitement sans perte.
* Calculer et analyser les métriques fondamentales : **Histogramme**, **Luminance** et **Contraste**.
* Visualiser l'histogramme pour l'analyse tonale.

## 1. Structure de l'Image et Utilitaires

La classe `ImagePGM` est définie dans `../utils/image_utils.py`. Elle encapsule la matrice de pixels (`numpy.ndarray` de type `uint8`) et les propriétés de l'image (hauteur, largeur, valeur max).

## 2. Implémentation du PGM Reader/Writer (Terminé)

Les fonctions `read_pgm` et `write_pgm` supportent la lecture des formats **PGM ASCII (P2)** et **PGM Binaire (P5)**, et l'écriture est effectuée en **P5** pour la performance.

## 3. Exécution et Dépendances

### Dépendances
Ce TP nécessite `numpy` et `matplotlib`. Installez-les via le fichier `requirements.txt` situé à la racine du projet :
```bash
pip install -r ../requirements.txt
```

### Exécution du Programme

Le script `main.py` lit une image PGM, vérifie les fonctions de lecture/écriture, calcule les métriques et affiche l'histogramme.

Pour exécuter le TP (en étant dans le dossier `TP1_representation/`):

```bash
python main.py ../images/cameraman.pgm
```

## 4\. Résultats et Analyse

Voici un exemple des résultats statistiques obtenus après exécution :

| Métrique | Valeur (Exemple: cameraman.pgm) | Interprétation |
| :--- | :--- | :--- |
| **Taille** | $256 \times 256$ pixels | Résolution spatiale. |
| **Luminance (Moyenne)** | $166.94$ | L'image est globalement claire (au-dessus du point médian 127.5). |
| **Niveau de Gris Min** | $22$ | Le noir le plus profond dans l'image. |
| **Niveau de Gris Max** | $255$ | Le blanc le plus pur (utilise la limite haute 255). |
| **Contraste (Dynamique)** | $233$ | L'image utilise 233 niveaux sur 256, ce qui est un très bon contraste. |

### Visualisation

L'histogramme (visualisé par Matplotlib) montre la distribution des intensités, confirmant la prédominance des niveaux de gris clairs.

## ❓ Questions de Compréhension (Réponses)

### 1\. Quelle est la différence fondamentale entre la **résolution spatiale** et la **résolution tonale** ?

  * **Résolution Spatiale :** Définit le **nombre de pixels** (la taille de la grille $M \times N$). Elle impacte la finesse des détails.
  * **Résolution Tonale :** Définit le **nombre de niveaux d'intensité** (la profondeur de bits, ex: 256 niveaux pour 8 bits). Elle impacte la précision des nuances de couleur ou de gris.

### 2\. Pourquoi le format **JPEG est généralement déconseillé pour le traitement d'images** après une opération, et pourquoi PGM/PPM sont-ils souvent préférés ?

  * **JPEG** utilise une **compression avec perte** (lossy compression) basée sur la Transformée en Cosinus Discrète (DCT). Chaque modification et réenregistrement dégrade l'image (artefacts).
  * **PGM/PPM** utilisent une **représentation brute et sans perte** (lossless) des données, essentielle pour un traitement numérique précis où chaque bit d'information est important.

### 3\. Si une image 8 bits (0 à 255) a une luminance de 128 et une dynamique (valeur\_min, valeur\_max) de [50, 200], comment décririez-vous le contraste de cette image ?

  * **Luminance (Moyenne) :** 128 est exactement le milieu de l'échelle [0, 255], signifiant une luminosité globale neutre.
  * **Contraste (Dynamique) :** L'image utilise $150$ niveaux sur $255$ (environ $58.8\%$ de la gamme). L'image a un **contraste modéré à faible** et pourrait être améliorée par des transformations d'étirement de dynamique.