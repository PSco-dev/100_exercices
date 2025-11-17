#!/usr/bin/env python3
#coding utf-8

def palindrome(texte: str) -> bool:
    """
    Vérifie qu'une chaîne de caractère est un palindrome'
    Args:
        texte (str): Le texte à vérifier.

    Returns:
        bool: True si texte est palindrome, False sinon.
    """

    # Suppression des caractères non alphanumériques et conversion en minuscule.
    texte_propre = "".join(car.lower() for car in texte if car.isalnum())

    # Vérification si la chaîne inversée est égale à la chaîne d'origine.
    return texte_propre == texte_propre[::-1]

var = palindrome("kaya ----k")
print(var)
