#!/usr/bin/env python3
# Créé par Paul Scoazec le 06/12/2025

from random import randint

def find_num():
    nb_random = randint(0, 100)
    count = 0
    while True:
        try:
            saisie_user = int(input("Entrer un nombre entier entre 0 et 100 : \n >>> "))
        except ValueError:
            print(f"Saisie incorrecte, il me faut un nombre entier.\n")
            continue
        else:

            if 0 <= saisie_user <= 100:
                print(f"Saisi out of range 0 - 100\n")

            trop_grand = saisie_user > nb_random
            trop_petit = saisie_user < nb_random
            count += 1

            if trop_grand:
                print(f"trop grand ! \n")
            elif trop_petit:
                print(f"trop petit ! \n")
            else:
                print(f"\n----- BRAVO, vous avez trouvé le nombre {nb_random} en {count} essais ! -----")
                return

def main():
    find_num()

if __name__ == "__main__":
    main()
