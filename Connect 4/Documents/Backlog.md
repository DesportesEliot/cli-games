# Backlog de Développement : Puissance 4 CLI 

Ce backlog définit la feuille de route pour l'implémentation du jeu Puissance 4 en mode console avec Python. Le découpage est resserré autour d'objectifs globaux pour un développement plus agile.

## 🏃‍♂️ Sprint 2 : 
*Objectif : Avoir un jeu de Puissance 4 fonctionnel, de bout en bout, avec une saisie standard.*

### [STORY-01] Moteur de la Grille et Mécanique de Placement
- [ ] **Tâche 1 :** Créer la grille (matrice 6x7 de zéros) et le système de joueurs (X et O).
- [ ] **Tâche 2 :** Implémenter la fonction `afficher_grille()` pour un rendu texte basique dans le terminal.
- [ ] **Tâche 3 :** Créer la logique de "gravité" (`placer_jeton`) qui valide la colonne et fait tomber le jeton à la ligne vide la plus basse.

### [STORY-02] Boucle de Jeu et Détection de Fin de Partie
- [ ] **Tâche 1 :** Implémenter la détection de victoire (vérification des alignements de 4 jetons : horizontal, vertical et les deux diagonales).
- [ ] **Tâche 2 :** Implémenter la détection de match nul (grille pleine sans vainqueur).
- [ ] **Tâche 3 :** Créer la boucle de jeu principale : demander au joueur actuel de choisir une colonne via `input()`, gérer les erreurs de saisie, et alterner les tours jusqu'à la fin de partie.

### [STORY-03] Contrôles Dynamiques et Design Visuel
- [ ] **Tâche 1 :** Utiliser une bibliothèque CLI (`keyboard` ou `curses`) pour remplacer le `input()` par un curseur visuel (ex: `V`) déplaçable de gauche à droite avec les flèches directionnelles.
- [ ] **Tâche 2 :** Intégrer des couleurs ANSI (ex: Rouge pour J1, Jaune pour J2) et utiliser des caractères Unicode pour dessiner une belle grille (bords et colonnes).
- [ ] **Tâche 3 :** Mettre en surbrillance l'alignement gagnant à la fin de la partie.

### [STORY-04] Mode Multimanque et Système de Score
- [ ] **Tâche 1 :** Implémenter un système de score persistant pendant la session (`score_j1` et `score_j2`) affiché en haut de l'écran.
- [ ] **Tâche 2 :** À l'écran de fin, proposer de relancer une nouvelle manche d'une simple pression de touche, en réinitialisant uniquement la grille.