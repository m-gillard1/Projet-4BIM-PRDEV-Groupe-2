#Importation de librairies
from random import *
import math
import numpy as np
import statistics
import os

## n'est pas utile dans la version sans note
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



    # Trier la liste de listes selon la note de chaque image
    sorted_image_list = sorted(image_list, key=lambda x: x[0][0], reverse=True)

    return sorted_image_list




def cross_over_avec_note(best_image_list, Tc):
    """
    Fait des croisements entre vecteurs d'image afin d'obtenir un nouveau vecteur qui sera transformé en image.

    Paramètres :
    ----------
    best_image_list: list
        list de vecteurs comprenant la note de l'image et le vecteur issue de celle-ci pour les meilleures images

    Tc: float
        Taux de croisement.

    Retourne :
    ---------
    new_P : list
        Liste contenant les vecteurs d'images + note ayant ou non subis des croisement
    """
    new_P = np.copy(best_image_list)

    if len(new_P)>6 :
        new_P=new_P[:6] ## si plus de 6 favoris on ne prend que les 6 premiers soit les 6 meilleurs

    print(new_P)
    print(len(new_P))
    for i in range(0, len(new_P)):
        if random() < Tc:
            #print('cross over !! ',i)
            indc = randint(0, len(new_P) - 1) # choisi l'image avec laquelle il va échanger
            posc = randint(0, len(new_P[i][1]) - 1) # choisi a quelle position du vecteur on coupe
            #print(indc)
            #print(posc)
            #print(len(new_P[i][1]))
            tmp = new_P[i][1][posc:len(new_P[i][1])]
            #print(tmp)
            new_P[i][1][posc:len(new_P[i][1])] = new_P[indc][1][posc:len(new_P[i][1])]
            new_P[indc][1][posc:len(new_P[i][1])] = tmp

    return new_P

def cross_over_sans_note(best_image_list, Tc):
    """
    Fait des croisements entre vecteurs d'image.

    Paramètres :
    ----------
    best_image_list: list
        list de vecteurs comprenant le vecteur issue de l'image pour les meilleures images

    Tc: float
        Taux de croisement.

    Retourne :
    ---------
    new_P : list
        Liste contenant les vecteurs d'images (sans note) ayant ou non subis des croisement
    """
    new_P = np.copy(best_image_list)

    for i in range(0, len(new_P)):
        if random() < Tc:
            #print('cross over !! ',i)
            indc = randint(0, len(new_P) - 1) #choisi l'image avec laquelle il va échanger entre 0 et 10
            posc = randint(0, len(new_P[i]) - 1) # choisi a quelle position du vecteur on coupe entre 0 et 20
            #print(indc)
            #print(posc)
            #print(len(new_P[i][1]))
            tmp = new_P[i][posc:len(new_P[i])]
            #print(tmp)
            new_P[i][posc:len(new_P[i])] = new_P[indc][posc:len(new_P[i])]
            new_P[indc][posc:len(new_P[i])] = tmp

    return new_P



def mutations(best_image_list, Tm) :
    """
    Fait des mutations sur les vecteurs d'image, rajoute +1 a certaines éléments du vecteur aléatoirement

    Paramètres :
    ----------
    best_image_list: list
        list de vecteurs comprenant le vecteur issue de l'image pour les meilleures images

    Tm: float
        Taux de mutations

    Retourne :
    ---------
    new_P : list
        Liste contenant les vecteurs d'images + note ayant ou non subis des croisement
    """

    new_P = np.copy(best_image_list)

    if len(new_P)>6 :
        new_P=new_P[:6] ## si plus de 6 favoris on ne prend que les 6 premiers soit les 6 meilleurs

    for i in range(0, len(new_P)):
        if random() < Tm:
            img_muta = new_P[i][1]

            for i in range(len(img_muta)) :
                if random() < Tm :
                    img_muta[i]=img_muta[i]+1

    return new_P


def one_loop_avec_note(image_list, Tc, Tm):
    """
    Trie la population, choisit les meilleurs images sur lesquelles vont etre faites de cross over.

    Paramètres :
    ----------
    image_list: list
        list de vecteur comprenant la note de l'image et le vecteur issue de celle-ci

    Tm: float
        Taux de mutation

    Tc: float
        Taux de croisement.

    Retourne :
    ---------
    list: Liste contenant les nouvelles images modifiées par le croos over
    """

    # Trie la population de façon à ce que les 6 premiers soient les 6 meilleurs
    sorted_image_list = pop_sort(image_list)
    print('sorted popu')
    print(sorted_image_list)

    # Applique des croisements aux meilleurs vecteurs
    popu_cross = cross_over_avec_note(sorted_image_list, Tc)
    print("cross")
    print(popu_cross)

    # Applique des mutations aux meilleurs vecteurs
    popu_muta = mutations(sorted_image_list, Tm)
    print("muta")
    print(popu_muta)

    # Crée une nouvelle population en fusionnant les vecteurs cross et les vecteurs mutés
    pop = np.concatenate((popu_cross, popu_muta), axis=0)
    print("tot")
    print(pop)
    return pop



###### MAIN #######


if __name__=='__main__':
    #Test de la fonction pop_sort(image_list)
    image_note_list = [[[3, None],[7, 2]], [[1, None],[9, 5]], [[4, None], [6, 1]], [[2, None], [8, 3]], [[2, None], [8, 3]], [[2, None], [8, 3]], [[2, None], [8, 3]], [[2, None], [8, 3]]]
    print('test pop_sort - ok ')
    print(pop_sort(image_note_list))

    #Test de la fonction lowest_cost_pop(sorted_image_list)
    print('test lowest cost - ok ')
    print(lowest_cost_pop(pop_sort(image_note_list)))

    # Test de la fonction cross_over_avec_note(best_image_list, Tc)
    print('test cross over avec note :')
    print(cross_over_avec_note(image_note_list,0.1))

    # Test de la fonction mutations
    print('test mutations:')
    print(mutations(image_note_list,0.8))

    image_list = [ [7, 2], [9, 5], [6, 1], [8, 3] ]
    # Test de la fonction cross_over_sans_note(best_image_list, Tc)
    print('test cross over sans note:')
    print(cross_over_sans_note(image_list,0.6))
