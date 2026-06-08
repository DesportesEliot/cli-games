from game import Game2048

def main():
    print("=== Bienvenue dans 2048 ===")
    
    jeu = Game2048()
    jeu.add_random_tile()
    jeu.add_random_tile()

    for ligne in jeu.get_grid():
        print(ligne)

if __name__ == "__main__":
    main()