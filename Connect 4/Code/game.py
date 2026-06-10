import random

class Connect4:
    def __init__(self):
        """
        Initialise une partie de Puissance 4.
        """
        # Grille 6x7 remplie de 0
        self.grid = [[0 for _ in range(7)] for _ in range(6)]

        # Joueur courant
        self.current_player = "X"

    def get_grid(self):
        """
        Retourne la grille.
        """
        return self.grid

    def get_current_player(self):
        """
        Retourne le joueur actuel.
        """
        return self.current_player

    def switch_player(self):
        """
        Change de joueur : X <-> O
        """
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def afficher_grille(self):
        """
        Affiche la grille dans le terminal (rendu texte basique).
        Les zéros sont remplacés par des '.' pour une meilleure lisibilité.
        """
        for row in self.grid:
            print(" ".join(str(cell) if cell != 0 else "." for cell in row))
        # Affichage des numéros de colonnes sous la grille pour aider le joueur
        print("0 1 2 3 4 5 6")

    def placer_jeton(self, colonne):
        """
        Tâche 3 : Logique de "gravité"
        Place le jeton du joueur actuel dans la colonne choisie en le faisant
        tomber sur la ligne vide la plus basse.
        Retourne True si le placement est réussi, False si la colonne est pleine ou invalide.
        """
        # 1. Vérification si l'index de la colonne est correct
        if colonne < 0 or colonne >= 7:
            return False

        # 2. On parcourt de la ligne du bas (5) jusqu'à la ligne du haut (0)
        # range(5, -1, -1) signifie : commence à 5, va jusqu'à 0 inclus, à reculons (-1)
        for ligne in range(5, -1, -1):
            if self.grid[ligne][colonne] == 0:
                # On trouve une case vide, on y dépose le jeton
                self.grid[ligne][colonne] = self.current_player
                return True # Placement réussi !

        # 3. Si la boucle s'est terminée sans trouver de 0, la colonne est pleine
        return False
    
    def verifier_victoire(self):
        joueur = self.current_player

        # Vérification horizontale
        for ligne in range(6):
            for col in range(4):
                if (self.grid[ligne][col] == joueur and
                    self.grid[ligne][col + 1] == joueur and
                    self.grid[ligne][col + 2] == joueur and
                    self.grid[ligne][col + 3] == joueur):
                    return True

        # Vérification verticale
        for ligne in range(3):
            for col in range(7):
                if (self.grid[ligne][col] == joueur and
                    self.grid[ligne + 1][col] == joueur and
                    self.grid[ligne + 2][col] == joueur and
                    self.grid[ligne + 3][col] == joueur):
                    return True

        # Vérification diagonale descendante (\)
        for ligne in range(3):
            for col in range(4):
                if (self.grid[ligne][col] == joueur and
                    self.grid[ligne + 1][col + 1] == joueur and
                    self.grid[ligne + 2][col + 2] == joueur and
                    self.grid[ligne + 3][col + 3] == joueur):
                    return True

        # Vérification diagonale montante (/)
        for ligne in range(3, 6):
            for col in range(4):
                if (self.grid[ligne][col] == joueur and
                    self.grid[ligne - 1][col + 1] == joueur and
                    self.grid[ligne - 2][col + 2] == joueur and
                    self.grid[ligne - 3][col + 3] == joueur):
                    return True

        return False

    def verifier_match_nul(self):
        """
        Vérifie si la grille est pleine.
        Retourne True si aucune case vide n'est présente.
        """
        for ligne in self.grid:
            if 0 in ligne:
                return False

        return True

    def jouer(self):
        """
        STORY-02 - Tâche 3 : Boucle de jeu principale.
        Gère les tours des joueurs, les saisies de colonne et la fin de la partie.
        """
        print("--- Début de la partie de Puissance 4 ! ---")
        
        while True:
            # 1. On affiche l'état actuel de la grille
            print("\n")
            self.afficher_grille()
            print(f"C'est au tour du joueur {self.current_player}.")

            # 2. Boucle de saisie avec gestion des erreurs
            colonne_choisie = -1
            while True:
                saisie = input("Choisissez une colonne (0-6) : ").strip()
                
                # Vérification si la saisie est bien un nombre entier
                if not saisie.isdigit():
                    print("Erreur : Veuillez entrer un nombre valide entre 0 et 6.")
                    continue
                
                colonne_choisie = int(saisie)
                
                # Tentative de placement du jeton (vérifie en même temps si l'index est valide et la colonne non pleine)
                if self.placer_jeton(colonne_choisie):
                    break # Placement réussi, on quitte la boucle de saisie
                else:
                    print("Erreur : Colonne pleine ou invalide (hors limites). Réessayez.")

            # 3. Vérification si le coup actuel entraîne une victoire
            if self.verifier_victoire():
                print("\n")
                self.afficher_grille()
                print(f"Félicitations ! Le joueur {self.current_player} a gagné la partie !")
                break

            # 4. Vérification si le coup actuel entraîne un match nul
            if self.verifier_match_nul():
                print("\n")
                self.afficher_grille()
                print("Match nul ! La grille est pleine.")
                break

            # 5. Changement de joueur pour le tour suivant
            self.switch_player()


# --- ZONE DE TEST ---
if __name__ == "__main__":
    jeu = Connect4()
    # Lancement de la boucle principale du jeu
    jeu.jouer()