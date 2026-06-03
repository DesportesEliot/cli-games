# Backlog de Développement : 2048 CLI 

Ce backlog définit la feuille de route pour l'implémentation du jeu 2048 en mode console. Les tâches sont classées par ordre de priorité pour construire d'abord un produit minimum viable (MVP), puis enrichir l'expérience utilisateur pour correspondre aux standards du projet `cli-games`.

---

## 🟢 Étape 1 : Le Moteur de Jeu (MVP)
*L'objectif est d'avoir la logique algorithmique pure du jeu 2048 fonctionnelle en arrière-plan.*

- [ ] **STORY-01 : Initialisation de la grille**
  - Initialiser une matrice de 4x4.
  - Placer deux tuiles aléatoires (90% de chance d'avoir un `2`, 10% de chance d'avoir un `4`) sur des cases vides au démarrage.
- [ ] **STORY-02 : Logique des 4 directions (Mouvements & Fusions)**
  - Implémenter le déplacement et la fusion vers la **Gauche**.
  - Implémenter les mouvements **Droite**, **Haut** et **Bas** (Astuce : utiliser des fonctions de rotation de matrice pour réutiliser la logique "Gauche").
  - Générer une nouvelle tuile aléatoire après chaque coup valide (un coup est valide si au moins une tuile a bougé ou fusionné).
- [ ] **STORY-03 : Conditions de Fin de Partie**
  - Détecter la condition de **Victoire** : une tuile atteint la valeur `2048`.
  - Détecter la condition de **Défaite (Game Over)** : la grille est pleine ET aucun mouvement/fusion n'est possible dans les 4 directions.
- [ ] **STORY-04 : Boucle de jeu brute (Entrées standard)**
  - Créer une boucle `main` qui attend une saisie utilisateur via la console (ex: taper `g` + Entrée pour aller à gauche).
  - Afficher la grille de manière textuelle rudimentaire après chaque action.

---

## 🟡 Étape 2 : L'Expérience Terminal (Temps Réel)
*L'objectif est de rendre le jeu dynamique, fluide et interactif sans fioritures visuelles majeures.*

- [ ] **STORY-05 : Capture instantanée du clavier (Raw Mode)**
  - Intégrer une bibliothèque de gestion de terminal (ex: `nsf/termbox-go` ou `gdamore/tcell`).
  - Intercepter l'appui direct sur les flèches du clavier ou les touches `ZQSD` / `WASD` sans imposer à l'utilisateur d'appuyer sur la touche "Entrée".
- [ ] **STORY-06 : Rafraîchissement propre de l'écran**
  - Effacer proprement le terminal à chaque frame pour éviter que les grilles ne s'empilent verticalement dans l'historique de la console.
- [ ] **STORY-07 : Gestion du Score**
  - Initialiser un compteur à 0.
  - Ajouter des points en temps réel lors des fusions (ex : fusionner deux tuiles `8` ajoute immédiatement `+16` au score).

---

## 🔵 Étape 3 : Design & Finitions (Polish)
*L'objectif est d'aligner le rendu visuel avec les standards graphiques du projet `cli-games`.*

- [ ] **STORY-08 : Couleurs ANSI pour les tuiles**
  - Associer un code couleur spécifique du terminal à chaque valeur de tuile (ex: fond vert pour le 2, bleu pour le 4, rouge pour le 2048) pour une lisibilité instantanée.
- [ ] **STORY-09 : Système de High Score persistant**
  - Sauvegarder le meilleur score dans un fichier local discret (ex: `.2048_score`).
  - Charger ce score au lancement du jeu et mettre à jour le fichier si le joueur bat son record.
