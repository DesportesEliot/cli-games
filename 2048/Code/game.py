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
        Vérifie si la grille est pleine ET qu'aucune fusion n'est possible.
        Retourne True si le joueur a perdu (Game Over), False sinon.
        """
        for row in range(4):
            for col in range(4):
                if self.grid[row][col] == 0:
                    return False

        for row in range(4):
            for col in range(3):
                if self.grid[row][col] == self.grid[row][col + 1]:
                    return False

        for col in range(4):
            for row in range(3):
                if self.grid[row][col] == self.grid[row + 1][col]:
                    return False

        return True

    def est_game_over(self):
        """
        Vérifie si la partie est terminée par défaite.
        """
        return self.est_bloque()


if __name__ == "__main__":
    jeu = Game2048()

    # Initialisation classique : 2 tuiles de départ
    jeu.add_random_tile()
    jeu.add_random_tile()

    print("=== BIENVENUE DANS 2048 ===")

    # Tâche 2 : Boucle de jeu utilisant input()
    while True:
        jeu.print_board()

        # Vérification des conditions de fin de jeu 
        if jeu.est_victoire():
            print("🏆 Victoire ! Vous avez atteint 2048 !")
            break

        if jeu.est_game_over():
            print("❌ Game Over ! La grille est pleine et bloquée.")
            break

        # Saisie utilisateur sécurisée
        action = input("Jouez (z=haut, s=bas, q=gauche, d=droite) ou 'quit' pour arrêter : ").lower()

        moved = False

        if action == 'z':
            moved = jeu.move_up()
        elif action == 's':
            moved = jeu.move_down()
        elif action == 'q':
            moved = jeu.move_left()
        elif action == 'd':
            moved = jeu.move_right()
        elif action == 'quit':
            print("Partie interrompue.")
            break
        else:
            print("⚠️ Commande non reconnue. Utilisez z, q, s, d.")
            continue  # Relance la boucle sans faire pop une nouvelle tuile

        # Si le mouvement est valide, on ajoute une nouvelle tuile
        if moved:
            jeu.add_random_tile()
        else:
            print("👉 Déplacement impossible dans cette direction.")
            print("\n")