
#Importation de librairies
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

def creation_dictionnaire(chemin):
    """
    Fonction qui permet de créer un dictionnaire contenant pour chaque numéro d'individu le nom de toutes les images le concernant.
    ------------------------
    Parameters:
          chemin: string
                  Chemin du répertoire contenant les fichiers avec les images non superposées (images initiales).
    ------------------------
    Returns:
          images_par_individu:
          Dictionnaire contenant pour chaque numéro d'individu le nom de toutes les images le concernant.

    """
    # Dictionnaire pour stocker les noms d'images pour chaque individu.
    images_par_individu = {}

    # Parcourir les 15 fichiers (fichiers numérotés de 0 à 14 contenant les images non superposées).
    for i in range(15):
        chemin_repertoire_individu = os.path.join(chemin, str(i))

        # Parcourir tous les fichiers dans le répertoire de l'individu.
        for fichier in os.listdir(chemin_repertoire_individu):
            # Vérifier si le fichier est une image
            if fichier.endswith(".png"):
                # Extraire le numéro d'individu du nom du fichier.
                individual_id = fichier.split('_')[0]

                # Vérifier si l'individu existe déjà dans le dictionnaire.
                if individual_id in images_par_individu:
                    # Ajouter le nom de l'image à la liste exstante pour cet individu.
                    images_par_individu[individual_id].append(fichier)
                else:
                    # Création d'une nouvelle liste pour cet individu et ajout du nom de l'image.
                    images_par_individu[individual_id] = [(fichier)]
        return  images_par_individu

def superposition(chemin_2 ,chemin_3, images_par_individu , i, j ):
    """
    Fonction qui permet d'obtenir pour chaque individu une seule image en superposant toutes celles le concernant et qui ajoute les images superposées formées au fur et à mesure dans dans un dossier.
    Parameters:
          chemin_2: string
                  Chemin du répertoire ou l'on veut créer le dossier contenant les images superposées formées.
          chemin_3: string
                  Chemin du du fichier contenant les images concernant les individus i à j-1.
          images_par_individu: dict
                  Dictionnaire contenant pour chaque numéro d'individu le nom de toutes les images le concernant.
          i: int
                  Plus petit numéro d'individu du fichier concerné
          j: int
                  Plus grand numéro d'individu du fichier concerné + 1
    ------------------------
    Returns:
          None

    """
    dossier_superpose = os.path.join(chemin_2, "img_superposees")
    if not os.path.exists(dossier_superpose):
        os.makedirs(dossier_superpose)

    for face in range (i, j):
        canvas = np.zeros((512,512)) # Les images ont une taille 512*512 pixels
        extension = ""
        if (face<10): #Pour les individus dont le numéro est inférieur à 10.
            extension =  str ("0000") + str(face)
        elif (face<100):  #Pour les individus dont le numéro est inférieur à 100.
            extension =  str ("000") + str(face)
        elif (face<1000):  #Pour les individus dont le numéro est inférieur à 1000.
            extension =  str("00") + str(face)
        elif (face<10000):  #Pour les individus dont le numéro est inférieur à 10000.
            extension = str("0")+ str(face)
        elif (face<100000):  #Pour les individus dont le numéro est inférieur à 100000.
            extension = "" +str(face)
        chemin = chemin_3+extension
        #On superpose les images de chaque individu dans un ordre bien défini afin de visualiser tous les éléments distinctement.
        file_names = [
            chemin +"_skin.png" if any("_skin.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_l_brow.png" if any("_l_brow.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_r_brow.png" if any("_r_brow.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_hair.png" if any("_hair.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_hat.png" if any("_hat.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_eye_g.png" if any("_eye_g.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_cloth.png" if any("_cloth.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_r_ear.png" if any("_r_ear.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_l_ear.png" if any("_l_ear.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_ear_r.png" if any("_ear_r.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_mouth.png"  if any("_mouth.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_l_lip.png" if any("_l_lip.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_neck.png" if any("_neck.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_nose.png" if any("_nose.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_r_eye.png" if any("_r_eye.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_u_lip.png" if any("_u_lip.png" in img for img in images_par_individu[extension]) else None,
            chemin + "_l_eye.png" if any("_l_eye.png" in img for img in images_par_individu[extension]) else None,
        ]

        count = 0
        for part in file_names :
            count+=1
            if (part is not None):
                img = cv2.imread(part, cv2.IMREAD_GRAYSCALE) #Lecture de l'image en niveaux de gris
                for i in range(512):
                    for j in range(512):
                        if (img[i, j] != 0):
                            canvas[i, j] = count*13

         # Enregistrer l'image superposée avec le nom de l'individu dans le répertoire approprié
        output_file_name = str(face) + "_superposee.png"
        chemin_fichier_superpose = os.path.join(dossier_superpose, output_file_name)
        cv2.imwrite(chemin_fichier_superpose, canvas)


if __name__ == "__main__":
    #Chemin du répertoire contenant les images non superposées
    chemin = "C:/Users/Selma/Downloads/CelebAMask-HQ/CelebAMask-HQ/CelebAMask-HQ-mask-anno"
    #Dictionnaire
    images_par_individu=creation_dictionnaire(chemin)
    #print(images_par_individu)
