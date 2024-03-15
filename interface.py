import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

import main_sprint1

########## __FONCTIONS__ ##########

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

Dico_note ={}


class Favori(tk.Button):
    def __init__(self,position, wide, **kwargs):
        h = int (wide*0.5)
        self.wd = wide
        self.ht = h
        self.large=h*15
        self.photo_image= None
        self.note=None
        self.id=None
        self.col = column
        self.row=row
        
        super().__init__(best_choices_container_frame,width=wide, height=h, **kwargs)

    def Make_favorite (self,id, note, image ):
        self.note=note
        self.id=id
        photo = Image.open(self.id)
        photo_resized = photo.resize((self.large, self.large))
        self.photo_image = ImageTk.PhotoImage(photo_resized)
        self.config(height=self.large, width=self.large,image=self.photo_image)
        return
    
    def Update_Fav (Dico_note):
        print('ici1')
        sorted_id_by_note =  sorted(Dico_note.items(), reverse=True, key=lambda x:x[1])
        lim = 1
        for i in sorted_id_by_note : 
            if lim < 10 :
                if (i[1]>6):
                    path = i[0]
                    print(path)
                    photo = Image.open(path)
                    photo_resized = photo.resize((Dico_rang_fav[lim].large, Dico_rang_fav[lim].large,))
                    Dico_rang_fav[lim].photo_image = ImageTk.PhotoImage(photo_resized)
                    print(Dico_rang_fav[lim])
                    Dico_rang_fav[lim].config(height=Dico_rang_fav[lim].large,width=Dico_rang_fav[lim].large, image=Dico_rang_fav[lim].photo_image)
                    lim+=1
                    
         for j in range (10):
            le_fav = Dico_rang_fav[j+1]
            la_note = sorted_id_by_note[j][1]
            h = le_fav.large
            w = le_fav.large
            if (la_note<7):
                le_fav.note=None
                name = str(le_fav.winfo_name())
                text_to_print=name[1:]
                le_fav.config(text=text_to_print, image='', padx=11, pady=11,height=le_fav.ht, width=le_fav.wd)      
       
    def get_first_non_fav(dico_sorted):
        pos = 0 
        for i in dico_sorted : 
            if i[1]>6:
                pos+=1
        return pos
            
    def Clear_fav (self):
        self.config(text= str(self.winfo_name()), image='', height=self.large, width=self.large)

        

class Suspect(tk.Button):
    def __init__(self, master, image_path, note, width, height, **kwargs):
        super().__init__(master, **kwargs)
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
        global suspect_actuel
        suspect_actuel = self
        note_label.config(text = 'Note: ' + str(self.note))
        image_suspect = suspect_actuel.cget('image')
        suspect_principal.configure(image=image_suspect)
    
    def increment_note(self):
        
        global suspect_actuel
        if suspect_actuel.note <10:
            suspect_actuel.note += 1
            
            suspect_actuel.update_color()
        global Dico_note
        global note_label
        note_label.config(text="Note: "+str(suspect_actuel.note))
        Dico_note[suspect_actuel.id]= suspect_actuel.note
        suspect_actuel.Ajout_Favori()
        Favori.Update_Fav(Dico_note=Dico_note)

            
    def decrement_note(self):
        global suspect_actuel
        if suspect_actuel.note >0:
            suspect_actuel.note = suspect_actuel.note - 1 
            suspect_actuel.update_color() 
        global note_label
        global Dico_note
        note_label.config(text="Note: "+str(suspect_actuel.note))
        Dico_note[suspect_actuel.id]= suspect_actuel.note
        Favori.Update_Fav(Dico_note=Dico_note)
    
    def garbage(self):
        global suspect_actuel
        suspect_actuel.note = 0  # Réinitialise la note à 0
        suspect_actuel.update_color()
        global note_label
        note_label.config(text="Note: "+str(suspect_actuel.note))
        global Dico_note
        Dico_note[suspect_actuel.id]= suspect_actuel.note
        
        Favori.Update_Fav(Dico_note=Dico_note)

    def update_color(self):
        global suspect_actuel
        
        if suspect_actuel.note >= 9 :
            border_color = "dark green"
        elif suspect_actuel.note >= 7:
            border_color = "green yellow"
        elif suspect_actuel.note > 3:
            border_color = self.original_border_color
        elif suspect_actuel.note > 1:
            border_color = "orange"
        else:
            border_color = "red"
        
        # Définit la couleur de la bordure du bouton
        suspect_actuel.config(highlightbackground=border_color)
   
    
    def ranking(self):
        rank=1
        rating=suspect_actuel.note
        for notes in Dico_note.values():
            if (rating<notes):
                rank+=1
        return rank
    
    def Ajout_Favori(self):
        global suspect_actuel
        rank = suspect_actuel.ranking()
        if (rank<10 and self.note>6):
            print('favori')
            Favori.Make_favorite(Dico_rang_fav[rank], suspect_actuel.id, suspect_actuel.note, suspect_actuel.photo_image)
        return


#fonction appelée par le bouton restart
# réinitialise à l'état d'origine (affichage, contenu des dossiers, numérotation vague, notations) 
def Restart_event(event):
    suspect_principal.configure(image=Image_Instruction)
    Start_Over()
    Vague_actuelle=1

def Refresh_event(event):
    global Vague_actuelle
    print('REFRESH REFRESH')
    Liste_path = Genere_Suspect(Dico_note, Vague_actuelle)
    Vague_actuelle+=1
    #genere 12 nouvelles images de suspects  "\vague_2\image_1", "\vague2|image2... n"
    suspect_principal.configure(image=Image_Instruction)
    Init_suspects(choices_container_frame,Liste_path,photo_width,photo_height)
    return

#Dico note est un dictionnaire qui contient en clé les path des images (string) et en value les notes associées aux images (int). Exemple de contenu :
#{'image_vague_1/1.png': 5, 'image_vague_1/2.png': 5, 'image_vague_1/3.png': 5, 'image_vague_1/4.png': 5, 'image_vague_1/5.png': 5, 'image_vague_1/6.png': 5, 'image_vague_1/7.png': 5, 'image_vague_1/8.png': 5, 'image_vague_1/9.png': 5}

#fonction Gene_Suspect :
#genere 12 nouvelles images de suspects dans un dossier nommée vague_n\: Par exemple pour n=2, on veut en sortie 12 images au format .png telles que:  "\vague_2\image_1.png", "\vague_2\image_2.png, ... , "\vague_2\image_11.png "
# return une liste contenant les paths des 12 image
def Genere_Suspect(Dico, Vague_actuelle ):
    print(Vague_actuelle)
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
    Liste_Path_nouvelle_vague=main_sprint1.IHM_loop(Vague_actuelle, note_list)
    
    print(Liste_Path_nouvelle_vague)
    return (Liste_Path_nouvelle_vague)

def Init_suspects(choices_container_frame,Liste_img,photo_width,photo_height):

    suspect_1 = Suspect(choices_container_frame,Liste_img[0],5,photo_width,photo_height)
    suspect_1.grid(row=0, column=0, padx=photo_width//50, pady=photo_height//50)

    suspect_2 = Suspect(choices_container_frame, Liste_img[1],5,photo_width,photo_height)
    suspect_2.grid(row=0, column=1, padx=photo_width//50, pady=photo_height//50)

    suspect_3 = Suspect(choices_container_frame, Liste_img[2],5,photo_width,photo_height)
    suspect_3.grid(row=0, column=2, padx=photo_width//50, pady=photo_height//50)

    suspect_4 = Suspect(choices_container_frame, Liste_img[3],5,photo_width,photo_height)
    suspect_4.grid(row=0, column=3, padx=photo_width//50, pady=photo_height//50)

    suspect_5 = Suspect(choices_container_frame, Liste_img[4],5,photo_width,photo_height)
    suspect_5.grid(row=1, column=0, padx=photo_width//50, pady=photo_height//50)

    suspect_6 = Suspect(choices_container_frame, Liste_img[5],5,photo_width,photo_height)
    suspect_6.grid(row=1, column=1, padx=photo_width//50, pady=photo_height//50)

    suspect_7 = Suspect(choices_container_frame, Liste_img[6],5,photo_width,photo_height)
    suspect_7.grid(row=1, column=2, padx=photo_width//50, pady=photo_height//50)

    suspect_8 = Suspect(choices_container_frame, Liste_img[7],5,photo_width,photo_height)
    suspect_8.grid(row=1, column=3, padx=photo_width//50, pady=photo_height//50)

    suspect_9 = Suspect(choices_container_frame, Liste_img[8],5,photo_width,photo_height)
    suspect_9.grid(row=2, column=0, padx=photo_width//50, pady=photo_height//50)

    suspect_10 = Suspect(choices_container_frame, Liste_img[9],5,photo_width,photo_height)
    suspect_10.grid(row=2, column=1, padx=photo_width//50, pady=photo_height//50)

    suspect_11 = Suspect(choices_container_frame, Liste_img[10],5,photo_width,photo_height)
    suspect_11.grid(row=2, column=2, padx=photo_width//50, pady=photo_height//50)

    suspect_12 = Suspect(choices_container_frame, Liste_img[11],5,photo_width,photo_height)
    suspect_12.grid(row=2, column=3, padx=photo_width//50, pady=photo_height//50)

def Start_Over():
    Vague_actuelle = 1
    Init_suspects(choices_container_frame, Liste_vague1, photo_width, photo_height)
    note_label.config(text = "Pas d'image sélectionnée")




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
left_frame = tk.Frame(root, width=left_width, height=screen_height, bg="gray80")
right_frame = tk.Frame(root, width=right_width, height=screen_height, bg="black")
left_frame.pack(side=tk.LEFT, fill=tk.Y)
left_frame.pack_propagate(False) 
right_frame.pack(side=tk.RIGHT, fill=tk.Y)
right_frame.pack_propagate(False) 
######### --Modif for the right side-- #########
### choices frame = partie supérieur de la partie de droite ###
choices_frame = tk.Frame(right_frame,width=right_width, height = choices_height, bg = "gray70")
choices_frame.pack(side=tk.TOP, fill=tk.X)
choices_frame.pack_propagate(False) 
### intérieur de la partie supérieur de la partie de droite, contient les suspects ###
choices_container_frame =  tk.Frame(choices_frame,width=right_width*0.9, height = choices_height*0.9, bg = "white")
choices_container_frame.pack(fill="both", expand=True)
choices_container_frame.pack_propagate(False) 
choices_container_frame.place(relx=0.5,rely=0.5,anchor="center")
choices_container_frame.update()
choices_height = (choices_container_frame.winfo_height()//1)
choices_width = choices_container_frame.winfo_width()
### partie inférieur de la partie de droite, contient les boutons d'options ###
Menu_Option_Frame = tk.Frame(right_frame,width=right_width, height = (screen_height-choices_height), bg = "gray10")
Menu_Option_Frame.pack_propagate(False) 
Menu_Option_Frame.pack(side=tk.TOP, fill='both')

##### Creation et ajout des boutons dans choices_container (en haut à droite) #####
photo_width = int(right_width*0.18)
photo_height = int(right_width*0.18)
Vague_actuelle = 1
Liste_vague1= ["image_vague_1/1.png", "image_vague_1/2.png", "image_vague_1/3.png","image_vague_1/4.png","image_vague_1/5.png","image_vague_1/6.png","image_vague_1/7.png","image_vague_1/8.png","image_vague_1/9.png","image_vague_1/10.png", "image_vague_1/11.png","image_vague_1/12.png"]
Init_suspects(choices_container_frame,Liste_vague1,photo_width,photo_height)


##### Création et ajout des boutons dans le frame menu option #####
Menu_Option_Frame.update()
height_menu = Menu_Option_Frame.winfo_height()
width_menu = Menu_Option_Frame.winfo_width()

pad_horizontal = width_menu // 15
pad_vertical = height_menu // 22

Bouton_restart = tk.Button(Menu_Option_Frame,text='Start Over',height=height_menu//47, width=width_menu//20,background='red', command=lambda: Restart_event)
Bouton_restart.grid(row=1, column=2, padx=pad_horizontal, pady=pad_vertical, sticky='nswe')
Bouton_restart.bind("<Button-1>", Restart_event)

Bouton_refresh = tk.Button(Menu_Option_Frame,text='Refresh',height=height_menu//47, width=width_menu//20, background='lightblue')
Bouton_refresh.grid(row=2, column=1, padx=pad_horizontal, pady=pad_vertical, sticky='nswe')
Bouton_refresh.bind("<Button-1>", Refresh_event)

Bouton_garbage= tk.Button(Menu_Option_Frame,text='Garbage Bin',height=height_menu//47, width=width_menu//20, background='lightgreen')
Bouton_garbage.grid(row=1, column=1, padx=pad_horizontal, pady=pad_vertical, sticky='nswe')
Bouton_garbage.bind("<Button-1>" , Suspect.garbage )

Bouton_FIN= tk.Button(Menu_Option_Frame,text='Finish', height=height_menu//47, width=width_menu//20, background='yellow')
Bouton_FIN.grid(row=2, column=2, padx=pad_horizontal, pady=pad_vertical, sticky='nswe')

######### --Modif for the left side-- #########
####### --Bottom side: selection des meilleures images-- ########
best_choices_frame = tk.Frame(left_frame,width=left_width,height=left_height,bg="gray75")
best_choices_frame.pack(side=tk.BOTTOM,fill = tk.X)
best_choices_frame.pack_propagate(False) 
best_choices_container_frame =  tk.Frame(best_choices_frame,width=left_width*0.95, height = left_height*0.95, bg = "white")
best_choices_container_frame.pack(fill="both", expand=True)
best_choices_container_frame.pack_propagate(False) 
best_choices_container_frame.place(relx=0.5,rely=0.5,anchor="center")
# Create a grid of frames
favorites = [[tk.Frame(best_choices_container_frame, bg="lightgreen") for _ in range(5)] for _ in range(2)]
fav_dim = int(left_width*0.021)
print(fav_dim)

fav_1 = Favori(1,fav_dim)
fav_1.config(text="favori 1")
fav_1.grid(row=1, column=1, padx=fav_dim, pady=fav_dim)

fav_2 = Favori(2, fav_dim)
fav_2.config(text='favori 2')
fav_2.grid(row=1, column = 2, padx=fav_dim, pady=fav_dim)

fav_3 = Favori(3,fav_dim)
fav_3.config(text="favori 3")
fav_3.grid(row=1, column=3, padx=fav_dim, pady=fav_dim)

fav_4 = Favori(4, fav_dim)
fav_4.config(text='favori 4')
fav_4.grid(row=1, column = 4, padx=fav_dim, pady=fav_dim)

fav_5 = Favori(5,fav_dim)
fav_5.config(text="favori 5")
fav_5.grid(row=1, column=5, padx=fav_dim, pady=fav_dim)

fav_6 = Favori(6, fav_dim)
fav_6.config(text='favori 6')
fav_6.grid(row=2, column = 1, padx=fav_dim, pady=fav_dim)

fav_7 = Favori(7,fav_dim)
fav_7.config(text="favori 7")
fav_7.grid(row=2, column=2, padx=fav_dim, pady=fav_dim)

fav_8 = Favori(8, fav_dim)
fav_8.config(text='favori 8')
fav_8.grid(row=2, column = 3, padx=fav_dim, pady=fav_dim)

fav_9 = Favori(9,fav_dim)
fav_9.config(text="favori 9")
fav_9.grid(row=2, column=4, padx=fav_dim, pady=fav_dim)

fav_10 = Favori(10, fav_dim)
fav_10.config(text='favori 10')
fav_10.grid(row=2, column = 5, padx=fav_dim, pady=fav_dim)

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

note_label = tk.Label(modif_main_image_frame,text="Note: " + str(5))
note_label.pack(side=tk.TOP,fill="both",expand=True)

photo_down_raw = Image.open("down.png")
photo_down_resized = photo_down_raw.resize((photo_updown_size, photo_updown_size))
Image_down = ImageTk.PhotoImage(photo_down_resized)
button_down = tk.Button(modif_main_image_frame, image=Image_down,bg="lightgray")
button_down.pack(side=tk.BOTTOM, fill="both",expand=True)
button_down.bind("<Button-1>",Suspect.decrement_note)

"""
jauge_frame = tk.Frame(modif_main_image_frame,width=jauge_width,height=(screen_height-left_height),bg="lightgray")
jauge_frame.pack(side=tk.LEFT,fill=tk.Y)
jauge_frame.pack_propagate(False) 
jauge = jauge(jauge_frame,(screen_height-left_height))
buttons_modif_main_frame = tk.Frame(modif_main_image_frame,width=(top_left_width-jauge_width),height=(screen_height-left_height),bg="lightgray")
buttons_modif_main_frame.pack(side=tk.RIGHT,fill=tk.Y)
buttons_modif_main_frame.pack_propagate(False) 
button1 = tk.Button(buttons_modif_main_frame, text="Save Mark")
button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
"""
view_main_image_frame = tk.Frame(main_image_frame,width=(left_width-top_left_width),height=(screen_height-left_height),bg="lightgray")
view_main_image_frame.pack_propagate(False) 
view_main_image_frame.pack(side=tk.LEFT,fill=tk.Y)

main_image_width = (left_width-top_left_width)
main_image_height = (520*main_image_width) / 360
### Label contenant l'image/texte en haut à gauche lors du lancement du logiciel, nécessaire car définissant taille des frames
Image_Instruction = PhotoImage(file = "instruction.png")
suspect_principal = tk.Label(view_main_image_frame , image=Image_Instruction, width=main_image_width, height=main_image_height,bg="lightgray")
suspect_principal.pack(fill="both",expand=True)
  


###############################################################################

# Bind toggle_fullscreen to F11 key
root.bind("<F11>", toggle_fullscreen)


# Run the main loop
root.mainloop()
