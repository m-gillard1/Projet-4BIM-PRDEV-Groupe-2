import Autoencoder_to_use

import numpy as np
import os
from PIL import Image
import pickle


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


###################################################
### encoder toutes les images de la db test ###
###################################################

def encoded_test_db():

    """
    retourne la list de toutes les images du jeu de test encodée
    """
    list_DB=encoded_image("data/")
    return list_DB



##### MAIN ##########
print('encoding...')
list_DB=encoded_test_db()
print('writing....')

# Sauvegarde de la liste
with open('liste.pkl', 'wb') as f:
    pickle.dump(list_DB, f)


## Verification
print("openning")

# Chargement de la liste
with open('liste.pkl', 'rb') as f:
    ma_liste_chargee = pickle.load(f)

print(list_DB[0])
print(ma_liste_chargee[0])
