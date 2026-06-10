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
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = "X"
        self.winning_cells = []
        
        # STORY-04 - Tâche 1 : Système de score
        self.score_j1 = 0  # Score du Joueur X
        self.score_j2 = 0  # Score du Joueur O

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

    def reinitialiser_manche(self):
        """
        Tâche 2 : Réinitialise uniquement la grille et les cellules gagnantes
        pour une nouvelle manche, tout en préservant les scores de session.
        """
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.winning_cells = []
        self.current_player = "X" # Le joueur X recommence la nouvelle manche

    def afficher_grille(self, col_curseur=-1):
        """
        Affiche la grille élargie (façon carrée) pour corriger le ratio du terminal
        et aligne parfaitement le curseur ▼ au centre de la colonne.
        """
        # Formule magique : le centre de la colonne 'c' est exactement à l'index (2 + 4 * c)
        if col_curseur != -1:
            print(" " * (2 + 4 * col_curseur) + "▼")
        else:
            print()

        # Bordure supérieure élargie (3 lignes horizontales par case)
        print("┌───┬───┬───┬───┬───┬───┬───┐")

        for i, row in enumerate(self.grid):
            ligne = []
            for j, cell in enumerate(row):
                if (i, j) in self.winning_cells:
                    token = f"\033[92m●{RESET}"  # Vert pour la victoire
                elif cell == "X":
                    token = f"{RED}●{RESET}"
                elif cell == "O":
                    token = f"{YELLOW}●{RESET}"
                else:
                    token = " "  # Case vide
                
                # On entoure le jeton d'un espace à gauche et à droite pour faire un carré
                ligne.append(f" {token} ")
            
            # On assemble la ligne avec les séparateurs verticaux
            print("│" + "│".join(ligne) + "│")
            
            # Lignes de séparation internes
            if i < 5:
                print("├───┼───┼───┼───┼───┼───┼───┤")

        # Bordure inférieure
        print("└───┴───┴───┴───┴───┴───┴───┘")
        # On espace aussi les numéros du bas pour coller au nouveau design
        print("  0   1   2   3   4   5   6 ")
  
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
        Boucle globale mise à jour.
        Gère les manches successives et l'invite de redémarrage (Tâche 2).
        """
        while True:  # <-- BOUCLE GLOBALE (Sessions / Manches)
            colonne_actuelle = 3 
            msg_status = ""
            manche_terminee = False

            while True:  # <-- BOUCLE DE LA MANCHE EN COURS (Tours)
                self.clear_screen()
                print("=== PUISSANCE 4 — MODE ARCADE ===")
                print(f"SCORES | Joueur X (Rouge) : {self.score_j1} - Joueur O (Jaune) : {self.score_j2}")
                print("-" * 33)
                print(f"Joueur actuel : {self.current_player}")
                print("Utilisez ◄ et ► pour vous déplacer, ENTRÉE pour jouer, 'q' pour quitter.")
                
                if msg_status:
                    print(msg_status)
                    msg_status = "" 
                else:
                    print()

                self.afficher_grille(colonne_actuelle)
                touche = get_key()

                if touche == 'left':
                    colonne_actuelle = max(0, colonne_actuelle - 1)
                elif touche == 'right':
                    colonne_actuelle = min(6, colonne_actuelle + 1)
                elif touche == 'q':
                    print("\nPartie interrompue. Merci d'avoir joué !")
                    return # Quitte définitivement le programme
                elif touche == 'enter':
                    if self.placer_jeton(colonne_actuelle):
                        if self.verifier_victoire():
                            if self.current_player == "X":
                                self.score_j1 += 1
                            else:
                                self.score_j2 += 1
                                
                            self.clear_screen()
                            print("=== FIN DE LA MANCHE ===")
                            print(f"SCORES | Joueur X : {self.score_j1} - Joueur O : {self.score_j2}")
                            self.afficher_grille()
                            print(f"🏆 Félicitations ! Le joueur {self.current_player} a gagné la manche !")
                            manche_terminee = True
                            break # Casse la boucle des tours
                        
                        if self.verifier_match_nul():
                            self.clear_screen()
                            print("=== FIN DE LA MANCHE ===")
                            print(f"SCORES | Joueur X : {self.score_j1} - Joueur O : {self.score_j2}")
                            self.afficher_grille()
                            print("🤝 Match nul ! La grille est pleine.")
                            manche_terminee = True
                            break # Casse la boucle des tours
                        
                        self.switch_player()
                    else:
                        msg_status = "⚠️ Erreur : La colonne est pleine ! Choisissez un autre endroit."

            # Écran de choix de fin de manche
            if manche_terminee:
                print("\n👉 Pressez 'r' pour relancer une manche ou 'q' pour quitter définitivement.")
                while True:
                    choix = get_key()
                    if choix == 'r':
                        self.reinitialiser_manche()
                        break  # Casse la boucle d'attente et remonte au début de la boucle globale
                    elif choix == 'q':
                        print("Merci d'avoir joué !")
                        return  # Ferme définitivement l'application


# --- LANCEMENT ---
if __name__ == "__main__":
    jeu = Connect4()
    jeu.jouer()