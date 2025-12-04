#!/usr/bin/env python3
# Créé par Paul Scoazec le 04/12/2025

def pierre_feuille_ciseaux():
    """
    Simulation du célèbre jeux Pierre Feuille Ciseaux.
    Règles -> La Pierre gagne contre les Ciseaux
            Les Ciseaux gagnent contre la feuille
            La feuille gagne contre la pierre.
    Returns:
        str: chaine de caractère indiquand si "gagné!" ou "perdu..."

    """

    while True:
            try:
                saisi_utilisateur = int(input("""
Faites le choix entre : 
1) Pierre
2) Feuille
3) Ciseaux

-> """))
                if saisi_utilisateur not in [1, 2 ,3]:
                    raise ValueError
            except ValueError as e:
                print(f"Erreur de saisi, Veuillez entrer un nombre entre 1 et 3")
            else:
                print(f"{saisi_utilisateur=}")
                break
        # match saisi_utilisateur:
        #     case 1

def main():
    pass

if __name__ == "__main__":
    pierre_feuille_ciseaux()