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
#import interface.py

nb_image_par_vague=12
path_im_vague1="C:/Users/auror/Downloads/SPRINT1/image_vague_1"
taux_cross_over=0.3

######################
### Exécuter l'IHM ###
######################
# Martin Théo

#############################################################
### Récupérer les images utilisées par l'IHM et leur note ###
#############################################################
# Martin Théo

# liste de note aléatoire en attendant lien fonctionnel avec l'IHM
note = np.zeros(nb_image_par_vague)
i=0
for i in range(nb_image_par_vague): 
    print(i)
    note[i] = int(uniform(0, 11)) # note aléatoire en attendant le lien avec l'IHM

#print(note)

##########################
### Encoder les images ###
##########################

encoded_image_list=[]
count=0

for image in os.listdir(path_im_vague1) : 
    #print(count)
    #print(image)
    encoded_image=Autoencoder_to_use.NumpyEncoding(path_im_vague1+image)
    encoded_image_list.append(encoded_image)
    count+=1

print(encoded_image_list)

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

# Aurore

#########################################
### Algorithme génétique (cross over) ###
#########################################
        
image_note_list = [[[3, None],[7, 2]], [[1, None],[9, 5]], [[4, None], [6, 1]], [[2, None], [8, 3]]]
print(Algo_gen.one_loop(image_note_list,taux_cross_over))


############################################
### Décoder les nparray obtenus en image ###
############################################
## Thibald



##############################################
### Retourner le nouveau pool de 12 images ###
##############################################
