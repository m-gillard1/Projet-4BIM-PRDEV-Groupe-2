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

#############################################################
### Récupérer les images utilisées par l'IHM et leur note ###
#############################################################

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
    encoded_image_list=[]
    count_1=0

    for image in os.listdir(path_im_vague) :
        encoded_image=Autoencoder_to_use.NumpyEncoding(path_im_vague+image)
        encoded_image_list.append(encoded_image)
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

    count_2=0
    image_note_list=[]

    for numpy in encoded_image_list:
            flatten_numpy_image=np.array(numpy.flatten())
            taille_vecteur_image =flatten_numpy_image.size
            note_numpy = np.zeros(taille_vecteur_image)
            print(note_numpy)
            print(count_2)
            print(note)
            note_numpy[0] = note[count_2]
            note_numpy [1:taille_vecteur_image] = None
            element=np.array([note_numpy,flatten_numpy_image])
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
        image_reshape=image_numpy.reshape(1,256,32,32) # remettre sous forme matricielle
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

    taux_cross_over=0.8

    encoded_image_list=encoded_image(path_im_vague)
    image_note_list=data_structure_note_image(encoded_image_list,note)

    # boucle pour extraire les favoris
    print(image_note_list)
    img_fav=[]
    for img in image_note_list :
        if (img[0][0] >= 7) :
            img_fav.append(img[1])
    print(img_fav)

    new_image_encoded=algo_genetique_avec_note(img_fav, taux_cross_over)
    list_path_img=[]
    list_path_img=sauv_img(new_image_encoded,path_result_vague)

    return list_path_img



if __name__=='__main__':

    #main_loop(8)

    note_list=creation_list_note(12)
    print(IHM_loop(1,note_list))
