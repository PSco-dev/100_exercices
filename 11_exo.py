#!/usr/bin/env python3
#coding: utf-8

class Voiture:
    """
    Cette classe représente une voiture avec des attributs comme, la marque,
    le modèle et l'année

    """
    def __init__(self, marque, modèle, année):
        """
        Le constructeur initialise les attributs de la voiture.
        Args:
            marque (str): La marque de la voiture (ex: Toyota, Ford).
            modèle (str): Le modèle de la voiture (ex: 208, Puma).
            année (int): L'année de construction de la voiture (ex: 2024).

        """
        self.marque = marque
        self.modèle = modèle
        self.année = année
    def afficher_infos(self):
        """
        Cette méthode permet d'afficher de manière formatée les informations de la voiture
        """
        print(f"marque : {self.marque}\nmodèle : {self.modèle}\nannée : {self.année}\n")

# Création d'un objet voiture        
ma_voiture = Voiture("Peugeot", "208", 2015)

# Affichage des information sur ma voiture
ma_voiture.afficher_infos()

