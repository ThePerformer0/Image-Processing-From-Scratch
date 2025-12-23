# 👁️ VisionCore - Studio Pro

> **Projet de Master 2 - Génie Informatique**
> **Auteur :** FEKE JIMMY WILSON
> **Sous la direction du Dr Hypolitte Tapamo**

---

## 🌟 La Philosophie du Projet

Bienvenue dans **VisionCore** ! Ce projet est né d'une envie simple : **performer comme toujours"**.

En tant qu'étudiant en Master 2 à l'ENSPY, nous avons eu a faire un cours sur le traitement d'image (je dois avouer que j'ai appris pas mal de chose). Pour **VisionCore**, j'ai décidé de soulever le capot : chaque filtre, chaque transformation et chaque calcul statistique a été réimplémenté **"From Scratch"** en utilisant la puissance de l'algèbre matricielle avec **NumPy**. Oui python c'est le meilleur

C'est une suite logicielle qui transforme des mathématiques pures en un outil de traitement d'image interactif, moderne et performant. 🚀

---

## 🚀 Fonctionnalités Clés

### 📊 1. Laboratoire d'Analyse en Temps Réel

* **Histogramme Dynamique :** Visualisation instantanée de la distribution des niveaux de gris via Matplotlib.
* **Métriques de Précision :** Calcul automatique de la Luminance moyenne, du Contraste (Ecart-type RMS) et de la dynamique (Min/Max).

### ⚡ 2. Moteur de Transformation Photométrique

* **Correction Gamma :** Ajustement non-linéaire de la luminance pour révéler les détails dans les zones sombres.
* **Égalisation d'Histogramme :** Algorithme de redistribution des fréquences pour maximiser le contraste global.
* **Étirement de la Dynamique :** Expansion linéaire des niveaux de gris sur toute la plage [0, 255].

### 🛡️ 3. Filtrage Spatial & Convolution

* **Débruitage Intelligent :** Filtre **Médian** (le roi contre le bruit poivre et sel) et Flou **Gaussien**.
* **Extraction de Caractéristiques :** Détection de contours via l'opérateur de **Sobel** (calcul des gradients verticaux et horizontaux).

### 🎯 4. Vision & Segmentation

* **Seuillage d'Otsu :** Binarisation automatique par recherche du seuil optimal (minimisation de la variance intra-classe).
* **Morphologie Mathématique :** Opérations d'Érosion et de Dilatation pour nettoyer les masques binaires.

---

## 🛠️ Stack Technique

| Composant | Technologie | Rôle |
| --- | --- | --- |
| **Langage** | Python 3.10+ | Le chef d'orchestre |
| **Core Engine** | **NumPy** | Calcul matriciel haute performance (Zéro boucle `for` inutile !) |
| **I/O** | Pillow (PIL) | Gestion robuste des formats (JPG, PNG, BMP, PGM) |
| **Interface** | **CustomTkinter** | UI Moderne, Dark Mode et Responsive |
| **Analytics** | Matplotlib | Rendu des graphiques statistiques |

---

## 📦 Installation rapide

1. **Cloner le projet**
```bash
git clone https://github.com/Theperfomer0/visioncore.git
cd visioncore

```


2. **Installer les dépendances**
```bash
pip install -r requirements.txt

```


3. **Lancer l'application**
```bash
python main.py

```



---

## 🧪 Comment tester l'application ?

Pour mon enseignant, le **Dr Hypolitte Tapamo**, ainsi que pour les curieux qui souhaitent explorer les capacités de l'outil, j'ai rédigé un guide de test complet :

👉 **[Consulter le GUIDE_TESTS.md](https://www.google.com/search?q=./TEST_GUIDE.md)**

Ce guide contient des scénarios pas-à-pas pour observer l'effet des algorithmes sur des images classiques (Cameraman, Lena, etc.).

---

## ❤️ Remerciements

Un grand merci au **Dr Hyppolite Tapamo** pour ses enseignements passionnants en traitement d'image qui ont rendu ce projet possible. Ce logiciel est le reflet de l'exigence et de la rigueur transmises durant ce cursus de Master 2.

---

**Fait avec passion et beaucoup de enthousiasme ☕ par The Performer.**

## 🧪 Tests et Démonstration
Pour tester les capacités de VisionCore (Restauration, Segmentation, Filtrage), veuillez consulter notre [Guide de Test détaillé (TEST_GUIDE.md)](./TEST_GUIDE.md).