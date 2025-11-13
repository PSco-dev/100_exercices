#!/usr/bin/env python3
#coding: utf-8
from pprint import pprint

def palindrome(saisi:str) -> bool:
    """
    Cette fonction vérifie si la chaîne donnée est un palindrome

    Args:
        saisi (str): Chaine de caractère à vérifier.

    Returns:
        result (bool): True si le texte est un palindrome, sinon False
    """
    # Mise au propre de la chaine en entrée
    saisi_verif = "".join( car.lower() for car in saisi if car.isalnum())

    # Vérification du palindrome
    result = True if saisi_verif == saisi_verif[::-1] else False
    
    return result

print(palindrome("lo  2 3!((ol"))
print(help(pprint))