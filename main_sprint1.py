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

nb_image_par_vague=12
numero_vague=1
path_im_vague=("C:/Users/auror/Downloads/SPRINT1/image_vague_"+str(numero_vague)+"/")
path_result_vague =("C:/Users/auror/Downloads/SPRINT1/image_vague_"+str(numero_vague+1)+"/")
taux_cross_over=0.3

######################
### Exécuter l'IHM ###
######################
# Martin Théo

#############################################################
### Récupérer les images utilisées par l'IHM et leur note ###
#############################################################

def creation_list_note(nb_image_par_vague) :
    # liste de note aléatoire en attendant lien fonctionnel avec l'IHM
    note = np.zeros(nb_image_par_vague)
    count_0=0
    for count_0 in range(nb_image_par_vague): 
        #print(count_0)
        note[count_0] = int(uniform(0, 11)) # note aléatoire en attendant le lien avec l'IHM
    return note
    
note=creation_list_note(nb_image_par_vague)

##########################
### Encoder les images ###
##########################

encoded_image_list=[]
count=0

for image in os.listdir(path_im_vague) : 
    #print(count)
    #print(image)
    encoded_image=Autoencoder_to_use.NumpyEncoding(path_im_vague+image)
    encoded_image_list.append(encoded_image)
    count+=1

#print(encoded_image_list)

######################################################
### Récupérer les .npy en sortie de l'autoencodeur ###
######################################################
# Aurore, Selma

###############################################
### Récupérer les notes en sortie de l'IHM ###
###############################################

# Aurore, Martin, Théo

###########################################################################################################
### Créer structure de données pour l'algorithme génétique [[[float note],[np.array image encodée]],[]] ###
###########################################################################################################

count=0
image_note_list=[]
for numpy in encoded_image_list:

        flatten_numpy_image=np.array(numpy.flatten())
        taille_vecteur_image =flatten_numpy_image.size
        note_numpy = np.zeros(taille_vecteur_image)
        note_numpy[0] = note[count]
        #print(note[count])
        #print(count)
        note_numpy [1:taille_vecteur_image] = None
        element=np.array([note_numpy,flatten_numpy_image])
        image_note_list.append(element)
        count+=1

#print(image_note_list)

#########################################
### Algorithme génétique (cross over) ###
#########################################
        
## pour test        
#image_note_list = [[[3, None],[7, 2]], [[1, None],[9, 5]], [[4, None], [6, 1]], [[2, None], [8, 3]]]
image_after_algo_list=Algo_gen.one_loop(image_note_list,taux_cross_over)

new_image_encoded=[]
count_3=0

## création de la liste avec uniquement les numpy a décoder pour la prochaine vague
for image in image_after_algo_list :
    new_image_numpy=image[1]
    image_reshape=new_image_numpy.reshape(1,256,32,32)
    #print(type(image_reshape[0][1][1][1]))
    new_image_encoded.append(image_reshape)
    count_3+=1
    #print(count_3)



#########################################################################
### Décoder les nparray obtenus en image + sauvegarde dans un dossier ###
#########################################################################
count_4=0
for numpy in new_image_encoded : 
    count_4+=1
    image_decoded=Autoencoder_to_use.NumpyDecoding(numpy)
    image_decoded.save(path_result_vague+str(count_4)+'.png')
    #print(count_4)



##############################################
### Retourner le nouveau pool de 12 images ###
##############################################
