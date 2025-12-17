# 🖼️ VisionCore - Studio de Traitement d'Image (Projet M2)

## 📌 Présentation du Projet

**VisionCore** est une application de bureau performante conçue pour l'analyse et la manipulation d'images numériques. Développé dans le cadre d'un cursus de **Master 2**, ce projet vise à faire le pont entre les concepts théoriques du traitement de signal et une implémentation logicielle concrète.

L'originalité de VisionCore réside dans son moteur de calcul : contrairement aux logiciels utilisant des bibliothèques "boîte noire", chaque algorithme est réimplémenté **"from scratch"** à l'aide de matrices **NumPy**, garantissant une compréhension totale des transformations mathématiques opérées sur les pixels.

---

## 🚀 Fonctionnalités Détaillées

### 1. Analyse Statistique & Diagnostic

* **Histogramme Dynamique :** Visualisation en temps réel de la distribution des intensités H(k) .
* **Indicateurs de Qualité :** Calcul automatique de la luminance moyenne (brillance globale) et du contraste (étendue de la dynamique).
* **Explorateur de Pixels :** Analyse des valeurs min/max pour détecter les sous-expositions ou les saturations.

### 2. Amélioration de l'Image (Transformations Ponctuelles)

* **Correction Gamma :** Ajustement non-linéaire pour corriger les problèmes d'exposition sans écraser les détails .
* **Égalisation d'Histogramme :** Algorithme d'étirement basé sur la fonction de répartition cumulative (CDF) pour maximiser le contraste visuel .
* **Optimisation par LUT :** Implémentation via *Look-Up Tables* pour appliquer des réglages complexes instantanément, peu importe la taille de l'image.

### 3. Restauration & Filtrage (Espace Local)

* **Noyau de Convolution Générique :** Moteur capable d'appliquer n'importe quel masque de convolution M \times N.
* **Réduction du Bruit :** * *Filtre Gaussien* pour un lissage naturel.
* *Filtre Médian* pour l'élimination radicale du bruit impulsionnel (poivre et sel).


* **Netteté :** Accentuation des détails par filtres passe-haut.

### 4. Vision Artificielle & Segmentation

* **Détection de Contours :** Utilisation de l'opérateur de **Sobel** pour calculer le gradient spatial et isoler les formes .
* **Seuillage Intelligent (Otsu) :** Binarisation automatique de l'image en minimisant la variance intra-classe pour séparer l'objet du fond.
* **Morphologie Mathématique :** Nettoyage des segmentations par opérations d'Érosion, Dilatation, Ouverture et Fermeture.

---

## 🛠️ Architecture du Système

* **Moteur (Backend) :** `NumPy` pour le calcul matriciel intensif.
* **Interface (Frontend) :** `CustomTkinter` pour une expérience utilisateur moderne (Dark Mode natif).
* **Gestion de Flux :** `Pillow` pour l'interface entre les formats de fichiers (JPG, PNG, PGM) et les matrices de données.
* **Visualisation :** `Matplotlib` pour l'affichage scientifique des données.

```text
VisionCore/
├── main_app.py            # Point d'entrée et gestion de l'interface
├── core/
│   ├── processor.py       # Algorithmes de point (Gamma, Égalisation, etc.)
│   ├── filters.py         # Moteur de convolution et filtres locaux
│   └── segmentation.py    # Otsu et morphologie
├── utils/
│   └── image_io.py        # Chargement/Sauvegarde et conversion
└── assets/                # Design et icônes

```

---

## 🎓 Objectifs d'Apprentissage (Master 2)

Ce projet valide la maîtrise des piliers suivants :

1. **Algorithmique Numérique :** Optimisation des calculs sur de grands volumes de données.
2. **Mathématiques Discrètes :** Passage du continu au discret pour les dérivées (contours) et les intégrales (moyennes).
3. **Génie Logiciel :** Création d'une application modulaire, maintenable et distribuable.

---

## 📦 Compilation & Distribution

Le projet est conçu pour être compilé en un exécutable autonome :

* **Windows :** Génération d'un `.exe` via PyInstaller.
* **Linux :** Binaire ELF optimisé.

```bash
# Pour compiler :
pyinstaller --noconsole --onefile --name VisionCore main_app.py

```