
#Importation de librairies
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

def creation_dictionnaire(chemin):
    """
    Fonction qui permet de créer un dictionnaire contenant pour chaque numéro d'individu le nom de toutes les images le concernant ainsi que le nom du fichier ou elles ont été trouvées.
    ------------------------
    Parameters:
          chemin: string
                  Chemin du répertoire contenant les fichiers avec les images non superposées (images initiales).
    ------------------------
    Returns:
          images_par_individu:
          Dictionnaire contenant pour chaque numéro d'individu le nom de toutes les images le concernant ainsi que le nom du fichier ou elles ont été trouvées.

    """
    # Dictionnaire pour stocker les noms d'images pour chaque individu ainsi que le numéro du fichier
    images_par_individu = {}

    # Parcourir les 15 fichiers (fichiers numérotés de 0 à 14 contenant les images non superposées).
    for i in range(15):
        chemin_repertoire_individu = os.path.join(chemin, str(i))

        # Parcourir tous les fichiers dans le répertoire de l'individu
        for fichier in os.listdir(chemin_repertoire_individu):
            # Vérifier si le fichier est une image
            if fichier.endswith(".png"):
                # Extraire le numéro d'individu du nom du fichier
                individual_id = fichier.split('_')[0]

                # Vérifier si l'individu existe déjà dans le dictionnaire
                if individual_id in images_par_individu:
                    # Ajouter le nom de l'image à la liste exstante pour cet individu avec le numéro du fichier
                    images_par_individu[individual_id].append(fichier)
                else:
                    # Création d'une nouvelle liste pour cet individu et ajout du nom de l'image avec le numéro du fichier
                    images_par_individu[individual_id] = [(fichier)]
        return  images_par_individu
