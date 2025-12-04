#!/usr/bin/env python3
# Créé par Paul Scoazec le 04/12/2025

def check_multiple(max_num: int) -> list[int]:
    """
    Renvoie la liste des multiples de trois et de cinq des nombres situés
    entre zéro et max_num.
    Args:
        max_num (int): le nombre maximum qui sera vérifié.

    Returns:
        list: La liste de tous les multiples de trois et de cinq entre zéro
         et max_num.

    """

    exit_list = list()

    for i in range(0, max_num + 1):
        if i % 3 == 0 or i % 5 == 0:
            exit_list.append(i)

    return exit_list

def main():

    while True:
        try:
            user_entry = int(input("Entrer un nombre : "))
        except ValueError as e:
            print(f"Saisir un nombre entier : {e}\n")
        else:
            break

    print(f"La somme des nombre multiple de 3 et de 5 entre O et {user_entry} est de {sum(check_multiple(user_entry))}")

if __name__ == "__main__":
    main()