# 🖼️ Série de Travaux Pratiques : Traitement d'Image Numérique (Master 2)

Ce dépôt contient la série complète de Travaux Pratiques réalisés pour le module de Traitement d'Image Numérique. L'objectif est d'implémenter manuellement (sans utiliser de bibliothèques haut niveau comme OpenCV pour les algorithmes) les fondations du traitement d'image, de la lecture PGM à la morphologie mathématique.

## 🎯 Objectifs Pédagogiques

* **Compréhension Mathématique :** Maîtriser les algorithmes clés basés sur l'algèbre matricielle et le calcul différentiel.
* **Code Professionnel :** Développer un code Python propre, modulaire et bien documenté (utilisation de classes, de fonctions utilitaires).

## 📁 Structure du Projet

| Dossier | Description |
| :--- | :--- |
| `utils/` | Fonctions et classes Python réutilisables (e.g., `ImagePGM` pour la manipulation de données). |
| `images/` | Contient toutes les images de test (`.pgm` recommandées). |
| `TPX_.../` | Contient le code principal (`main.py`) et le `README.md` spécifique pour chaque TP. |

## 💻 Environnement et Dépendances

Ce projet utilise principalement **Python** et la bibliothèque **NumPy** pour la gestion efficace des matrices.

```bash
# Recommandation : Utiliser un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sous Linux/macOS
# .\venv\Scripts\activate  # Sous Windows

# Installation des dépendances
pip install numpy