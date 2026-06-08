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
    

    def print_board(self):
        """
        Affiche la grille de jeu en texte brut dans la console.
        Tâche 3 : Dessiner la grille en texte brut.
        """
        print("+------+------+------+------+")
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    print("|      ", end="")
                else:
                    print(f"| {cell:4d} ", end="")
            
            print("|")
            print("+------+------+------+------+")

    

if __name__ == "__main__":
    # 1. On initialise le jeu 
    jeu = Game2048()
        
    # 2. On ajoute deux tuiles de départ, comme dans le vrai jeu 
    jeu.add_random_tile()
    jeu.add_random_tile()
    
    # 3. On affiche la grille 
    print("Grille de départ :")
    jeu.print_board()