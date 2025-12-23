# 🧪 Guide de Test et de Validation - VisionCore

Ce document guide l'utilisateur à travers différents scénarios pour tester la robustesse et la précision des algorithmes implémentés dans VisionCore.

## 📁 Images de Test recommandées
Pour des résultats optimaux, utilisez les images classiques du traitement d'image :
* `cameraman.pgm` (pour les contours et la segmentation)
* `lena.png` (pour le lissage et l'histogramme)
* Toute image sous-exposée ou bruitée.

---

## 🛠️ Scénario 1 : Restauration d'Images Terne ou Bruitée
**Objectif :** Valider l'amélioration du contraste et le débruitage non-linéaire.

1.  **Charger une image sombre :** Observez l'histogramme concentré à gauche.
2.  **Appliquer 'Étirement Dyn.' :** L'histogramme s'étire sur toute la plage [0, 255].
3.  **Appliquer 'Égaliser Hist.' :** Observez la redistribution uniforme des niveaux de gris pour maximiser les détails.
4.  **Test du Bruit :** Si l'image est granuleuse, appliquez le **'Filtre Médian'**. Comparez avec le **'Flou Gaussien'** pour noter comment le Médian préserve la netteté des bords tout en éliminant les pixels isolés.

## 📐 Scénario 2 : Analyse de Contours (Gradient)
**Objectif :** Valider l'extraction de caractéristiques hautes fréquences.

1.  **Charger `cameraman.pgm`.**
2.  *(Optionnel)* Appliquer un **'Flou Gaussien'** léger pour réduire le bruit de fond.
3.  **Appliquer 'Contours (Sobel)' :** L'image devient noire avec les contours blancs. 
    * *Note technique :* L'application calcule la norme du gradient $|\nabla f| \approx |G_x| + |G_y|$.

## 🎯 Scénario 3 : Segmentation et Morphologie Mathématique
**Objectif :** Isoler un objet du fond de manière automatisée.

1.  **Appliquer 'Seuillage Otsu' :** L'algorithme calcule automatiquement le seuil optimal en minimisant la variance intra-classe. L'image devient binaire.
2.  **Nettoyage (Morpho) :** * Si des points blancs indésirables apparaissent dans le fond noir : appliquez **'Érosion'**.
    * Si l'objet présente des trous noirs internes : appliquez **'Dilatation'**.

---

## 📊 Interprétation de l'Analyseur
Sous l'image, le panneau de statistiques permet de vérifier en temps réel :
* **Luminance :** La moyenne des intensités.
* **Contraste (Std Dev) :** L'écart-type. Une valeur élevée indique une image dynamique.
* **Histogramme :** Visualisation de la distribution spectrale.