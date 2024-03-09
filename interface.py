import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

########## __FONCTIONS__ ##########

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))




class Suspect(tk.Button):
    def __init__(self, master, image_path, note, width, height, **kwargs):
        super().__init__(master, **kwargs)
        self.note = note
        self.original_border_color = self.cget('highlightbackground')

        photo = Image.open(image_path)
        photo_resized = photo.resize((width, height))
        self.photo_image = ImageTk.PhotoImage(photo_resized)
        self.config(image=self.photo_image, command=self.selected_suspect_event)
        self.update_color()


    #fonction appelée par les boutons suspects en haut à droite #
    #remplace l'image du suspect selctionné en haut gauche pour le noter ensuite#
    def selected_suspect_event(self):
        suspect = self
        image_suspect = suspect.cget('image')
        print(image_suspect)
        suspect_principal.configure(image=image_suspect)
    
    def increment_note(self):
        if self.note <10:
            self.note += 1
        
    def decrement_note(self):
        if self.note >0:
            self.note -= 1  
    
    def garbage(self):
        self.note = 0  # Réinitialise la note à 0
        self.config(highlightbackground='red') 

    def update_color(self):
        if self.note > 9 :
            border_color = "green"
        elif self.note > 6:
            border_color = "yellow"
        elif self.note > 3:
            border_color = "orange"
        else:
            border_color = "red"
        
        # Définit la couleur de la bordure du bouton
        self.config(highlightbackground=border_color)





#fonction appelée par le bouton restart
# réinitialise à l'état d'origine (affichage, contenu des dossiers, numérotation vague, notations) 
def Restart_event(event):
    suspect_principal.configure(image=Image_Instruction)
    Vague_actuelle=1

def Refresh_event(event):
    Genere_Suspect
    Vague_actuelle+=1
    suspect_principal.configure(image=Image_Instruction)

    return


def Genere_Suspect():
    return

#Creation d'une jauge :
def jauge(place,h):
    
    max_val = 10
    value = tk.DoubleVar()
    value.set(5)

    def mouvement(click):
        return

    #creation du slider
    slider = tk.Scale(place,from_=0,to=max_val,orient=tk.VERTICAL,variable=value,command=mouvement,length = (h*0.50),resolution= 0.1,bg="lightgray",highlightbackground="lightgray")
    slider.pack(side=tk.LEFT)



    
########## __MAIN__ ##########
    
# Create the main window
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
top_left_width = left_width * 1 // 3
jauge_width = top_left_width * 2 // 15

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

suspect_1 = Suspect(choices_container_frame, "image_vague_1/52_superposee.png",5,photo_width,photo_height)
suspect_1.grid(row=0, column=0, padx=photo_width//50, pady=photo_height//50)

suspect_2 = Suspect(choices_container_frame, "image_vague_1/138_superposee.png",5,photo_width,photo_height)
suspect_2.grid(row=0, column=1, padx=photo_width//50, pady=photo_height//50)

suspect_3 = Suspect(choices_container_frame, "image_vague_1/142_superposee.png",5,photo_width,photo_height)
suspect_3.grid(row=0, column=2, padx=photo_width//50, pady=photo_height//50)

suspect_4 = Suspect(choices_container_frame, "image_vague_1/842_superposee.png",5,photo_width,photo_height)
suspect_4.grid(row=0, column=3, padx=photo_width//50, pady=photo_height//50)

suspect_5 = Suspect(choices_container_frame, "image_vague_1/643_superposee.png",5,photo_width,photo_height)
suspect_5.grid(row=1, column=0, padx=photo_width//50, pady=photo_height//50)

suspect_6 = Suspect(choices_container_frame, "image_vague_1/623_superposee.png",5,photo_width,photo_height)
suspect_6.grid(row=1, column=1, padx=photo_width//50, pady=photo_height//50)

suspect_7 = Suspect(choices_container_frame, "image_vague_1/567_superposee.png",5,photo_width,photo_height)
suspect_7.grid(row=1, column=2, padx=photo_width//50, pady=photo_height//50)

suspect_8 = Suspect(choices_container_frame, "image_vague_1/451_superposee.png",5,photo_width,photo_height)
suspect_8.grid(row=1, column=3, padx=photo_width//50, pady=photo_height//50)

suspect_9 = Suspect(choices_container_frame, "image_vague_1/286_superposee.png",5,photo_width,photo_height)
suspect_9.grid(row=2, column=0, padx=photo_width//50, pady=photo_height//50)

suspect_10 = Suspect(choices_container_frame, "image_vague_1/284_superposee.png",5,photo_width,photo_height)
suspect_10.grid(row=2, column=1, padx=photo_width//50, pady=photo_height//50)

suspect_11 = Suspect(choices_container_frame, "image_vague_1/842_superposee.png",5,photo_width,photo_height)
suspect_11.grid(row=2, column=2, padx=photo_width//50, pady=photo_height//50)

suspect_12 = Suspect(choices_container_frame, "image_vague_1/842_superposee.png",5,photo_width,photo_height)
suspect_12.grid(row=2, column=3, padx=photo_width//50, pady=photo_height//50)


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

Bouton_garbage= tk.Button(Menu_Option_Frame,text='Garbage Bin',height=height_menu//47, width=width_menu//20, background='lightgreen')
Bouton_garbage.grid(row=1, column=1, padx=pad_horizontal, pady=pad_vertical, sticky='nswe')

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




######## --Top side: Selection d'une image et action dessus-- ########

main_image_frame = tk.Frame(left_frame,width=left_width,height=(screen_height-left_height),bg="gray85")
main_image_frame.pack(side=tk.TOP,fill=tk.X)
main_image_frame.pack_propagate(False) 

modif_main_image_frame = tk.Frame(main_image_frame,width=top_left_width,height=(screen_height-left_height),bg="lightgray")
modif_main_image_frame.pack(side=tk.RIGHT,fill=tk.Y)
modif_main_image_frame.pack_propagate(False) 

buttonP = tk.Button(modif_main_image_frame, text="+",bg="green")
buttonP.pack(side=tk.TOP, fill="both",expand=True, padx=20, pady=10)

buttonM = tk.Button(modif_main_image_frame, text="-",bg="red")
buttonM.pack(side=tk.TOP, fill="both",expand=True, padx=20, pady=10)


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
view_main_image_frame.pack(side=tk.LEFT,fill=tk.Y)
view_main_image_frame.pack_propagate(False) 

main_image_width = (left_width-top_left_width)
main_image_height = (520*main_image_width) / 360

### Label contenant l'image/texte en haut à gauche lors du lancement du logiciel, nécessaire car définissant taille des frames
Image_Instruction = PhotoImage(file = "instruction.png")
suspect_principal = tk.Label(view_main_image_frame , image=Image_Instruction, width=main_image_width, height=main_image_height,bg="lightgray")
suspect_principal.pack(fill="both",expand=True)









###############################################################################

# Bind toggle_fullscreen to F11 key
root.bind("<F11>", toggle_fullscreen)

# Numéro de la vague de suspect présente en haut à droite initialement, incrémentée à chaque refresh
Vague_actuelle = 1


# Run the main loop
root.mainloop()
