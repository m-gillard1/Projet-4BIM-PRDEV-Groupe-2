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

def cross_over(best_image_list, Tc):
    """
    Fait des croisements entre vecteurs d'image.

    Paramètres :
    ----------
    image_list: list
        list de vecteurs comprenant la note de l'image et le vecteur issue de celle-ci

    Tc: float
        Taux de croisement.

    Retourne :
    ---------
    new_P : list
        Liste contenant les vecteurs d'images ayant ou non subis des croisement. // avec ou sans note meme problème qu'avant
    """
    new_P = np.copy(best_image_list) ## image_list ou sorted_image_list ?

    print(new_P)
    print(len(new_P))

    for i in range(0, len(new_P)):
        if random() < Tc:
            #print('cross over !! ',i)
            indc = randint(0, len(new_P) - 1) #choisi l'image avec laquelle il va échanger entre 0 et 10
            posc = randint(0, len(new_P[i][1]) - 1) # choisi a quelle position du vecteur on coupe entre 0 et 20
            #print(indc)
            #print(posc)
            #print(len(new_P[i][1]))
            tmp = new_P[i][1][posc:len(new_P[i][1])]
            #print(tmp)
            new_P[i][1][posc:len(new_P[i][1])] = new_P[indc][1][posc:len(new_P[i][1])]
            new_P[indc][1][posc:len(new_P[i][1])] = tmp

    return new_P

def one_loop(image_list, Tc):
    """
    Calcule la moyenne des couts, le cout minimum et definit la population finale de vecteurs.

    Paramètres :
    ----------
    image_list: list
        list de vecteur comprenant la note de l'image et le vecteur issue de celle-ci

    (Tm: float
        Taux de mutation.)

    Tc: float
        Taux de croisement.

    Retourne :
    ---------
    list: Liste contenant la population dinale de vecteurs.
    """
    nombre_image=len(image_list)
    taille_vect_image=len(image_list[0][1])

    # Trie la population et sélectionne les Ns = N/2 meilleurs vecteurs en fonction du coût
    sorted_image_list = pop_sort(image_list)
    best_popu = lowest_cost_pop(sorted_image_list)

    # Applique (des mutations et /ou) des croisements aux meilleurs vecteurs
    popu_cross = cross_over(best_popu, Tc)

    # Crée une nouvelle population en fusionnant les meilleurs vecteurs et les vecteurs mutés
    popu_final = np.concatenate((popu_cross, best_popu), axis=0)

    pop = popu_final
    return pop

if __name__=='__main__':
    #Test de la fonction pop_sort(image_list)
    image_list = [[[3, None],[7, 2]], [[1, None],[9, 5]], [[4, None], [6, 1]], [[2, None], [8, 3]]]
    print('test pop_sort - ok ')
    print(pop_sort(image_list))

    #Test de la fonction lowest_cost_pop(sorted_image_list)
    print('test lowest cost - ok ')
    print(lowest_cost_pop(pop_sort(image_list)))

    # Test de la fonction cross_over(best_image_list, Tc)
    print('test cross over :')
    print(cross_over(image_list,0.1))
