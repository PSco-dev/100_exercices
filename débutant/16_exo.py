#!/usr/bin/env python3
# Créé par Paul Scoazec le 22/11/2025

def factoriel(nb:int | float) -> int | float:
    """
    calcule la factoriel d'un nombre.
    Args:
        nb (int): nombre dont la factoriel sera calculé.

    Returns:
        int: Le factoriel calculé.

    """
    if nb == 0 or nb == 1:
        return 1
    return nb * factoriel(nb - 1)

def main():
    # nombre = int(input('nombre : '))
    # print(factoriel(nombre))
    result = factoriel(5)
    print(result)

if __name__ == "__main__":
    main()
