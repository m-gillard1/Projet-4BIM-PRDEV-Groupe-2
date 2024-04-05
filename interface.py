import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

#import main_sprint1

########## __FONCTIONS__ ##########

def toggle_fullscreen(event=None):
    """
        Bascule l'application en mode plein écran.

        Parameters:
        event: tkinter.Event: L'événement qui a déclenché l'appel de cette fonction ( par défaut, None).

        Returns:
        None
    """
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

Dico_note ={}
Sus_Being_Dragged = None


class Favori(tk.Button):
    def __init__(self,position, wide,column, row,r,c, **kwargs):
        """
        Permet de spécifier les dimensions de l'encadré contenant une image favorite sur l'interface.

        Parameters:
        position (tuple): Un tuple contenant les coordonnées (x, y) de la position de l'objet.
        size (int): La taille de l'objet, en pixels.
        column (int): La colonne dans laquelle l'objet doit être placé.
        row (int): La ligne dans laquelle l'objet doit être placé.
        **kwargs (dict): Tout argument supplémentaire.

        Attributes:
        wd (int): La largeur de l'objet, en pixels.
        ht (int): La hauteur de l'objet, en pixels.
        large (int): La taille de l'objet agrandie, en pixels.
        photo_image (tkinter.PhotoImage): L'image associée à l'objet.
        note (str): Une note associée à l'objet.
        id (int): L'identifiant unique de l'objet.
        col (int): La colonne dans laquelle l'objet est placé.
        row (int): La ligne dans laquelle l'objet est placé.

        Returns:
        None
        """
        self.wd = wide
        self.ht = int (self.wd*0.43)
        self.large=wide*7
        self.photo_image= None
        self.note=None
        self.id=None
        self.col = column
        self.row=row
        self.c = c
        self.r= r
        self.position= position
    

        super().__init__(best_choices_container_frame,width=self.wd, height = self.ht,compound='top', anchor='center', pady = 20,**kwargs)
        #compound='bottom', anchor='n',

    def Make_favorite (self,id, note, image ):
        """
        Définit une image favorite pour l'objet courant. Elle charge l'image grace à son identifiant `id`, la redimensionne à la taille souhaitée, et l'associe à l'objet.

        Parameters:
        id (str): Identifiant l'image favorite.
        note (str): Une note associée à l'image favorite.
        image (PIL.Image.Image): L'image favorite.

        Returns:
        None
        """
        self.note=note
        self.id=id
        photo = Image.open(self.id)
        photo_resized = photo.resize((self.large, self.large))
        self.photo_image = ImageTk.PhotoImage(photo_resized)
        self.config(height=self.large, width=self.large,image=self.photo_image)
        return

    def Update_Fav (Dico_note):
        """
        Met à jour les images favorites en fonction des notes fournies dans le dictionnaire.

        Parameters:
        Dico_note (dict): Dictionnaire contenant les notes associées aux ID des images.

        Returns:
        None
        """

        sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
        lim = 1
        for i in sorted_id_by_note :
            if lim < 11 :
                if (i[1]>6):
                    path = i[0]
                    #print(path)
                    photo = Image.open(path)
                    photo_resized = photo.resize((Dico_rang_fav[lim].large, Dico_rang_fav[lim].large,))
                    Dico_rang_fav[lim].photo_image = ImageTk.PhotoImage(photo_resized)
                    #print(Dico_rang_fav[lim])
                    Dico_rang_fav[lim].id=path
                    Dico_rang_fav[lim].note=i[1]
                    Dico_rang_fav[lim].config(height=Dico_rang_fav[lim].large,width=Dico_rang_fav[lim].large, image=Dico_rang_fav[lim].photo_image, text=Dico_rang_fav[lim].note , pady = 20)
                    lim+=1

        for j in range (10):
            le_fav = Dico_rang_fav[j+1]
            la_note = sorted_id_by_note[j][1]
            h = le_fav.large
            w = le_fav.large
            if (la_note<7):
                le_fav.note=None
                le_fav.id=None
                name = str(le_fav.winfo_name())
                text_to_print='favori ' +  str (j+1)
                le_fav.config(text=text_to_print, image='',height=le_fav.ht, width=le_fav.wd)

    def get_first_non_fav(dico_sorted):
        """
        Trouve la position du premier élément non favori dans un dictionnaire trié par note.

        Parameters:
        dico_sorted (list): Liste de tuples (ID, note) triés par note.

        Returns:
        int: La position du premier élément non favori.
        """

        pos = 0
        for i in dico_sorted :
            if i[1]>6:
                pos+=1
        return pos

    def Clear_fav (self):
        """
        Efface les informations de l'élément favori en réinitialisant son affichage.

        Parameters:
        self (object): L'instance de l'élément favori.

        Returns:
        None
        """
        self.config(text= str(self.winfo_name()), image='', height=self.large, width=self.large)

    def update_color(self):
        return
    def Ajout_Favori(self):
        return
    
    def selected_suspect_event(self):
        """
        Fonction appelée par les boutons suspects en haut à droite pour sélectionner un suspect.

        Parameters:
        self: Le suspect actuel.

        Returns:
        None
        """
        if (type(self)==Favori):
            
            global suspect_actuel
            suspect_actuel = self
            note_label.config(text = 'Note: ' + str(self.note))
            global suspect_principal
            new_image = Image.open(self.id)
            resized_image = new_image.resize((512, 512))
            self.resized_photo_image = ImageTk.PhotoImage(resized_image)
            suspect_principal.configure(image=self.resized_photo_image)
        


    





class Suspect(tk.Button):
    def __init__(self, master, image_path, note, width, height, row, col, **kwargs):
        """
        Initialise un élément avec une image d’un suspect, une note et des dimensions spécifiées.

        Parameters:
        master: Le frame dans lequel on crée le suspect.
        image_path (str): Le chemin de l'image d’un suspect.
        note (int): La note associée à l'image du suspect.
        width (int): Largeur de l'image du suspect.
        height (int): Hauteur de l'image du suspect.
        **kwargs: Arguments supplémentaires.

        Returns:
        None
        """
        super().__init__(master, **kwargs)
        self.col = col
        self.row= row
        self.note = note
        self.original_border_color = self.cget('highlightbackground')
        self.config(highlightthickness=10)
        self.id = image_path
        global Dico_note
        Dico_note[self.id]= self.note
        photo = Image.open(image_path)
        photo_resized = photo.resize((width, height))
        self.photo_image = ImageTk.PhotoImage(photo_resized)
        self.config(image=self.photo_image, command=self.selected_suspect_event)



    #fonction appelée par les boutons suspects en haut à droite #
    #remplace l'image du suspect selctionné en haut gauche pour le noter ensuite#
    def selected_suspect_event(self):
        """
        Fonction appelée par les boutons suspects en haut à droite pour sélectionner un suspect.

        Parameters:
        self: Le suspect actuel.

        Returns:
        None
        """
        if (type(self)==Suspect):
            global suspect_actuel
            suspect_actuel = self
            note_label.config(text = 'Note: ' + str(self.note))
            global suspect_principal
            new_image = Image.open(self.id)
            resized_image = new_image.resize((512, 512))
            self.resized_photo_image = ImageTk.PhotoImage(resized_image)
            suspect_principal.configure(image=self.resized_photo_image)

       

    def increment_note(self):
        """
        Incrémente la note du suspect actuel s'il est inférieur à 10, met à jour la couleur et les informations.

        Returns:
        None
        """

        global suspect_actuel
        if suspect_actuel.note <10:
            suspect_actuel.note += 1

            suspect_actuel.update_color()
        global Dico_note
        global note_label
        note_label.config(text="Note: "+str(suspect_actuel.note))
        Dico_note[suspect_actuel.id]= suspect_actuel.note
        Favori.Update_Fav(Dico_note=Dico_note)

    def decrement_note(self):
        """
        Décrémente la note du suspect actuel s'il est supérieur à 0, met à jour la couleur et les informations.

        Returns:
        None
        """

        global suspect_actuel
        if suspect_actuel.note >0:
            suspect_actuel.note = suspect_actuel.note - 1
            suspect_actuel.update_color()
        global note_label
        global Dico_note
        Dico_note[suspect_actuel.id]= suspect_actuel.note
        note_label.config(text="Note: "+str(suspect_actuel.note))
        
        print("ICI" +  str(suspect_actuel.note))
        if (suspect_actuel.note==6):
            print("here")
            note_label.config(text="Pas d'image selectionnée")
            suspect_actuel = None
            suspect_principal.configure(image=Image_Instruction)
        Favori.Update_Fav(Dico_note=Dico_note)
        
        

    def garbage(self):
        """
        Réinitialise la note du suspect actuel à 0, met à jour la couleur et les informations.

        Returns:
        None
        """

        global suspect_actuel
        suspect_actuel.note = 0  # Réinitialise la note à 0
        suspect_actuel.update_color()
        global note_label
        note_label.config(text="Note: "+str(suspect_actuel.note))
        global Dico_note
        Dico_note[suspect_actuel.id]= suspect_actuel.note

        Favori.Update_Fav(Dico_note=Dico_note)

    def update_color(self):
        """
        Met à jour la couleur de la bordure du bouton qui encadre l’image d’un suspect en fonction de la note qu’on lui attribue.

        Returns:
        None
        """

        global suspect_actuel

        if suspect_actuel.note >= 9 :
            border_color = "dark green"
        elif suspect_actuel.note >= 7:
            border_color = "green yellow"
        elif suspect_actuel.note > 3:
            border_color = "white"
        elif suspect_actuel.note > 1:
            border_color = "orange"
        else:
            border_color = "red"

        # Définit la couleur de la bordure du bouton
        suspect_actuel.config(highlightbackground=border_color)

    def ranking(self):
        """
        Calcule le classement du suspect actuel en fonction de sa note parmi tous les suspects.

        Returns:
        int: Le classement du suspect actuel.
        """
        rank=1
        rating=suspect_actuel.note
        for notes in Dico_note.values():
            if (rating<notes):
                rank+=1
        return rank

    def Ajout_Favori(self):
        """
        Ajoute le suspect actuel aux favoris si sa note appartient à ]6;10[.

        Returns:
        None
        """
        global suspect_actuel
        rank = suspect_actuel.ranking()
        if (rank<10 and self.note>6):
            #print('favori')
            Favori.Make_favorite(Dico_rang_fav[rank], suspect_actuel.id, suspect_actuel.note, suspect_actuel.photo_image)
        return

### GESTION DU DND ###
def make_draggable_fav(widget):
    widget.bind("<Button-1>", on_fav_drag_start)
    widget.bind("<B1-Motion>", on_fav_drag_motion)
    widget.bind("<ButtonRelease-1>", on_fav_drag_release)

def on_fav_drag_start(event):
    widget = event.widget
    widget.lift()
    container = widget.nametowidget(widget.winfo_parent())
    widget.drag_start_x = event.x
    widget.drag_start_y = event.y
    if(widget.note is not None):
        Favori.selected_suspect_event(widget)
        global Dico_note
        Favori.Update_Fav(Dico_note)

def on_fav_drag_motion(event):
    widget = event.widget
    container = widget.nametowidget(widget.winfo_parent())
    x = widget.winfo_x() - widget.drag_start_x + event.x
    y = widget.winfo_y() - widget.drag_start_y + event.y
    widget.place(x=x, y=y)


def on_fav_drag_release(event):
    widget = event.widget
    widget.grid(row=widget.r, column=widget.c, padx=widget.wd, pady=widget.wd)
    global Dico_note
    
    if (widget.note is not None and widget.note >= 7):
        if (widget.winfo_x()+event.x > 10 and widget.winfo_x()+event.x < 120 and (widget.winfo_y()+event.y)>15 and (widget.winfo_y()+event.y)<155):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[0][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[0][1]
                Favori.Update_Fav(Dico_note)
            

        if (widget.winfo_x()+event.x > 145 and widget.winfo_x()+event.x < 245 and (widget.winfo_y()+event.y)>15 and (widget.winfo_y()+event.y)<155):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[1][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[1][1]
                Favori.Update_Fav(Dico_note)
            

        if (widget.winfo_x()+event.x > 275 and widget.winfo_x()+event.x < 370 and (widget.winfo_y()+event.y)>15 and (widget.winfo_y()+event.y)<155):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[2][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[2][1]
                Favori.Update_Fav(Dico_note)
            
        
        if (widget.winfo_x()+event.x > 400 and widget.winfo_x()+event.x < 495 and (widget.winfo_y()+event.y)>15 and (widget.winfo_y()+event.y)<155):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[3][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[3][1]
                Favori.Update_Fav(Dico_note)
            
        
        if (widget.winfo_x()+event.x > 520 and widget.winfo_x()+event.x < 620 and (widget.winfo_y()+event.y)>15 and (widget.winfo_y()+event.y)<155):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[4][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[4][1]
                Favori.Update_Fav(Dico_note)
            
        
        if (widget.winfo_x()+event.x > 10 and widget.winfo_x()+event.x < 120 and (widget.winfo_y()+event.y)>175 and (widget.winfo_y()+event.y)<314):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[5][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[5][1]
                Favori.Update_Fav(Dico_note)
            
        
        if (widget.winfo_x()+event.x > 145 and widget.winfo_x()+event.x < 245 and (widget.winfo_y()+event.y)>175 and (widget.winfo_y()+event.y)<314):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[6][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[6][1]
                Favori.Update_Fav(Dico_note)
            
        
        if (widget.winfo_x()+event.x > 275 and widget.winfo_x()+event.x < 370 and (widget.winfo_y()+event.y)>175 and (widget.winfo_y()+event.y)<314):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[7][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[7][1]
                Favori.Update_Fav(Dico_note)
            
        
        if (widget.winfo_x()+event.x > 400 and widget.winfo_x()+event.x < 495 and (widget.winfo_y()+event.y)>175 and (widget.winfo_y()+event.y)<314):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[8][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[8][1]
                Favori.Update_Fav(Dico_note)
            
    
        if (widget.winfo_x()+event.x > 520 and widget.winfo_x()+event.x < 620 and (widget.winfo_y()+event.y)>175 and (widget.winfo_y()+event.y)<314):
            sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
            if (sorted_id_by_note[9][1]>=7):
                Dico_note[widget.id] = sorted_id_by_note[9][1]
                Favori.Update_Fav(Dico_note)
            
    



def make_draggable_suspect(widget):
    widget.bind("<Button-1>", on_suspect_drag_start)
    widget.bind("<B1-Motion>", on_suspect_drag_motion)
    widget.bind("<ButtonRelease-1>", on_suspect_drag_release)

def on_suspect_drag_start(event):
    global Sus_Being_Dragged
    widget = event.widget
    widget.lift()
    Sus_Being_Dragged=widget
    container = widget.nametowidget(widget.winfo_parent())
    widget.drag_start_x = event.x
    widget.drag_start_y = event.y
    Sus_Being_Dragged.drag_start_x = event.x
    Sus_Being_Dragged.drag_start_y = event.y
    Suspect.selected_suspect_event(widget)

    
def on_suspect_drag_motion(event):

    global Sus_Being_Dragged
    widget = Sus_Being_Dragged
    container = widget.nametowidget(widget.winfo_parent())

    x = Sus_Being_Dragged.winfo_x() - Sus_Being_Dragged.drag_start_x + event.x
    y = Sus_Being_Dragged.winfo_y() - Sus_Being_Dragged.drag_start_y + event.y
    Sus_Being_Dragged.place(x=x, y=y)
def on_suspect_drag_release(event):
    global Sus_Being_Dragged
    widget = Sus_Being_Dragged
    container = widget.nametowidget(widget.winfo_parent())
    x = round((widget.winfo_x() - widget.drag_start_x + event.x) ) 
    y = round((widget.winfo_y() - widget.drag_start_y + event.y) ) 
    widget.grid(row=widget.row, column=widget.col, padx=photo_width//50, pady=photo_height//50)
    if (x < -100 and x > -900 and y > 350 and y < 800):
        widget.note=7
        global suspect_actuel
        global Dico_note
        global note_label
        note_label.config(text="Note: "+str(suspect_actuel.note))
        Dico_note[suspect_actuel.id]= suspect_actuel.note
        suspect_actuel.Ajout_Favori()
        Favori.Update_Fav(Dico_note=Dico_note)
    ### mettre un suspect à la poubelle
    if (x < -20 and x > -900 and y > 350 and y < 800):
        print()
    Sus_Being_Dragged = None
#fonction appelée par le bouton restart
# réinitialise à l'état d'origine (affichage, contenu des dossiers, numérotation vague, notations)
def Restart_event(event):
    """
    Réinitialise l'application à son état d'origine.

    Parameters:
    event: L'événement déclencheur du redémarrage.
()
    Returns:
    None
    """

    suspect_principal.configure(image=Image_Instruction)
    Start_Over()
    Vague_actuelle=1

def Refresh_event(event):
    """
    Met à jour l'affichage en générant de nouveaux suspects pour la vague actuelle.

    Parameters:
    event: L'événement déclencheur.

    Returns:
    Non
    """

    global Vague_actuelle
    Liste_path = Genere_Suspect(Dico_note, Vague_actuelle)
    Vague_actuelle+=1
    #genere 12 nouvelles images de suspects  "\vague_2\image_1", "\vague2|image2... n"
    suspect_principal.configure(image=Image_Instruction)
    Init_suspects(choices_frame,Liste_path,photo_width,photo_height)
    return

#Dico note est un dictionnaire qui contient en clé les path des images (string) et en value les notes associées aux images (int). Exemple de contenu :
#{'image_vague_1/1.png': 5, 'image_vague_1/2.png': 5, 'image_vague_1/3.png': 5, 'image_vague_1/4.png': 5, 'image_vague_1/5.png': 5, 'image_vague_1/6.png': 5, 'image_vague_1/7.png': 5, 'image_vague_1/8.png': 5, 'image_vague_1/9.png': 5}

#fonction Gene_Suspect :
#genere 12 nouvelles images de suspects dans un dossier nommée vague_n\: Par exemple pour n=2, on veut en sortie 12 images au format .png telles que:  "\vague_2\image_1.png", "\vague_2\image_2.png, ... , "\vague_2\image_11.png "
# return une liste contenant les paths des 12 images
def Genere_Suspect(Dico, Vague_actuelle ):
    """
    Génère 12 nouvelles images de suspects pour une vague donnée.

    Parameters:
    Dico (dict): Dictionnaire contenant les chemins des images et les notes associées.
    Vague_actuelle (int): Le numéro de la vague pour laquelle on génère nouveaux suspects.

    Returns:
    list: Liste contenant les chemins des 12 nouvelles images générées.
    """

    # Parcourir le dictionnaire et afficher chaque clé et valeur
    note_list=[]
    for img, note in Dico.items():
        print(f"{img} a {note} points.")
        note_list.append(note)

    # Génération des nouvelles images :
        # prend en entree le numero de la vague et les notes
        # va chercher les images de la vague correspondante
        # génère les nouvelles images
        # renvoie la liste des path svers les nouvelles images
    #Liste_Path_nouvelle_vague=main_sprint1.IHM_loop(Vague_actuelle, note_list)

    print(Liste_Path_nouvelle_vague)
    return (Liste_Path_nouvelle_vague)


def Init_suspects(choices_container_frame,Liste_img,photo_width,photo_height):
    """
    Initialise les suspects avec leurs images et positions dans l’encadré dédié.

    Parameters:
    choices_container_frame: L’encadré contenant les choix des suspects.
    Liste_img (list): Liste des chemins des images des suspects.
    photo_width (int): Largeur des images des suspects.
    photo_height (int): Hauteur des images des suspects.

    Returns:
    None
    """

    suspect_1 = Suspect(choices_container_frame,Liste_img[0],5,photo_width,photo_height,0,0)
    suspect_1.grid(row=0, column=0, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_1)

    suspect_2 = Suspect(choices_container_frame, Liste_img[1],5,photo_width,photo_height,0,1)
    suspect_2.grid(row=0, column=1, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_2)

    suspect_3 = Suspect(choices_container_frame, Liste_img[2],5,photo_width,photo_height,0,2)
    suspect_3.grid(row=0, column=2, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_3)

    suspect_4 = Suspect(choices_container_frame, Liste_img[3],5,photo_width,photo_height,0,3)
    suspect_4.grid(row=0, column=3, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_4)

    suspect_5 = Suspect(choices_container_frame, Liste_img[4],5,photo_width,photo_height,1,0)
    suspect_5.grid(row=1, column=0, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_5)
    suspect_6 = Suspect(choices_container_frame, Liste_img[5],5,photo_width,photo_height,1,1)
    suspect_6.grid(row=1, column=1, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_6)

    suspect_7 = Suspect(choices_container_frame, Liste_img[6],5,photo_width,photo_height,1,2)
    suspect_7.grid(row=1, column=2, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_7)

    suspect_8 = Suspect(choices_container_frame, Liste_img[7],5,photo_width,photo_height,1,3)
    suspect_8.grid(row=1, column=3, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_8)

    suspect_9 = Suspect(choices_container_frame, Liste_img[8],5,photo_width,photo_height,2,0)
    suspect_9.grid(row=2, column=0, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_9)

    suspect_10 = Suspect(choices_container_frame, Liste_img[9],5,photo_width,photo_height,2,1)
    suspect_10.grid(row=2, column=1, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_10)

    suspect_11 = Suspect(choices_container_frame, Liste_img[10],5,photo_width,photo_height,2,2)
    suspect_11.grid(row=2, column=2, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_11)

    suspect_12 = Suspect(choices_container_frame, Liste_img[11],5,photo_width,photo_height,2,3)
    suspect_12.grid(row=2, column=3, padx=photo_width//50, pady=photo_height//50)
    make_draggable_suspect(suspect_12)

def Init_favori(fav_dim,pad):
    """
    Initialise les éléments favoris avec leurs dimensions et positions dans la grille.

    Parameters:
    fav_dim: La dimension des éléments favoris.

    Returns:
    dict: Dictionnaire contenant les éléments favoris indexés par leur rang.
    """

    fav_1 = Favori(1,fav_dim, 1, 1,0,0)
    fav_1.config(text="favori 1")
    fav_1.grid(row=0, column=0, padx=pad, pady=pad)
    make_draggable_fav(fav_1)

    fav_2 = Favori(2, fav_dim, 1, 2,0,1)
    fav_2.config(text='favori 2')
    fav_2.grid(row=0, column = 1, padx=pad, pady=pad)
    make_draggable_fav(fav_2)

    fav_3 = Favori(3,fav_dim, 1, 3, 0, 2)
    fav_3.config(text="favori 3")
    fav_3.grid(row=0, column=2, padx=pad, pady=pad)
    make_draggable_fav(fav_3)

    fav_4 = Favori(4, fav_dim, 1, 4,0,3)
    fav_4.config(text='favori 4')
    fav_4.grid(row=0, column = 3, padx=pad, pady=pad)
    make_draggable_fav(fav_4)

    fav_5 = Favori(5,fav_dim, 1, 5,0,4)
    fav_5.config(text="favori 5")
    fav_5.grid(row=0, column=4, padx=pad, pady=pad)
    make_draggable_fav(fav_5)

    fav_6 = Favori(6, fav_dim, 1, 6, 1 ,0)
    fav_6.config(text='favori 6')
    fav_6.grid(row=1, column = 0, padx=pad, pady=pad)
    make_draggable_fav(fav_6)

    fav_7 = Favori(7,fav_dim, 1, 7, 1, 1)
    fav_7.config(text="favori 7")
    fav_7.grid(row=1, column=1, padx=pad, pady=pad)
    make_draggable_fav(fav_7)

    fav_8 = Favori(8, fav_dim, 1, 8, 1, 2)
    fav_8.config(text='favori 8')
    fav_8.grid(row=1, column = 2, padx=pad, pady=pad)
    make_draggable_fav(fav_8)

    fav_9 = Favori(9,fav_dim, 1, 9, 1, 3)
    fav_9.config(text="favori 9")
    fav_9.grid(row=1, column=3, padx=pad, pady=pad)
    make_draggable_fav(fav_9)

    fav_10 = Favori(10, fav_dim, 1, 10, 1,4)
    fav_10.config(text='favori 10')
    fav_10.grid(row=1, column = 4, padx=pad, pady=pad)
    make_draggable_fav(fav_10)

    Dico_rang_fav ={1: fav_1,
                2: fav_2,
                3:fav_3,
                4:fav_4,
                5:fav_5,
                6:fav_6,
                7:fav_7,
                8:fav_8,
                9:fav_9,
                10:fav_10}
    return Dico_rang_fav

def Start_Over():
    """
    Réinitialise l'application en remettant la vague actuelle à 1, réinitialisant les suspects et les favoris, et affichant un message par défaut.

    Returns:
    None
    """

    Vague_actuelle = 1
    Init_suspects(choices_frame, Liste_vague1, photo_width, photo_height)
    note_label.config(text = "Pas d'image sélectionnée")
    global Dico_rang_fav
    for le_fav in (Dico_rang_fav.values()):
        le_fav.note=None
        le_fav.id=None
        name = str(le_fav.winfo_name())
        text_to_print=name[1:]
        le_fav.config(text=text_to_print, image='',height=le_fav.ht, width=le_fav.wd)
    fav_pad_x = 10
    fav_dim = int(((left_width *0.95)) / 40)
    #fav_pad_y = left_height-
    Dico_rang_fav= Init_favori(fav_dim,fav_pad_x)
    #for le_fav in (Dico_rang_fav.items()):
    #    le_fav.note=None
    #    le_fav.id=None
    #    name = str(le_fav.winfo_name())
    #    text_to_print=name[1:]
    #    le_fav.config(text=text_to_print, image='', padx=11, pady=11,height=le_fav.ht, width=le_fav.wd)

def switch_frames(fram1,fram2):
    fram1.pack_forget()
    fram2.place(relx=0.5, rely=0.5, anchor="center") 

# Ceate the main window
root = tk.Tk()
root.title("Face Determination Software")
# Define the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Calculate the width and height
left_width = screen_width * 3 // 7
right_width = screen_width * 4 // 7
choices_height = screen_height * 2 // 3
left_height = screen_height * 3 // 8
top_left_width = left_width * 1 // 4
#jauge_width = top_left_width * 2 // 15
# Create frames for left and right sections


frame_depart = tk.Frame(root, width=screen_width, height=screen_height, bg="midnight blue")
frame_depart.pack(fill = 'both',expand=True,anchor='center')
frame_depart.pack_propagate(False)

titre_depart = tk.Label(frame_depart,text = 'FACE RECOGNITION SOFTWARE',fg = 'white', font = ('Dyuthi',50),bg = 'midnight blue')
titre_depart.pack(anchor="center", pady=(150, 0) )

button = tk.Button(frame_depart, width = 20, height = 5, text="Start Working", font = ('Dyuthi',30), bg = 'gold',command=lambda: switch_frames(frame_depart,frame_interface))
button.place(relx=0.5, rely=0.5, anchor="center")

legend_depart = tk.Label(frame_depart,text = 'Made by Martin Gillard, Thibald Chalas, Aurore Le Houssel, Selma Kadiri, Théo Ducasse',fg = 'white', font = ('Dyuthi',15),bg = 'midnight blue')
legend_depart.pack(anchor="center", pady=(0, 150) )

frame_interface = tk.Frame(root, width=screen_width, height=screen_height, bg="gray80")
frame_interface.pack(expand=True,fill='both')

frame_fin = tk.Frame(root, width=screen_width, height=screen_height, bg="gray80")
frame_fin.pack(expand=True,fill='both')
frame_fin.pack_forget()


left_frame = tk.Frame(frame_interface, width=left_width, height=screen_height, bg="gray80")
right_frame = tk.Frame(frame_interface, width=right_width, height=screen_height, bg="black")
left_frame.pack(side=tk.LEFT, fill=tk.Y)
left_frame.pack_propagate(False)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)
right_frame.pack_propagate(False)
######### --Modif for the right side-- #########
### choices frame = partie supérieur de la partie de droite ###
choices_frame = tk.Frame(right_frame,width=right_width, height = choices_height, bg = "gray70")
choices_frame.pack(side=tk.TOP, fill=tk.X)
choices_frame.pack_propagate(False)

choices_frame.grid_rowconfigure(0, weight=1)
choices_frame.grid_rowconfigure(1, weight=1)
choices_frame.grid_rowconfigure(2, weight=1)
choices_frame.grid_columnconfigure(0, weight=1)
choices_frame.grid_columnconfigure(1, weight=1)
choices_frame.grid_columnconfigure(2, weight=1)
choices_frame.grid_columnconfigure(3, weight=1)



##### Creation et ajout des boutons dans choices_container (en haut à droite) #####
photo_width = int(right_width*0.18)
photo_height = int(right_width*0.18)
Vague_actuelle = 1
Liste_vague1= ["image_vague_1/1.png", "image_vague_1/2.png", "image_vague_1/3.png","image_vague_1/4.png","image_vague_1/5.png","image_vague_1/6.png","image_vague_1/7.png","image_vague_1/8.png","image_vague_1/9.png","image_vague_1/10.png", "image_vague_1/11.png","image_vague_1/12.png"]
Init_suspects(choices_frame,Liste_vague1,photo_width,photo_height)


### partie inférieur de la partie de droite, contient les boutons d'options ###
Menu_Option_Frame= tk.Frame(right_frame, bg = "black")
Menu_Option_Frame.pack(fill="both",expand=True)
Menu_Option_Frame.pack_propagate(False)

##### Création et ajout des boutons dans le frame menu option #####
"""
Menu_Option_Frame_bas= tk.Frame(right_frame, bg = "black")
Menu_Option_Frame_bas.pack(side=tk.BOTTOM, fill="both",expand=True)
Menu_Option_Frame_bas.pack_propagate(False)
"""
pad_horizontal = 10
pad_vertical = 10
Menu_Option_Frame.grid_rowconfigure(0, weight=1)
Menu_Option_Frame.grid_rowconfigure(1, weight=1)
Menu_Option_Frame.grid_columnconfigure(0, weight=1)
Menu_Option_Frame.grid_columnconfigure(1, weight=1)

Bouton_restart = tk.Button(Menu_Option_Frame,text='Start Over',background='red', command=lambda: Restart_event)
Bouton_restart.grid(column=1, row=0, sticky="nswe",padx=pad_horizontal, pady=pad_vertical)
Bouton_restart.bind("<Button-1>", Restart_event)

Bouton_refresh = tk.Button(Menu_Option_Frame,text='Refresh', background='lightblue')
Bouton_refresh.grid(column=0, row=1, sticky="nswe",padx=pad_horizontal, pady=pad_vertical)
Bouton_refresh.bind("<Button-1>", Refresh_event)

Bouton_garbage= tk.Button(Menu_Option_Frame,text='Garbage Bin', background='lightgreen')
Bouton_garbage.grid(column=0, row=0, sticky="nswe",padx=pad_horizontal, pady=pad_vertical)
Bouton_garbage.bind("<Button-1>" , Suspect.garbage )

Bouton_FIN= tk.Button(Menu_Option_Frame,text='Finish', background='yellow',command=lambda: switch_frames(frame_interface,frame_fin))
Bouton_FIN.grid(column=1, row=1, sticky="nswe",padx=pad_horizontal, pady=pad_vertical)

######### --Modif for the left side-- #########
####### --Bottom side: selection des meilleures images-- ########
best_choices_frame = tk.Frame(left_frame,width=left_width,height=left_height,bg="gray75")
best_choices_frame.pack(side=tk.BOTTOM,fill = tk.X)
best_choices_frame.pack_propagate(False)

best_choices_container_frame =  tk.Frame(best_choices_frame,width=left_width*0.95, height = left_height*0.95, bg = "white")
best_choices_container_frame.pack(fill="both", expand=True)

best_choices_container_frame.grid_rowconfigure(0, weight=1)
best_choices_container_frame.grid_rowconfigure(1, weight=1)
best_choices_container_frame.grid_columnconfigure(0, weight=1)
best_choices_container_frame.grid_columnconfigure(1, weight=1)
best_choices_container_frame.grid_columnconfigure(2, weight=1)
best_choices_container_frame.grid_columnconfigure(3, weight=1)
best_choices_container_frame.grid_columnconfigure(4, weight=1)



# Create a grid of frames
fav_pad_x = 10
fav_dim = int(((left_width *0.95)) / 40)
#fav_pad_y = left_height-
Dico_rang_fav= Init_favori(fav_dim,fav_pad_x)

Dico_rank = {}

######## --Top side: Selection d'une image et action dessus-- ########
suspect_actuel = None
main_image_frame = tk.Frame(left_frame,width=left_width,height=(screen_height-left_height),bg="gray85")
main_image_frame.pack(side=tk.TOP,fill=tk.X)
main_image_frame.pack_propagate(False)
modif_main_image_frame = tk.Frame(main_image_frame,width=top_left_width,height=(screen_height-left_height),bg="lightgray")
modif_main_image_frame.pack(side=tk.RIGHT,fill=tk.Y)
modif_main_image_frame.pack_propagate(False)

modif_main_image_frame.update()
photo_updown_size = modif_main_image_frame.winfo_width()

photo_up_raw = Image.open("up.png")
photo_up_resized = photo_up_raw.resize((photo_updown_size, photo_updown_size))
Image_up = ImageTk.PhotoImage(photo_up_resized)
button_up = tk.Button(modif_main_image_frame, image=Image_up,bg="lightgray")
button_up.pack(side=tk.TOP, fill="both",expand=True)
button_up.bind("<Button-1>",Suspect.increment_note)

note_label = tk.Label(modif_main_image_frame,text="Pas d'image sélectionnée")
note_label.pack(side=tk.TOP,fill="both",expand=True)

photo_down_raw = Image.open("down.png")
photo_down_resized = photo_down_raw.resize((photo_updown_size, photo_updown_size))
Image_down = ImageTk.PhotoImage(photo_down_resized)
button_down = tk.Button(modif_main_image_frame, image=Image_down,bg="lightgray")
button_down.pack(side=tk.BOTTOM, fill="both",expand=True)
button_down.bind("<Button-1>",Suspect.decrement_note)


view_main_image_frame = tk.Frame(main_image_frame,width=(left_width-top_left_width),height=(screen_height-left_height),bg="lightgray")
view_main_image_frame.pack_propagate(False)
view_main_image_frame.pack(side=tk.LEFT,fill=tk.Y)

### Label contenant l'image/texte en haut à gauche lors du lancement du logiciel, nécessaire car définissant taille des frames
Image_Instruction = PhotoImage(file = "instruction.png")
suspect_principal = tk.Label(view_main_image_frame , width = top_left_width, height = left_height, image = Image_Instruction)
suspect_principal.place(relx = 0.5,rely = 0.5, anchor="center")
suspect_principal.pack(fill="both",expand=True)






###############################################################################

# Bind toggle_fullscreen to F11 key
root.bind("<F11>", toggle_fullscreen)


# Run the main loop
root.mainloop()
