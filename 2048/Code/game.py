import random
import os

class Game2048:
    def __init__(self):
        """
        Initialise une nouvelle partie de 2048.
        """
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.score = 0
        self.colors = {
    2: "\033[97m",      # Blanc
    4: "\033[93m",      # Jaune
    8: "\033[91m",      # Rouge clair
    16: "\033[31m",     # Rouge
    32: "\033[35m",     # Magenta
    64: "\033[95m",     # Rose
    128: "\033[92m",    # Vert
    256: "\033[96m",    # Cyan
    512: "\033[94m",    # Bleu
    1024: "\033[34m",   # Bleu foncé
    2048: "\033[33m"    # Or/Jaune foncé
}

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
        Affiche la grille de jeu en texte brut et le score actuel.
        """
        print(f"Score : {self.score}") # Affichage du score
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
        Fusionne les cases identiques adjacentes et met à jour le score.
        """
        resultat = ligne.copy()
        for i in range(len(resultat) - 1):
            if resultat[i] != 0 and resultat[i] == resultat[i + 1]:
                resultat[i] *= 2
                self.score += resultat[i]  # <-- AJOUT : On ajoute les points au score !
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
    
    def clear_screen(self):
         """
         Nettoie le terminal.
          """
         os.system('cls' if os.name == 'nt' else 'clear')
    


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
        msg_erreur = ""

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
            msg_erreur = "⚠️ Commande non reconnue. Utilisez z, q, s, d."

        # On nettoie l'écran ici, juste avant de potentiellement rajouter une tuile et de reboucler   
        jeu.clear_screen()

        # On réaffiche le message de bienvenue en haut pour faire propre
        print("=== BIENVENUE DANS 2048 ===")

        if msg_erreur:
            print(msg_erreur)
            continue

        # Si le mouvement est valide, on ajoute une nouvelle tuile
        if moved:
            jeu.add_random_tile()
        elif action in ['z', 'q', 's', 'd']: # Si on a tapé une bonne touche mais que ça n'a pas bougé
            print("👉 Déplacement impossible dans cette direction.\n")

     