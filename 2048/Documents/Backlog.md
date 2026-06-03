# Backlog de Développement : 2048 CLI 

Ce backlog définit la feuille de route pour l'implémentation du jeu 2048 en mode console. Les tâches sont classées par ordre de priorité pour construire d'abord un produit minimum viable (MVP), puis enrichir l'expérience utilisateur pour correspondre aux standards du projet `cli-games`.

---

## 🏃‍♂️ Sprint 1 : Le Moteur Fonctionnel 
*Objectif : Avoir la logique algorithmique pure du jeu 2048 fonctionnelle, avec une saisie basique.*

### [STORY-01] Initialisation de la grille et affichage de base
- [ ] **Tâche 1 :** Créer la structure de données pour la grille (matrice `[4][4]int`).
- [ ] **Tâche 2 :** Écrire la fonction `AddRandomTile()` pour générer un `2` ou un `4` aléatoirement sur une case vide.
- [ ] **Tâche 3 :** Créer la fonction `Print()` pour dessiner la grille en texte brut dans la console.
- [ ] **Tâche 4 :** Implémenter la logique de base du déplacement vers la gauche (`slideLigne` et `fusionneLigne`).

### [STORY-02] Logique des 4 directions
- [ ] **Tâche 1 :** Créer une fonction `InverserLignes()` (pour inverser l'ordre des éléments d'une ligne, utile pour le mouvement Droite).
- [ ] **Tâche 2 :** Créer une fonction `TransposerMatrice()` (pour échanger les lignes et colonnes, utile pour Haut/Bas).
- [ ] **Tâche 3 :** Implémenter `DeplacerDroite()`, `DeplacerHaut()` et `DeplacerBas()` en combinant les inversions/transpositions avec la logique "Gauche".
- [ ] **Tâche 4 :** S'assurer que `AddRandomTile()` n'est appelée **que si** la grille a effectivement été modifiée par un mouvement.

### [STORY-03] Conditions de Fin de Partie (Victoire & Défaite)
- [ ] **Tâche 1 :** Créer une fonction `EstVictoire() bool` qui cherche la tuile `2048`.
- [ ] **Tâche 2 :** Créer une fonction `EstBloque() bool` qui vérifie si la grille est pleine ET qu'aucune fusion n'est possible.
- [ ] **Tâche 3 :** Créer une fonction `EstGameOver() bool` pour valider la fin de partie.

### [STORY-04] Boucle de jeu brute (Saisie Standard)
- [ ] **Tâche 1 :** Créer une boucle `for` infinie dans la fonction `main()`.
- [ ] **Tâche 2 :** Utiliser `fmt.Scanln()` pour demander une action au joueur (ex: 'z'=haut, 's'=bas, 'q'=gauche, 'd'=droite).
- [ ] **Tâche 3 :** Brancher les saisies utilisateur sur les bonnes fonctions de déplacement.
- [ ] **Tâche 4 :** Ajouter les messages de fin ("Gagné !" ou "Game Over !") qui stoppent la boucle.

---

## 🏃‍♂️ Sprint 2 : L'Interaction Terminal (Temps Réel)
*Objectif : Transformer le script en un vrai jeu interactif sans avoir à appuyer sur "Entrée" à chaque coup.*

### [STORY-05] Capture instantanée du clavier (Mode Raw)
- [ ] **Tâche 1 :** Importer une bibliothèque de gestion de terminal (ex: `nsf/termbox-go` ou `gdamore/tcell`).
- [ ] **Tâche 2 :** Initialiser la bibliothèque et configurer l'écoute des événements clavier.
- [ ] **Tâche 3 :** Remplacer `fmt.Scanln` par la capture directe des flèches du clavier ou des touches `ZQSD`/`WASD`.

### [STORY-06] Rafraîchissement propre de l'écran
- [ ] **Tâche 1 :** Implémenter une fonction de nettoyage d'écran (ex: `termbox.Clear()`).
- [ ] **Tâche 2 :** Nettoyer le terminal avant chaque affichage pour éviter l'empilement vertical des grilles.

### [STORY-07] Gestion du Score
- [ ] **Tâche 1 :** Ajouter une variable `Score` au jeu.
- [ ] **Tâche 2 :** Modifier les fusions pour additionner les valeurs combinées au score global.
- [ ] **Tâche 3 :** Afficher le score en temps réel au-dessus de la grille.

---

## 🏃‍♂️ Sprint 3 : Design & Finitions (Polish)
*Objectif : Rendre le jeu visuellement attractif et aligné avec les standards du dépôt cli-games.*

### [STORY-08] Couleurs ANSI pour les tuiles
- [ ] **Tâche 1 :** Créer une map associant chaque valeur (2, 4, 8, 16...) à un code couleur ANSI ou à un attribut de la librairie graphique.
- [ ] **Tâche 2 :** Appliquer ces couleurs lors de l'affichage pour différencier les tuiles instantanément.
- [ ] **Tâche 3 :** Améliorer le design des bordures (utiliser des caractères Box Drawing unicode au lieu de `+` et `-`).

### [STORY-09] Système de High Score persistant
- [ ] **Tâche 1 :** Créer une fonction pour lire un fichier caché `.2048_highscore` au démarrage.
- [ ] **Tâche 2 :** Sauvegarder et écraser la valeur dans ce fichier si le joueur bat son record.
- [ ] **Tâche 3 :** Afficher le "Meilleur Score" à côté du score actuel.
