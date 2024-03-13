##################################
####### MAIN pour sprint 1 #######
##################################

#######################################################################
### Importer les fonctions de l'autoencodeur et de l'algo génétique ###
#######################################################################

import Algo_gen
#import Autoencoder_to_use

from random import *
import numpy as np
#import interface.py



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
## Thibald

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
        
# Aurore Selma

############################################
### Décoder les nparray obtenus en image ###
############################################
## Thibald



##############################################
### Retourner le nouveau pool de 12 images ###
##############################################
