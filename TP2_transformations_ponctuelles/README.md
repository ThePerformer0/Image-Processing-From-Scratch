# ⚙️ TP 2 : Transformations Ponctuelles (Look-Up Tables)

## 🎯 Objectifs

* Comprendre le concept des **Transformations Ponctuelles** (ou Look-Up Tables, LUTs).
* Implémenter l'opération d'**inversion négative**.
* Implémenter le contrôle de la **luminosité** et du **contraste linéaire**.
* Implémenter l'**Égalisation d'Histogramme** (une technique non-linéaire fondamentale).

## 1. Principe Mathématique

Une transformation ponctuelle est une fonction $T$ appliquée à chaque pixel indépendamment de ses voisins :

$$I_{\text{out}}(x, y) = T(I_{\text{in}}(x, y))$$

Pour une image 8 bits, $I_{\text{in}}$ et $I_{\text{out}}$ appartiennent à l'intervalle $[0, 255]$.

## 2. Implémentations (À faire)

Toutes les fonctions seront implémentées dans une classe ou un module d'utilitaires, et testées dans `main.py`. Nous réutiliserons la classe `ImagePGM` et les fonctions d'I/O du TP 1.

## 3. Exécution

```bash
# Assurez-vous d'être dans le dossier TP2_transformations_ponctuelles
python main.py ../images/image_test.pgm