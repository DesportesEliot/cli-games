import random

class Game2048:
    def __init__(self):
        """
        Initialise une nouvelle partie de 2048.
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

    def slide_ligne(self, ligne):
        """
        Déplace toutes les valeurs non nulles vers la gauche.
        """
        resultat = [x for x in ligne if x != 0]
        while len(resultat) < 4:
            resultat.append(0)
        return resultat

    def fusionne_ligne(self, ligne):
        """
        Fusionne les cases identiques adjacentes.
        """
        resultat = ligne.copy()
        for i in range(len(resultat) - 1):
            if resultat[i] != 0 and resultat[i] == resultat[i + 1]:
                resultat[i] *= 2
                resultat[i + 1] = 0
        return resultat
    
    def move_left(self):
        """
        Applique le glissement et la fusion vers la GAUCHE sur toute la grille.
        """
        moved = False
        for i in range(4):
            ligne_originale = self.grid[i].copy()
            etape1 = self.slide_ligne(ligne_originale)
            etape2 = self.fusionne_ligne(etape1)
            ligne_finale = self.slide_ligne(etape2)
            self.grid[i] = ligne_finale
            if ligne_originale != ligne_finale:
                moved = True
        return moved

    def move_right(self):
        """
        Applique le mouvement vers la DROITE en inversant les lignes.
        """
        moved = False
        for i in range(4):
            ligne_originale = self.grid[i].copy()
            ligne_inversee = ligne_originale[::-1]
            etape1 = self.slide_ligne(ligne_inversee)
            etape2 = self.fusionne_ligne(etape1)
            ligne_finale_inversee = self.slide_ligne(etape2)
            ligne_finale = ligne_finale_inversee[::-1]
            self.grid[i] = ligne_finale
            if ligne_originale != ligne_finale:
                moved = True
        return moved

    def transpose_matrix(self):
        """
        Transpose la grille. Les lignes deviennent des colonnes.
        """
        self.grid = [list(row) for row in zip(*self.grid)]
 
    def move_up(self):
        """
        Applique le mouvement vers le HAUT.
        """
        self.transpose_matrix()
        moved = self.move_left()
        self.transpose_matrix()
        return moved

    def move_down(self):
        """
        Applique le mouvement vers le BAS.
        """
        self.transpose_matrix()
        moved = self.move_right()
        self.transpose_matrix()
        return moved
    
    def est_victoire(self):
        """
        Vérifie si le joueur a atteint la tuile 2048.
        """
        for ligne in self.grid:
            if 2048 in ligne:
                return True
        return False

    def est_bloque(self):
        """
        Tâche 2 : Vérifie si la grille est pleine ET qu'aucune fusion n'est possible.
        Retourne True si le joueur a perdu (Game Over), False sinon.
        """
        # 1. On cherche s'il y a des cases vides
        for row in range(4):
            for col in range(4):
                if self.grid[row][col] == 0:
                    return False  # La grille n'est pas pleine

        # 2. On vérifie les fusions possibles horizontalement
        for row in range(4):
            for col in range(3): # On va jusqu'à 3 pour éviter de dépasser la grille avec col+1
                if self.grid[row][col] == self.grid[row][col + 1]:
                    return False  # Fusion possible !

        # 3. On vérifie les fusions possibles verticalement
        for col in range(4):
            for row in range(3): # Pareil, on va jusqu'à 3
                if self.grid[row][col] == self.grid[row + 1][col]:
                    return False  # Fusion possible !

        # Si on arrive jusqu'ici, c'est qu'il n'y a ni case vide, ni fusion possible.
        return True


if __name__ == "__main__":
    jeu = Game2048()

    # --- SIMULATION GRILLE CLASSIQUE ---
    jeu.add_random_tile()
    jeu.add_random_tile()
    print("--- Test de l'état initial ---")
    jeu.print_board()
    
    if jeu.est_bloque():
        print("❌ Game Over ! (Ce serait bizarre dès le début...)")
    else:
        print("✅ Le jeu n'est pas bloqué, on peut jouer !\n")

    # --- SIMULATION GRILLE BLOQUÉE (Game Over) ---
    print("--- On triche et on crée une grille totalement bloquée ---")
    # Une disposition en damier où aucune case adjacente n'est identique
    jeu.grid = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    jeu.print_board()

    if jeu.est_bloque():
        print("❌ Game Over ! La grille est pleine et bloquée.")
    else:
        print("✅ Il y a un bug, la grille devrait être bloquée !")