#!/usr/bin/env python3
#coding utf-8

class Voiture:
    """
    Cette classe représente une voiture avec des attributs comme la marque,
    le modèle et l'année.
    """
    def __init__(self, marque, modèle, année):
        """
        Le constructeur qui initialise les attributs de la voiture.

        Args:
            marque (str): La marque du voiture (ex: Peugeot, Toyota).
            modèle (str): Le modèle de la voiture (ex: 203).
            année (int): L'année de la voiture (ex: 1996).
        """
        self.marque = marque
        self.modèle = modèle
        self.année = année

    def __str__(self):
        """
        Cette méthode affiche les information de la voiture dans une chaîne formatée.

        Returns (str): chaine de caractère sur trois lignes
        """
        return (
            f"marque : {self.marque}\n"
            f"modèle : {self.modèle}\n"
            f"année : {self.année}"
        )
if __name__ == "__main__":
    ma_voiure = Voiture("Peugoet", "Ford", 1996)
    print(ma_voiure)