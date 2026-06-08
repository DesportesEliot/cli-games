class Game2048:
    def __init__(self):
        """
        Initialise une nouvelle partie de 2048.
        Tâche 1 : Création de la structure de données pour la grille (matrice 4x4 d'entiers).
        Les cases vides sont représentées par des 0.
        """
        self.grid = [[0 for _ in range(4)] for _ in range(4)]

    def get_grid(self):
        """Retourne la grille actuelle."""
        return self.grid