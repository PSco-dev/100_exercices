#!/usr/bin/env python3
# Créé par Paul Scoazec le 06/12/2025

import random
import string

def demande_user() -> int:
    """
    Demander la longueur du mot de passe souhaité par l'utilisateur.

    Returns:
        int: longueur du mot de passe
    """
    while True:
        try:
            choix_user = int(input("Choix du mot de passe ? \n >> "))
            if not (5 <= choix_user <= 80):
                raise ValueError("valeur hors intervalle. \n")
        except ValueError as e:
            print(f"Saisie incorrecte, nombre entier attendu entre 5 "
                  f"et 80.\n{e}\n")
        else:
            return choix_user

def pass_generator(longueur_du_mot_passe: int=10) -> str:
    """
    Génère un mot de passe d'une longueur égal un la valeur entrée
    en argument.

    Args:
        longueur_du_mot_passe (int) : La longueur du mot de passe choisi
         par l'utilisateur.

    Returns:
        str: le mot de passe généré
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mdp = ""
    for _ in range(longueur_du_mot_passe):
        mdp += random.choice(caracteres)
    return mdp

def main():
    longueur_pass = demande_user()
    mdp = pass_generator(longueur_pass)
    print(mdp)

if __name__ == "__main__":
    main()