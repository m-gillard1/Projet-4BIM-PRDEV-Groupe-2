
# Projet Informatique : Groupe 2 , 2023/2024

Ce projet a été réalisé par le Groupe 2 (4 BIM) formé par :
- S.KADIRI
- T.CHALAS
- A.LE HOUSSEL
- M.GILLARD
- T.DUCASSE

## Description du Projet

Notre projet vise à créer un logiciel qui permet à l'utilisateur de sélectionner des images parmis une série d'images de portraits robots. Au fur et à mesure de la progression, ces images convergent progressivement vers le portrait de la personne à laquelle l'utilisateur pense.


## Emplacement de la documentation

La documentation a été réalisée grâce à l'outil "Sphinx". Pour y accéder, il faut se rendre dans le dossier "build" puis dans le dossier "html".

  * Pour se rendre sur la page d’accueil, il faut ensuite ouvrir dans un navigateur le fichier "index.html".

  * Une fois sur la page d'accueil vous pouvez sélectionner la documentation qui vous intéresse:
      - Documentation autoencodeur
      - Documentation algorithme génétique
      - Documentation main
      - Documentation interface
      - Mode d'emploi du logiciel

## Emplacement de la base de données

Le jeu de test contient initialement 3000 images mais afin d'alléger le dépot git nous en avons conservé 1000 dans le dossier "data".

## Comment démarrer l'application ?

* Ouvrir un terminal linux
* Taper la commande suivante  : python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps software-project-g2
* Taper python3 pour ouvrir une console python3
* Taper from software_project_g2 import run
* Taper run.run()


Si il y a un éventuel problème concernant les packages :
* Se placer dans le dossier .local/lib/python[version selon votre ordinateur]/site-packages/software_project_g2
* Lancer pip install -r requirements.text
* Taper python3 pour ouvrir une console python3
* Taper from software_project_g2 import interface

Sinon:
* Installer les packages demandés.
* run le fichier "interface.py" en éxécutant "python3 interface.py " dans un terminal linux.

## git

Il faut se mettre sur la branche "final_project" qui est la branche finale de notre projet.
