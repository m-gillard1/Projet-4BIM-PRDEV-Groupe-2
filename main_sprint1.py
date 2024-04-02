##################################
####### MAIN pour sprint 1 #######
##################################

#######################################################################
### Importer les fonctions de l'autoencodeur et de l'algo génétique ###
#######################################################################

import Algo_gen
import Autoencoder_to_use

from random import *
import numpy as np
import os
from PIL import Image
#import interface.py

######################
### Exécuter l'IHM ###
######################
# Martin Théo

############################
### Récupérer les notes ###
###########################

#inutile
def creation_list_note(nb_image_par_vague) :
    # liste de note aléatoire en attendant lien fonctionnel avec l'IHM
    note = np.zeros(nb_image_par_vague)
    count_0=0
    for count_0 in range(nb_image_par_vague):
        #print(count_0)
        note[count_0] = int(uniform(0, 11)) # note aléatoire en attendant le lien avec l'IHM
    return note

##########################
### Encoder les images ###
##########################

def encoded_image (path_im_vague) :
    """
    entree : lien vers le dossier contenant les images de la vagues
    sortie : list de vecteur correspondnat aux images encodées
    """
    encoded_image_list=[]
    count_1=0

    for image in os.listdir(path_im_vague) :
        encoded_image=Autoencoder_to_use.NumpyEncoding(path_im_vague+image)
        ## flatten here or in data_structure_note_image
        flatten_numpy_image=np.array(encoded_image.flatten())
        encoded_image_list.append(flatten_numpy_image)
        count_1+=1

    return encoded_image_list

###############################################
### Récupérer les favoris en sortie de l'IHM ###
###############################################

# Aurore, Martin, Théo

###########################################################################################################
### Créer structure de données pour l'algorithme génétique [[[float note],[np.array image encodée]],[]] ###
###########################################################################################################

### on utilise directement ceux labelisés comme favoris plus besoin de note
def data_structure_note_image(encoded_image_list, note) :
    """
    entree : list de vecteur des images encodee et list des notes dans l'ordre corresponant à la liste de taille_vecteur_image
    sortie : list contenant pour chaque image une list avec 2 vecteurs : le 1er element du 1er vecteur contient la note puis le
        reste du vecteur contient des Nan (afin d'avoir un vecteur de la meme taille que l'image encodée) et le 2e vecteur correspond à l'image encodée
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
            element=np.array([note_numpy, numpy]) ##flatten_numpy_image])
            image_note_list.append(element)
            count_2+=1

    return image_note_list

#########################################
### Algorithme génétique (cross over) ###
#########################################

def algo_genetique_sans_note (encoded_image_list, taux_cross_over) :

    image_after_algo_list=Algo_gen.cross_over_sans_note(encoded_image_list,taux_cross_over)

    new_image_encoded=[]
    count_3=0

    ## création de la liste avec uniquement les numpy a décoder pour la prochaine vague
    for image_numpy in image_after_algo_list :
        image_reshape=image_numpy.reshape(1,256,32,32) # remettre sous forme matricielle
        new_image_encoded.append(image_reshape)
        count_3+=1

    return new_image_encoded

#########################################
### Algorithme génétique (cross over) ###
#########################################

def algo_genetique_avec_note (image_note_list, taux_cross_over) :

    image_after_algo_list=Algo_gen.cross_over_avec_note(image_note_list,taux_cross_over)

    new_image_encoded=[]
    count_3=0

    ## création de la liste avec uniquement les numpy a décoder pour la prochaine vague
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

    # verfier si le dossier existe sinon le creer
    if not os.path.exists(path_result_vague):
        # Créez le dossier
        os.makedirs(path_result_vague)

    count_4=0
    List_path=[]

    # enregistrer les images et leur chemin
    for numpy in new_image_encoded :
        count_4+=1
        image_decoded=Autoencoder_to_use.NumpyDecoding(numpy)
        image_decoded.save(path_result_vague+str(count_4)+'.png')
        # pour IHM list des path :
        List_path.append(path_result_vague+str(count_4)+'.png')

    return List_path

#######################################################################
### Fonction pour ajouter des nouveaux visages de la base de donnes ###
#######################################################################

def add_Suspect_from_DB():

    """
    renvoie un chemin vers une images en choisissant un nb_aleatoirement dans la db
    """

    ## extraire les numeros des images ayant deja ete utilisées

    ## aleatoire
    numero = int(uniform(24000, 24030))

    ## avec distances
    # parcourir toutes les images de la DB pour calculer leur distance avec toutes les images du la vague actuelle 3000 x 12

    path=("data/"+ str(numero) +'_superposee.png')


    # chercher une image dans la DB
    return  path #List_new_path # un path vers une new image de la DB

## faire une autre fonction qui encoded toutes les images du test
# supprime une image des qu'elle a ete utilisée


###################################################
### calculer distances entre 2 images en numpy  ###
###################################################

def distance_img(img1, img2):

    """
    prends 2 img sous forme vetorielles
    et renvoie leur ditance euclidienne

    """

    # from scipy.spatial import distance
    # calculate Euclidian distance between vectors
    # dist=distance.euclidean(img1, img2)

    from scipy.spatial.distance import cityblock
    #calculate Manhattan distance between vectors
    dist=cityblock(img1, img2)

    return  dist


###################################################
### encoder toutes les images de la db test ###
###################################################

def encoded_test_db():

    """
    retourne la list de toutes les images du jeu de test encodée
    """
    list_DB=encoded_image("data/")
    return list_DB


###################################################
### trouve l'image la plus proche en distance d'une autre image  ###
###################################################

def img_proche (img1, list_DB):

    """
    prends 1 img sous forme vetorielle
    et renvoie l'image la plus proche dans le jeu de test

    """
    low_dist=1000000
    count=24000
    for img in list_DB :
        dist=distance_img(img,img1)
        #print('distance :'+str(dist))
        if dist<=low_dist :
            low_dist=dist
            nb_image=count
        count+=1
        #print('count: '+str(count))

    return nb_image


###################################################
### trouve l'image la plus loin en distance d'une autre image  ###
###################################################

def img_loin (img1, list_DB):

    """
    prends 1 img sous forme vetorielle
    et renvoie l'image la plus loin dans le jeu de test

    """
    high_dist=0
    count=24000
    for img in list_DB :
        dist=distance_img(img,img1)
        if dist>=high_dist :
            high_dist=dist
            nb_image=count
        count+=1

    return nb_image


######################
### PRINCIPAL LOOP ###
######################

def main_loop (nb_vague) :

    for vague in range(nb_vague) :

        vague=vague+1
        numero_vague=vague

        nb_image_par_vague=12

        path_im_vague=("image_vague_"+str(numero_vague)+"/")
        path_result_vague =("image_vague_"+str(numero_vague+1)+"/")

        taux_cross_over=0.3

        note=creation_list_note(nb_image_par_vague)
        encoded_image_list=encoded_image(path_im_vague)
        #image_note_list=data_structure_note_image(encoded_image_list,note) # pas utile sans note
        new_image_encoded=algo_genetique_sans_note(encoded_image_list, taux_cross_over)
        sauv_img(new_image_encoded,path_result_vague)


################s
### IHM LOOP ###
################

def IHM_loop (numero_vague,note) :

    nb_image_par_vague=12

    path_im_vague=("image_vague_"+str(numero_vague)+"/")
    path_result_vague =("image_vague_"+str(numero_vague+1)+"/")

    taux_cross_over=1

    encoded_image_list=encoded_image(path_im_vague)
    image_note_list=data_structure_note_image(encoded_image_list,note)

    # boucle pour extraire les favoris
    print("image note list")
    print(image_note_list)
    img_fav=[]
    for img in image_note_list :
        if (img[0][0] >= 7) :
            img_fav.append(img)
    print("fav")
    print(img_fav)

    new_image_encoded=algo_genetique_avec_note(img_fav, taux_cross_over)
    list_path_img=[]
    list_path_img=sauv_img(new_image_encoded,path_result_vague)


    nb_new_img_from_db=12-len(list_path_img) # nombre de nouvelles images à ajouter de la base de données
    print(nb_new_img_from_db)
    list_path_complete=list_path_img
    print('avant')
    print(list_path_complete)
    # completer liste path en consequence
    for i in range(nb_new_img_from_db) :
        list_path_complete.append(add_Suspect_from_DB())

    print('apres')
    print(list_path_complete)

    return list_path_complete



if __name__=='__main__':

    #main_loop(8)

    note_list=creation_list_note(12)
    print("note")
    print(note_list)
    print(IHM_loop(1,note_list))


    ### test des distances
    print('encoded....')
    the_list=encoded_test_db()
    print(len(the_list))
    print(the_list[0])
    print('proche')
    print(img_proche(the_list[2], the_list))
    print('loin ')
    print(img_loin(the_list[2], the_list))
