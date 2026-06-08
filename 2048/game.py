import random
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
    def add_random_tile(self):
        """
        Ajoute un 2 ou un 4 dans une case vide aléatoire.
        """
        empty_cells = []

        for row in range(4):
            for col in range(4):
                if self.grid[row][col] == 0:
                    empty_cells.append((row, col))

        if not empty_cells:
            return False

        row, col = random.choice(empty_cells)

        self.grid[row][col] = 2 if random.random() < 0.9 else 4

        return True    