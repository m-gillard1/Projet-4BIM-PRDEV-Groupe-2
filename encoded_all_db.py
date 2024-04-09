import Autoencoder_to_use

import numpy as np
import os
from PIL import Image


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

###################################################
### ficheir avec les vecteurs de toute la DB ###
###################################################
def encoded_in_file(list_DB_, encoded_data_):
    with open(encoded_data_, 'w') as fichier:
        for vecteur in list_DB_:
            ligne = ' '.join(str(element) for element in vecteur)
            print(ligne)
            fichier.write(ligne + '\n')
            #fichier.write(vecteur+ '\n')

# # Exemple de vecteurs
# vecteurs = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Nom du fichier de sortie
# nom_fichier = "vecteurs.txt"
#
# # Appel de la fonction pour sauvegarder les vecteurs dans le fichier
# sauvegarder_vecteurs_dans_fichier(list_DB,"encoded_data.txt")
#


##### MAIN ##########
print('encoding...')
list_DB=encoded_test_db()
print('writing....')
encoded_in_file(list_DB,"encoded_data.txt")
