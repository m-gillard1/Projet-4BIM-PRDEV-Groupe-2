#Importation de librairies
from random import *
import math
import numpy as np
import statistics
import os

def pop_sort(image_list):

    """
    Trie les vecteurs en fonction de leur cout de la meilleure à la moins bonne note.

    Paramètres :
    ----------
    image_list: list
        list de vecteur comprenant la note de l'image et le vecteur issue de celle-ci

    Retourne :
    ---------
    sorted_image_list: image_list ordonnées par ordre decroissant selon les notes (couts)

    """

    sorted_image_list = []



    # Trier la liste de listes selon le deuxième élément de chaque sous-liste
    sorted_image_list = sorted(image_list, key=lambda x: x[0][0], reverse=True)

    return sorted_image_list

def lowest_cost_pop(sorted_image_list):
    """
    Retourne la première moitié de vecteurs (ceux ayant le plus faible cout = la meilleure note).

    Paramètres :
    ----------

    sorted_image_list: list
        image_list ordonnées par ordre decroissant selon les notes (couts)

    Retourne :
    ---------
    low_pop : list
        Listes contenant les images + notes ayant le plus faible cout.

    """
    nombre_image=len(sorted_image_list)
    Ns = nombre_image // 2
    low_pop = sorted_image_list[0:Ns]
    return low_pop
