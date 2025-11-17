#!/usr/bin/env python3

def demande() -> tuple[int, int]:
    """
    Récupération de deux nombres donnés par l'utilisateur.
    Returns:
        list: Deux floats
    """
    user_entry = list()
    print("veuillez saisir deux nombres entier ou décimaux.\n")
    while len(user_entry) < 2:
        while True:
            try:
                saisi = float(input(f"saisir le nombre n°\
{len(user_entry) + 1} : "))
                user_entry.append(saisi)
                break
            except ValueError as e:
                print(f"Erreur de saisi {type(e).__name__} : {e}.\n\n\
Veuillez insérer un nombre")

    return user_entry[0], user_entry[1]

def addition(nombre1:float, nombre2:float) -> float:
    """
    Additionne deux nombres entre eux
    Args:
        nombre1 (float): nombre 1 :
        nombre2 (float): nombre 2 :

    Returns:
        float: somme des deux entrées
    """
    print(f"\nL'addition égal : {nombre1 + nombre2}")
    return nombre1 + nombre2

def soustraction(nombre1:float, nombre2:float) -> float:
    """
    Soustraction deux nombres entre eux
    Args:
        nombre1 (float): nombre 1 :
        nombre2 (float): nombre 2 :

    Returns:
        float: la soustraction des deux entrées.
    """
    print(f"La soustraction égal : {nombre1 - nombre2}")
    return nombre1 - nombre2

def multiplication(nombre1:float, nombre2:float) -> float:
    """
    Multiplication deux nombres entre eux
    Args:
        nombre1 (float) : nombre 1 :
        nombre2 (float) : nombre 2 :

    Returns:
        float: la multiplication deux nombres entre eux
    """
    print(f"La multiplication égal : {nombre1 * nombre2}")
    return nombre1 * nombre2

def division(nombre1:float, nombre2:float) -> float | None:
    """
    Division deux nombres entre eux
    Args:
        nombre1 (float) : nombre 1 :
        nombre2 (float) : nombre 2 :

    Returns:
        float: la division deux nombres entre eux
    """
    # Gestion des erreurs
    try:
        print(f"La division égal : {nombre1 / nombre2}\n")
        return nombre1 / nombre2
    except ZeroDivisionError as e:
        print(f"PAS DE DIVISION PAR ZERO !! : {e}")

def main():
    nb1, nb2 = demande()
    addition(nb1, nb2)
    soustraction(nb1, nb2)
    multiplication(nb1, nb2)
    division(nb1, nb2)

if __name__ == "__main__":
    main()