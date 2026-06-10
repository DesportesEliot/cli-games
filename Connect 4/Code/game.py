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