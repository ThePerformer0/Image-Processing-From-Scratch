# 👁️ VisionCore - Suite Logicielle de Traitement d'Image

> **Projet de Master 2 - Génie Informatique**
> **Auteur :** FEKE JIMMY WILSON

## 📌 À propos
**VisionCore** est une application de bureau professionnelle dédiée à l'analyse et à la restauration d'images numériques. Conçue comme une synthèse de mes compétences acquises en Master 2, elle se distingue par son approche **"From Scratch"**.

Contrairement aux solutions commerciales qui utilisent des "boîtes noires", le moteur de VisionCore implémente manuellement les algorithmes fondamentaux du traitement du signal (convolutions, transformations fréquentielles, morphologie mathématique) en utilisant l'algèbre matricielle pure via **NumPy**.

## 🚀 Fonctionnalités Clés

### 1. Laboratoire d'Analyse
* **Histogramme Temps Réel :** Visualisation dynamique de la distribution spectrale.
* **Métriques :** Calcul instantané de la luminance, du contraste (RMS) et de l'entropie.

### 2. Moteur de Transformation
* **Photométrie :** Correction Gamma, égalisation d'histogramme, inversion négative.
* **Look-Up Tables (LUT) :** Optimisation des calculs pour un rendu instantané.

### 3. Filtrage Spatial & Convolution
* **Débruitage :** Filtres Gaussiens (lissage) et Médians (préservation des bords).
* **Extraction de Caractéristiques :** Détection de contours via opérateurs de gradient (Sobel, Prewitt).

### 4. Vision & Segmentation
* **Binarisation Intelligente :** Algorithme d'Otsu (minimisation de la variance intra-classe).
* **Morphologie :** Opérations d'érosion/dilatation pour le nettoyage des masques binaires.

## 🛠️ Stack Technique

| Composant | Technologie | Rôle |
| :--- | :--- | :--- |
| **Langage** | Python 3.10+ | Logique globale |
| **Core** | **NumPy** | Calcul matriciel haute performance |
| **I/O** | Pillow (PIL) | Gestion des formats (JPG, PNG, BMP) |
| **Interface** | **CustomTkinter** | UI Moderne (Dark Mode, Responsive) |
| **Graphiques** | Matplotlib | Visualisation des histogrammes |
| **Build** | PyInstaller | Compilation en exécutable (.exe / Linux) |

## 📦 Installation et Utilisation

### Prérequis
```bash
pip install -r requirements.txt