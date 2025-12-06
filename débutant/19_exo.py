#!/usr/bin/env python3
# Créé par Paul Scoazec le 04/12/2025

from random import randint

def pierre_feuille_ciseaux():
    """
    Simulation du célèbre jeux Pierre Feuille Ciseaux.
    Règles → La Pierre gagne contre les Ciseaux
            Les Ciseaux gagnent contre la feuille
            La feuille gagne contre la pierre.
    affiche si gangé, perdu ou égalité.

    Returns:
        tuple(int, int) retourne 1 ou 0 pour les participants en fonction du score.

    """
    choix = {
        '1': "Pierre",
        '2': "Feuille",
        '3': "Ciseaux",
    }

    message = ("""
Faites le choix entre : 
1) Pierre
2) Feuille
3) Ciseaux

q | Q ) Exit
h ) help
""")
    print(message)
    while True:
        saisie_user = input('-> ')
        match saisie_user:
            case 'q' | 'Q':
                exit(0)
            case 'h' | 'H':
                print(message)
            case '1' | '2' | '3':
                break
            case _:
                print("Saisi incorrecte, je n'ai pas compris votre choix.\n")

    choix_ia = choix.get(str(randint(1,3)))
    choix_joueur = choix.get(saisie_user)

    msg_equal = "égalité !"
    msg_win = "Vous avez gagné ! "
    msg_lose = "perdu..."

    print(f"Vous avez choisi {choix_joueur} et l'ordinateur à choisi... {choix_ia} !")

    match choix_joueur:
        case "Pierre":
            if choix_ia == "Feuille":
                print(msg_lose)
                compteur_ia, compteur_joueur = 1, 0
            elif choix_ia == "Ciseaux":
                print(msg_win)
                compteur_ia, compteur_joueur = 0, 1
            else:
                print(msg_equal)
                compteur_ia, compteur_joueur = 0, 0
        case "Feuille":
            if choix_ia == "Pierre":
                print(msg_win)
                compteur_ia, compteur_joueur = 0, 1
            elif choix_ia == "Ciseaux":
                print(msg_lose)
                compteur_ia, compteur_joueur = 1, 0
            else:
                print(msg_equal)
                compteur_ia, compteur_joueur = 0, 0
        case "Ciseaux":
            if choix_ia == "Pierre":
                print(msg_lose)
                compteur_ia, compteur_joueur = 1, 0
            elif choix_ia == "Feuille":
                print(msg_win)
                compteur_ia, compteur_joueur = 0, 1
            else:
                print(msg_equal)
                compteur_ia, compteur_joueur = 0, 0

    return compteur_ia, compteur_joueur

def affichage(ia: int, joueur: int, init_ia: int, init_joueur: int):
    print('\n', 50 * "=")
    print(f"score de l'ia : {ia} ", end="")
    print(f"score joueur : {joueur}")
    print('\n', 50 * "=")
    if ia >= 99 or joueur >= 99:
        exit(0)


def main():
    init_ia, init_joueur = 0, 0

    while True:
        var_ia, var_joueur = pierre_feuille_ciseaux()
        init_ia += var_ia
        init_joueur += var_joueur
        print('\n', 50 * "=")
        print(f"        score de l'ia : {init_ia} ", end="")
        print(f"score joueur : {init_joueur} ", end="")
        print('\n', 50 * "=")
        if init_ia >= 99 or init_joueur >= 99:
            exit(0)

if __name__ == "__main__":
    main()