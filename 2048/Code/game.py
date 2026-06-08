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

    def slide_ligne(self, ligne):
        """
        Déplace toutes les valeurs non nulles vers la gauche.
        Exemple : [2, 0, 2, 4] -> [2, 2, 4, 0]
        """
        resultat = [x for x in ligne if x != 0]

        while len(resultat) < 4:
            resultat.append(0)

        return resultat

    def fusionne_ligne(self, ligne):
        """
        Fusionne les cases identiques adjacentes.
        Exemple : [2, 2, 4, 0] -> [4, 0, 4, 0]
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
        Retourne True si la grille a été modifiée, False sinon.
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
        Retourne True si la grille a été modifiée.
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
    Transpose la grille.
    Les lignes deviennent des colonnes.
       """
       self.grid = [list(row) for row in zip(*self.grid)]
 
    def move_up(self):
        """
        Applique le mouvement vers le HAUT.
        Retourne True si la grille a été modifiée.
        """
        self.transpose_matrix()
        moved = self.move_left()
        self.transpose_matrix()
        return moved

    def move_down(self):
        """
        Applique le mouvement vers le BAS.
        Retourne True si la grille a été modifiée.
        """
        self.transpose_matrix()
        moved = self.move_right()
        self.transpose_matrix()
        return moved

if __name__ == "__main__":
    # 1. On initialise le jeu
    jeu = Game2048()

    # 2. On ajoute deux tuiles de départ, comme dans le vrai jeu
    jeu.add_random_tile()
    jeu.add_random_tile()

    # 3. On affiche la grille
    print("Grille de départ :")
    jeu.print_board()

    # --- SIMULATION DU JEU ET TEST DE LA TÂCHE 4 ---
    
    print("\n--- Le joueur fait un mouvement vers la GAUCHE ---")
    # On stocke le résultat du mouvement (True si la grille a changé, False sinon)
    grille_a_bouge = jeu.move_left() 

    # Tâche 4 : Sécurisation de l'apparition de la nouvelle tuile
    if grille_a_bouge:
        print("La grille a été modifiée ! Apparition d'une nouvelle tuile.")
        jeu.add_random_tile()
    else:
        print("Mouvement dans le vide. La grille n'a pas bougé, aucune tuile n'est ajoutée.")

    # On affiche le résultat
    jeu.print_board()