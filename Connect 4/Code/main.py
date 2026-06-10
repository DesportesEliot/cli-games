from game import Connect4

def main():
    jeu = Connect4()

    print("Grille :")
    for ligne in jeu.get_grid():
        print(ligne)

    print("Joueur actuel :", jeu.get_current_player())

    jeu.switch_player()

    print("Après changement :", jeu.get_current_player())

if __name__ == "__main__":
    main()