#####################################################################
#####################################################################
####### Script regroupant algo genetique + encodage decodage  #######
#####################################################################
#####################################################################

#######################################################################
### Importer les fonctions de l'autoencodeur et de l'algo génétique ###
#######################################################################

import Algo_gen
import Autoencoder_to_use

from random import *
import numpy as np
import os
from PIL import Image
import pickle


#############
### Notes ###
#############

def creation_list_note(nb_image_par_vague) :
    """
    Créer une liste de note aléatoire pour permettre de tester nos fonctions sans l'IHM

    Paramètres :
    ----------
    nb_image_par_vague : int
        donne le nombre d'image dans une vague et donc le nombre de note à générer

    Retourne :
    ---------
    note : list
        Liste d'entier qui serviront de note
    """

    # liste de note aléatoire pour tester sans l'IHM
    note = np.zeros(nb_image_par_vague)
    count_0=0
    for count_0 in range(nb_image_par_vague):
        #print(count_0)
        note[count_0] = int(uniform(0, 11)) # note aléatoire le lien sans l'IHM
    return note

# ##########################
# ### Encoder les images ###
# ##########################
#
# def encoded_image (path_im_vague) :
#     """
#     Encode toutes les images de la vague en vecteur grace à l'autoencodeur
#
#     Paramètres :
#     ----------
#     path_im_vague : str
#         lien vers le dossier contenant les images de la vague en cours
#
#     Retourne :
#     ---------
#     encoded_image_list : list
#         list de vecteur correspondant aux images encodées (pas de note)
#     """
#
#     encoded_image_list=[]
#     count_1=0
#
#     for image in os.listdir(path_im_vague) :
#         encoded_image=Autoencoder_to_use.NumpyEncoding(path_im_vague+image)
#         ## flatten here or in data_structure_note_image
#         flatten_numpy_image=np.array(encoded_image.flatten())
#         encoded_image_list.append(flatten_numpy_image)
#         count_1+=1
#
#     return encoded_image_list

##########################
### Encoder les images ###
##########################

def encoded_image (path_list) :
    """
    Encode toutes les images de la vague en vecteur grace à l'autoencodeur

    Paramètres :
    ----------
    path_list !!!!!!!!!!

    Retourne :
    ---------
    encoded_image_list : list
        list de vecteur correspondant aux images encodées (pas de note)
    """

    encoded_image_list=[]
    count_1=0

    for path in path_list :
        encoded_image=Autoencoder_to_use.NumpyEncoding(path)
        ## flatten here or in data_structure_note_image
        flatten_numpy_image=np.array(encoded_image.flatten())
        encoded_image_list.append(flatten_numpy_image)
        count_1+=1

    return encoded_image_list

##############################################################################################################################
### Créer structure de données pour l'algorithme génétique [[[float note, Nan, Nan ... Nan ],[np.array image encodée]],[]] ###
##############################################################################################################################

def data_structure_note_image(encoded_image_list, note) :

    """
    Creation de la structure de données qui va etre utilisée pour l'algorithme genetique soit : une list contenant pour
    chaque image 2 vecteurs de meme taille (taille du vecteur de l'image encodée) un avec la note comme premier élément
    puis Nan et le 2eme vecteur contenant l'image encodée

    Paramètres :
    ----------
    encoded_image_liste : list de vecteur
        list de vecteur des images encodee

    note : list de int
        list de int contenant les notes dans l'ordre corresponant à encoded_image_list

    Retourne :
    ---------
    image_note_list : list
        list contenant pour chaque image une list avec 2 vecteurs : le 1er element du 1er vecteur contient la note puis le
        reste de ce vecteur contient des Nan (afin d'avoir un vecteur de la meme taille que le vecteur de l'image encodée) et le 2e vecteur correspond à l'image encodée
    """

    count_2=0
    image_note_list=[]

    for numpy in encoded_image_list:
            # si flatten here
            #flatten_numpy_image=np.array(numpy.flatten())
            #taille_vecteur_image =flatten_numpy_image.size
            # sinon
            taille_vecteur_image=numpy.size


            note_numpy = np.zeros(taille_vecteur_image)
            print(note_numpy)
            print(count_2)
            print(note)
            note_numpy[0] = note[count_2]
            note_numpy [1:taille_vecteur_image] = None
            element=np.array([note_numpy, numpy])
            image_note_list.append(element)
            count_2+=1

    return image_note_list


#############################
### Algorithme génétique  ###
#############################

def algo_genetique_avec_note (image_note_list, taux_cross_over, taux_mutation) :
    """
    Creer de nouveau vecteur d'image avec le cross over

    Paramètres :
    ----------
    image_note_list : list
        list contenat la note et l'image encodee obtenue par data_structure_note_image

    taux_cross_over : int
        probabilite que le cross over se fasse

    taux_mutation: int
        probabilite que les mutations se fassent

    Retourne :
    ---------
    new_image_encoded : list
        list de vecteur correspondant aux nouvelles images encodées apres cross over (pas de note)
    """

    #image_after_algo_list=Algo_gen.cross_over_avec_note(image_note_list,taux_cross_over) ## si pas de mutation suffit d'appeler juste la focntion cross_over
    image_after_algo_list=Algo_gen.one_loop_avec_note(image_note_list,taux_cross_over, taux_mutation)

    new_image_encoded=[]
    count_3=0

    ## création de la liste avec uniquement les numpy (on enleve les notes) à décoder pour la prochaine vague
    for image_numpy in image_after_algo_list :
        new_image=image_numpy[1]
        image_reshape=new_image.reshape(1,256,32,32) # remettre sous forme matricielle
        new_image_encoded.append(image_reshape)
        count_3+=1

    return new_image_encoded

#########################################################################
### Décoder les nparray obtenus en image + sauvegarde dans un dossier ###
#########################################################################

def sauv_img (new_image_encoded, path_result_vague) :
    """
    décode les nouvelles images obtenues puis les sauvegarde dans un dossier et repertorie les liens,
    ajoute egalement dans ce dossier des nouvelles images issues de l DB

    Paramètres :
    ----------
    new_image_encoded : list
        list des vecteurs des nouvelles images encodées apres cross over (pas de note)

    path_result_vague : str
        lien vers le dossier contenant les nouvelles images crées

    Retourne :
    ---------
    list_path : list de str
        list des chemin vers chacune des nouvelles images d ela vague suivante
    """

    # verfier si le dossier existe sinon le creer
    if not os.path.exists(path_result_vague):
        # Créez le dossier
        os.makedirs(path_result_vague)

    #initialisation
    count_4=0
    List_path=[]

    # enregistrer les images de l'algo genetique et leur chemin
    for numpy in new_image_encoded :
        count_4+=1
        image_decoded=Autoencoder_to_use.NumpyDecoding(numpy) # decoder en image
        image_decoded.save(path_result_vague+str(count_4)+'.png') # sauvegarder dans un dossier
        List_path.append(path_result_vague+str(count_4)+'.png') # list de path a retourner pour l'IHM

    # completer avec des images de la base de données aleatoirement
    nb_new_img_from_db=12-len(List_path) # calcul du nombre de nouvelles images à ajouter de la base de données
    for i in range(nb_new_img_from_db) :
        count_4+=1
        print("compt")
        print(count_4)
        new_img_path=add_Suspect_from_DB() # récupère le path d'un image de la DB
        new_img=Image.open(new_img_path) # récupère au format img
        new_img.save(path_result_vague+str(count_4)+'.png') # sauvegarde l'img dans le dossier de la vague suivante
        List_path.append(path_result_vague+str(count_4)+'.png') # ajout à la liste de path pour l'IHM

    return List_path

#######################################################################
### Fonction pour ajouter des nouveaux visages de la base de donnes ###
#######################################################################

def add_Suspect_from_DB():

    """
    renvoie un chemin vers une images en choisissant un nb_aleatoirement dans la db

    Retourne :
    ---------
    path : str
        chemin vers une image de la DB
    """
    ## extraire les numeros des images ayant deja ete utilisées ?

    numero = int(uniform(25000, 25999)) # nombre aléatoire dans les images à disposition
    path=("data/"+ str(numero) +'_superposee.png') # chemin de l'image

    return  path


# ###################################################
# ### Calculer distances entre 2 images en numpy  ###
# ###################################################
#
# def distance_img(img1, img2):
#
#     """
#     Calcule la distance Manhattan entre 2 vecteurs d'image encodées
#
#     Paramètres :
#     ----------
#     img1 : vector
#         vecteur d'une image encodée
#     img2: vector
#         vecteur d'une image encodée
#
#     Retourne :
#     ---------
#     dist : float
#         distance Manhattan entre 2 images encodées
#     """
#
#     # from scipy.spatial import distance
#     # calculate Euclidian distance between vectors
#     # dist=distance.euclidean(img1, img2)
#
#     from scipy.spatial.distance import cityblock
#     #calculate Manhattan distance between vectors
#     dist=cityblock(img1, img2)
#
#     return  dist
#
#
# ###############################################
# ### encoder toutes les images de la db test ###
# ###############################################
#
# def encoded_test_db():
#     """
#     Retourne la list de toutes les images du dossier encodé
#
#     Cette fonction est longue à faire tourner, nous avons essayé de stocker cela directement
#     dans un fichier à réutiliser ensuite mais ce fichier est trop volumneux pour git
#
#     Retourne :
#     ---------
#     list_DB : list of vectors
#         list des images encodées
#     """
#
#     list_DB=encoded_image("data/")
#     return list_DB
#
#
# ##################################################################
# ### trouve l'image la plus loin en distance d'une autre image  ###
# ##################################################################
#
# def img_loin (img1, list_DB):
#
#     """
#     renvoie l'img a la plus grande distance de img1 dans la list_DB
#
#     Paramètres :
#     ----------
#     img1 : vector
#         vecteur d'une image encodée
#     list_DB : list of vectors
#         list des images encodées
#
#     Retourne :
#     ---------
#     nb_images : int
#         numero de l'image la plus loin
#     """
#
#     high_dist=0
#     count=25000
#     for img in list_DB :
#         dist=distance_img(img,img1)
#         if dist>=high_dist :
#             high_dist=dist
#             nb_image=count
#         count+=1
#
#     return nb_image


################
### IHM LOOP ###
################

def IHM_loop (numero_vague,note,fav_list) :

    """
    A partir du numero de vague et des notes données par l'utilisateur, cette boucle renverra des nouvelles images
    à lui proposer afin de s'approcher au mieux de ces attentes. Ces 12 noooooouvelles images seront issus des favoris
    de la vague precedentes modifiées par l'algorithme genetique (cross over et mutation), de nouvelles images de la DB
    seront également inclus afin d'introduire de nouveaux profils

    Paramètres :
    ----------
    numero_vague : int
        numero de la vague pour savoir ou l'on se situe et quel dossier prendre en comte
    note : list de int
        list des notes qui seront attribuéessss par l'utilisateur

    Retourne :
    ---------
    list_path_img : list de str
        list des chemin vers l'image que l'on proposera à l'utilisateur pour la vague suivante
    """

    nb_image_par_vague=12
    nb_new_img_from_db=0

    ##note=note[len(note)-12:] # prendre en compte uniquement les notes de la dernièere vagues de 12 images
    #print(note)

    ## chemin vers les dossiers avec les images
    path_im_vague=("image_vague_"+str(numero_vague)+"/")
    path_result_vague =("image_vague_"+str(numero_vague+1)+"/")

    taux_cross_over=1 # on met un taux de cross over = à 1 pour obtenir forcement des images modifiées
    taux_mutation=1 # on met un taux de mutation = à 1 pour obtenir forcement des images modifiées


    fav_path=[]
    ## recupérer les favorites
    for fav in fav_list :
        fav_path.append(fav[0]) # recuperer les path des fav pour les encoder
    #print("fav")
    #print(fav_path)

    ## preparer nos images à encodee + associer à la note
    encoded_image_list=encoded_image(fav_path)
    img_note_list=data_structure_note_image(encoded_image_list,note)

    ## sauvegarde des images issues de l'algorithme genetique et des nouvelles provenant de la DB
    new_image_encoded=algo_genetique_avec_note(img_note_list, taux_cross_over,taux_mutation) #### verif structure des donnees si les notes apparaisent encore ou pas
    #print('result algo gene')
    #print(new_image_encoded)
    #print(len(new_image_encoded))
    list_path_img=[]
    list_path_img=sauv_img(new_image_encoded,path_result_vague)

    ###### utile si utilisation des distances
    # ## extraire les images dont les note inf ou = à 2
    # img_0=[]
    # for img in image_note_list :
    #     if (img[0][0] <= 2 ) :
    #         img_0.append(img[1])
    # print("list 0000")
    # print(img_0)
    #
    # ## trouver une images "loin" des images = à 0
    # if img_0!=[]:
    #     # recuperationn de 1000 images encodées
    #     with open('liste.pkl', 'rb') as f:
    #         listDB = pickle.load(f)
    #     for img in img_0 :
    #         numero=img_loin(img[1],listDB)
    #         path=("data/"+ str(numero) +'_superposee.png')
    #         list_path_complete.append(path)
    #         nb_new_img_from_db=nb_new_img_from_db-1
    #         print("path")
    #         print(path)
    #         print("nb img a ajdd")
    #         print(nb_new_img_from_db)

    return list_path_img



if __name__=='__main__':

    note_list=creation_list_note(12) # creation de note pour test sans IHM
    print("note")
    print(note_list) # affichage des notes
    print(IHM_loop(1,note_list))


    # ### test des distances
    # print('encoded....')
    # the_list=encoded_test_db()
    # print(len(the_list))
    # print(the_list[0])
    # print('proche')
    # print(img_proche(the_list[2], the_list))
    # print('loin ')
    # print(img_loin(the_list[2], the_list))
    #
    # print(the_list[0]!=the_list[2])
