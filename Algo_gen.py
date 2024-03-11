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
