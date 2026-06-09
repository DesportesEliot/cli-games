# Backlog de Développement : 2048 CLI 

Ce backlog définit la feuille de route pour l'implémentation du jeu 2048 en mode console. Les tâches sont classées par ordre de priorité pour construire d'abord un produit minimum viable (MVP), puis enrichir l'expérience utilisateur pour correspondre aux standards du projet `cli-games`.

---

## 🏃‍♂️ Sprint 1 : Mécanique de Base (Le Moteur Mathématique)
*Objectif : Mettre en place les fondations algorithmiques du jeu (grille et mouvements).*

### [STORY-01] Initialisation de la grille et affichage de base
- [x] **Tâche 1 :** Créer la structure de données pour la grille (une liste de listes 4x4 remplie de zéros).
- [x] **Tâche 2 :** Écrire la fonction `AddRandomTile()` pour générer un `2` ou un `4` aléatoirement.
- [x] **Tâche 3 :** Créer la fonction `Print()` pour dessiner la grille en texte brut.
- [x] **Tâche 4 :** Implémenter la logique de base du déplacement vers la gauche (`slideLigne` et `fusionneLigne`).

### [STORY-02] Logique des 4 directions
- [x] **Tâche 1 :** Créer une fonction `InverserLignes()` (pour le mouvement Droite).
- [x] **Tâche 2 :** Créer une fonction `TransposerMatrice()` (pour les mouvements Haut/Bas).
- [x] **Tâche 3 :** Implémenter `DeplacerDroite()`, `DeplacerHaut()` et `DeplacerBas()`.
- [x] **Tâche 4 :** Sécuriser `AddRandomTile()` pour qu'elle ne se déclenche que si la grille a bougé.

*Objectif : Ajouter les conditions de victoire/défaite et rendre le jeu jouable au tour par tour.*

### [STORY-03] Conditions de Fin de Partie (Victoire & Défaite)
- [x] **Tâche 1 :** Créer `EstVictoire() bool` qui cherche la tuile `2048`.
- [x] **Tâche 2 :** Créer `EstBloque() bool` qui vérifie si la grille est pleine ET sans fusion possible.
- [x] **Tâche 3 :** Créer `EstGameOver() bool` pour valider la défaite totale.

### [STORY-04] Boucle de jeu brute (Saisie Standard)
- [x] **Tâche 1 :** Créer la boucle `for` principale dans `main()`.
- [x] **Tâche 2 :** Utiliser `input()` pour la saisie (ex: 'z'=haut, 's'=bas, 'q'=gauche, 'd'=droite).
- [x] **Tâche 3 :** Brancher les saisies sur les fonctions de déplacement correspondantes.
- [x] **Tâche 4 :** Gérer l'arrêt de la boucle avec les messages "Gagné !" ou "Game Over !".

---

## 🏃‍♂️ Sprint 2 : Expérience Terminal (Temps Réel)
*Objectif : Supprimer la touche "Entrée" et rendre l'affichage fluide et dynamique.*

### [STORY-05] Capture instantanée du clavier (Mode Raw)
- [ ] **Tâche 1 :** Importer une bibliothèque CLI.
- [ ] **Tâche 2 :** Initialiser la bibliothèque et écouter les événements clavier en continu.
- [ ] **Tâche 3 :** Remplacer le `input()` par la capture directe des flèches directionnelles.

### [STORY-06] Rafraîchissement propre de l'écran
- [ ] **Tâche 1 :** Implémenter une fonction de nettoyage d'écran adaptée à la librairie choisie.
- [ ] **Tâche 2 :** Nettoyer le terminal avant chaque frame pour empêcher l'empilement du texte.

### [STORY-07] Gestion du Score en temps réel
- [ ] **Tâche 1 :** Ajouter une variable `Score`.
- [ ] **Tâche 2 :** Faire en sorte que les fusions additionnent les valeurs au score global.
- [ ] **Tâche 3 :** Afficher le score mis à jour au-dessus de la grille à chaque frame.

*Objectif : Rendre le jeu visuellement attractif et prêt à être partagé sur GitHub.*

### [STORY-08] Couleurs ANSI & Design de la grille
- [ ] **Tâche 1 :** Associer chaque valeur (2, 4, 8, 16...) à un code couleur spécifique.
- [ ] **Tâche 2 :** Appliquer ces couleurs lors du rendu pour une lisibilité instantanée.
- [ ] **Tâche 3 :** Utiliser des caractères "Box Drawing" unicode (ex: `╔═╗`) pour de belles bordures.

### [STORY-09] Système de High Score persistant
- [ ] **Tâche 1 :** Lire un fichier local `.2048_highscore` au démarrage.
- [ ] **Tâche 2 :** Sauvegarder le nouveau record dans ce fichier si le joueur se surpasse.
- [ ] **Tâche 3 :** Afficher le "Meilleur Score" sur l'interface de jeu.
