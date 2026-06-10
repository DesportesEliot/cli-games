import random
import os
import sys

RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Gestion de la capture instantanée du clavier (Cross-platform)
try:
    import msvcrt
    def get_key():
        """Capture une touche sous Windows (les flèches renvoient deux octets)."""
        ch = msvcrt.getch()
        if ch in (b'\x00', b'\xe0'):  # Touche spéciale (ex: flèches)
            ch2 = msvcrt.getch()
            if ch2 == b'K': return 'left'
            if ch2 == b'M': return 'right'
        if ch in (b'\r', b'\n'):
            return 'enter'
        try:
            return ch.decode('utf-8').lower()
        except UnicodeDecodeError:
            return None
except ImportError:
    import tty
    import termios
    def get_key():
        """Capture une touche sous Linux / macOS."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':  # Séquence d'échappement (ex: flèches)
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'D': return 'left'
                    if ch3 == 'C': return 'right'
            if ch in ('\r', '\n'):
                return 'enter'
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


class Connect4:
    def __init__(self):
        """
        Initialise une partie de Puissance 4.
        """
        # Grille 6x7 remplie de 0
        self.grid = [[0 for _ in range(7)] for _ in range(6)]

        # Joueur courant
        self.current_player = "X"

        self.winning_cells = []

    def get_grid(self):
        """Retourne la grille."""
        return self.grid

    def get_current_player(self):
        """Retourne le joueur actuel."""
        return self.current_player

    def switch_player(self):
        """Change de joueur : X <-> O"""
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def clear_screen(self):
        """Nettoie l'écran du terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def afficher_grille(self, col_curseur=-1):
       """
          Affiche la grille avec couleurs ANSI et caractères Unicode.
         """

       if col_curseur != -1:
         print("  " + "  " * col_curseur + "▼")
       else:
          print()

       print("┌─┬─┬─┬─┬─┬─┬─┐")

       for i, row in enumerate(self.grid):

         ligne = []

         for j, cell in enumerate(row):

            if (i, j) in self.winning_cells:
                ligne.append(f"\033[92m●{RESET}")  # Vert pour l'alignement gagnant

            elif cell == "X":
                ligne.append(f"{RED}●{RESET}")

            elif cell == "O":
                ligne.append(f"{YELLOW}●{RESET}")

            else:
                ligne.append(" ")

         print("│" + "│".join(ligne) + "│")

         if i < 5:
            print("├─┼─┼─┼─┼─┼─┼─┤")

       print("└─┴─┴─┴─┴─┴─┴─┘")
       print(" 0 1 2 3 4 5 6")
  
    def placer_jeton(self, colonne):
        """
        Place le jeton du joueur actuel dans la colonne choisie.
        """
        if colonne < 0 or colonne >= 7:
            return False

        for ligne in range(5, -1, -1):
            if self.grid[ligne][colonne] == 0:
                self.grid[ligne][colonne] = self.current_player
                return True
        return False
    
    def verifier_victoire(self):
        joueur = self.current_player

         # Vérification horizontale
        for ligne in range(6):
          for col in range(4):
            if (
                self.grid[ligne][col] == joueur and
                self.grid[ligne][col + 1] == joueur and
                self.grid[ligne][col + 2] == joueur and
                self.grid[ligne][col + 3] == joueur
            ):
                self.winning_cells = [
                    (ligne, col),
                    (ligne, col + 1),
                    (ligne, col + 2),
                    (ligne, col + 3)
                ]
                return True

         # Vérification verticale
        for ligne in range(3):
         for col in range(7):
            if (
                self.grid[ligne][col] == joueur and
                self.grid[ligne + 1][col] == joueur and
                self.grid[ligne + 2][col] == joueur and
                self.grid[ligne + 3][col] == joueur
            ):
                self.winning_cells = [
                    (ligne, col),
                    (ligne + 1, col),
                    (ligne + 2, col),
                    (ligne + 3, col)
                ]
                return True

         # Vérification diagonale descendante (\)
        for ligne in range(3):
         for col in range(4):
            if (
                self.grid[ligne][col] == joueur and
                self.grid[ligne + 1][col + 1] == joueur and
                self.grid[ligne + 2][col + 2] == joueur and
                self.grid[ligne + 3][col + 3] == joueur
            ):
                self.winning_cells = [
                    (ligne, col),
                    (ligne + 1, col + 1),
                    (ligne + 2, col + 2),
                    (ligne + 3, col + 3)
                ]
                return True

         # Vérification diagonale montante (/)
        for ligne in range(3, 6):
         for col in range(4):
            if (
                self.grid[ligne][col] == joueur and
                self.grid[ligne - 1][col + 1] == joueur and
                self.grid[ligne - 2][col + 2] == joueur and
                self.grid[ligne - 3][col + 3] == joueur
            ):
                self.winning_cells = [
                    (ligne, col),
                    (ligne - 1, col + 1),
                    (ligne - 2, col + 2),
                    (ligne - 3, col + 3)
                ]
                return True

        return False

    def verifier_match_nul(self):
        """Vérifie si la grille est pleine."""
        for ligne in self.grid:
            if 0 in ligne:
                return False
        return True

    def jouer(self):
        """
        Boucle de jeu principale modifiée.
        Remplacement de input() par un déplacement de curseur en temps réel.
        """
        colonne_actuelle = 3 # On commence au milieu de la grille (colonne 3)
        msg_status = ""

        while True:
            self.clear_screen()
            print("=== PUISSANCE 4 — MODE ARCADE ===")
            print(f"Joueur actuel : {self.current_player}")
            print("Utilisez ◄ et ► pour vous déplacer, ENTRÉE pour jouer, 'q' pour quitter.")
            
            if msg_status:
                print(msg_status)
                msg_status = "" # Réinitialisation après affichage
            else:
                print()

            # On affiche la grille en lui passant la colonne sur laquelle se trouve le joueur
            self.afficher_grille(colonne_actuelle)

            # Attente de la saisie d'une touche (bloquant mais instantané, pas besoin d'Entrée)
            touche = get_key()

            if touche == 'left':
                colonne_actuelle = max(0, colonne_actuelle - 1)
            elif touche == 'right':
                colonne_actuelle = min(6, colonne_actuelle + 1)
            elif touche == 'q':
                print("\nPartie interrompue.")
                break
            elif touche == 'enter':
                # Tentative de validation du coup sur la colonne sélectionnée
                if self.placer_jeton(colonne_actuelle):
                    # On vérifie les conditions de fin tout de suite
                    if self.verifier_victoire():
                        self.clear_screen()
                        print("=== FIN DE LA PARTIE ===")
                        self.afficher_grille()
                        print(f"🏆 Félicitations ! Le joueur {self.current_player} a gagné !")
                        break
                    
                    if self.verifier_match_nul():
                        self.clear_screen()
                        print("=== FIN DE LA PARTIE ===")
                        self.afficher_grille()
                        print("🤝 Match nul ! La grille est pleine.")
                        break
                    
                    # Si la partie continue, on passe au joueur suivant
                    self.switch_player()
                else:
                    msg_status = "⚠️ Erreur : La colonne est pleine ! Choisissez un autre endroit."


# --- LANCEMENT ---
if __name__ == "__main__":
    jeu = Connect4()
    jeu.jouer()