import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

########## __FONCTIONS__ ##########

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

#fonction appelée par les boutons suspects en haut à droite #

def Selected_Suspect_event(event):
    suspect = event.widget
    image_suspect = suspect.cget('image')
    suspect_principal.configure(image=image_suspect)
    



#Creation d'une jauge :
def jauge(place):
    max_val = 10
    value = tk.DoubleVar()
    value.set(5)

    def dessin():
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        #Dessin du background
        canvas.create_rectangle(0,0,width,height,fill="lightgray",outline="")

        #Calculer la largeure de la jauge basée sur la valeur actuelle
        jauge_width = (value.get() / max_value) * width

        #Dessin de la jauge
        canvas.create_rectangle(0,0,jauge_width,height,fill="green",outline="")
        
    def mouvement(click):
        dessin()

    #creation du canvas
    canvas = tk.Canvas(master,width = 200, height = 20)
    canvas.pack(padx=10,pady=10)

    #creation du slider
    slider = tk.Scale(info,from_=0,to=max_value,orient=tk.VERTICAL,variable=value,command=mouvement)
    slider.pack(fill=tk.y)

    #Dessin
    dessin()


    
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
top_left_width = left_width * 9 // 20

# Create frames for left and right sections
left_frame = tk.Frame(root, width=left_width, height=screen_height, bg="gray80")
right_frame = tk.Frame(root, width=right_width, height=screen_height, bg="gray50")
left_frame.pack(side=tk.LEFT, fill=tk.Y)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)


######### --Modif for the right side-- #########

choices_frame = tk.Frame(right_frame,width=right_width, height = choices_height, bg = "gray70")
choices_frame.pack(side=tk.TOP, fill=tk.X)

choices_container_frame =  tk.Frame(choices_frame,width=right_width*0.9, height = choices_height*0.9, bg = "white")
choices_container_frame.pack(fill="both", expand=True)
choices_container_frame.place(relx=0.5,rely=0.5,anchor="center")

######### Creation et ajout des boutons dans choices_container (en haut à droite)
photo_1 = PhotoImage(file = "image_sample/0_superposee.png") 
photo_resized_1 = photo_1.subsample(3,3)
suspect_1 = tk.Button(choices_container_frame, image = photo_resized_1, command=lambda: Selected_Suspect_event)
suspect_1.grid(row=0,column=0, padx=20, pady=5)
suspect_1.bind("<Button-1>", Selected_Suspect_event)

photo_2 = PhotoImage(file = "image_sample/1_superposee.png") 
photo_resized_2 = photo_2.subsample(3,3)
suspect_2 = tk.Button(choices_container_frame, image = photo_resized_2 , command=lambda: Selected_Suspect_event)
suspect_2.grid(row=0,column=1, padx=20, pady=5)
suspect_2.bind("<Button-1>", Selected_Suspect_event)

photo_3 = PhotoImage(file = "image_sample/2_superposee.png") 
photo_resized_3 = photo_3.subsample(3,3)
suspect_3 = tk.Button(choices_container_frame, image = photo_resized_3 , command=lambda: Selected_Suspect_event)
suspect_3.grid(row=0,column=2, padx=20, pady=5)
suspect_3.bind("<Button-1>", Selected_Suspect_event)

photo_4 = PhotoImage(file = "image_sample/3_superposee.png") 
photo_resized_4 = photo_4.subsample(3,3)
suspect_4 = tk.Button(choices_container_frame, image = photo_resized_4 , command=lambda: Selected_Suspect_event)
suspect_4.grid(row=1,column=0, padx=20, pady=5)
suspect_4.bind("<Button-1>", Selected_Suspect_event)

photo_5 = PhotoImage(file = "image_sample/4_superposee.png") 
photo_resized_5 = photo_5.subsample(3,3)
suspect_5 = tk.Button(choices_container_frame, image = photo_resized_5 , command=lambda: Selected_Suspect_event)
suspect_5.grid(row=1,column=1, padx=20, pady=5)
suspect_5.bind("<Button-1>", Selected_Suspect_event)

photo_6 = PhotoImage(file = "image_sample/5_superposee.png") 
photo_resized_6 = photo_6.subsample(3,3)
suspect_6 = tk.Button(choices_container_frame, image = photo_resized_6 , command=lambda: Selected_Suspect_event)
suspect_6.grid(row=1,column=2, padx=20, pady=5)
suspect_6.bind("<Button-1>", Selected_Suspect_event)

photo_7 = PhotoImage(file = "image_sample/6_superposee.png") 
photo_resized_7 = photo_7.subsample(3,3)
suspect_7 = tk.Button(choices_container_frame, image = photo_resized_7 , command=lambda: Selected_Suspect_event)
suspect_7.grid(row=2,column=0, padx=20, pady=5)
suspect_7.bind("<Button-1>", Selected_Suspect_event)

photo_8 = PhotoImage(file = "image_sample/7_superposee.png") 
photo_resized_8 = photo_8.subsample(3,3)
suspect_8 = tk.Button(choices_container_frame, image = photo_resized_8 , command=lambda: Selected_Suspect_event)
suspect_8.grid(row=2,column=1, padx=20, pady=5)
suspect_8.bind("<Button-1>", Selected_Suspect_event)

photo_9 = PhotoImage(file = "image_sample/8_superposee.png") 
photo_resized_9 = photo_9.subsample(3,3)
suspect_9 = tk.Button(choices_container_frame, image = photo_resized_9 , command=lambda: Selected_Suspect_event)
suspect_9.grid(row=2,column=2, padx=20, pady=5)
suspect_9.bind("<Button-1>", Selected_Suspect_event)




######### --Modif for the left side-- #########



####### --Bottom side: selection des meilleures images-- ########

best_choices_frame = tk.Frame(left_frame,width=left_width,height=left_height,bg="gray75")
best_choices_frame.pack(side=tk.BOTTOM,fill = tk.X)

best_choices_container_frame =  tk.Frame(best_choices_frame,width=left_width*0.95, height = left_height*0.95, bg = "white")
best_choices_container_frame.pack(fill="both", expand=True)
best_choices_container_frame.place(relx=0.5,rely=0.5,anchor="center")

# Create a grid of frames
favorites = [[tk.Frame(best_choices_container_frame, bg="lightgreen") for _ in range(5)] for _ in range(2)]





######## --Top side: Selection d'une image et action dessus-- ########

main_image_frame = tk.Frame(left_frame,width=left_width,height=(screen_height-left_height),bg="gray85")

main_image_frame.pack(side=tk.TOP,fill=tk.X)

modif_main_image_frame = tk.Frame(main_image_frame,width=top_left_width,height=(screen_height-left_height),bg="gray80")
modif_main_image_frame.pack(side=tk.RIGHT,fill=tk.Y)

view_main_image_frame = tk.Frame(main_image_frame,width=(left_width-top_left_width),height=(screen_height-left_height),bg="gray82")
view_main_image_frame.pack(side=tk.LEFT,fill=tk.Y)
photo_Q_mark = PhotoImage(file = "instruction.png")
suspect_principal = tk.Label(view_main_image_frame , image=photo_Q_mark, width=360, height=520)
suspect_principal.pack()






###############################################################################

# Bind toggle_fullscreen to F11 key
root.bind("<F11>", toggle_fullscreen)


# Run the main loop
root.mainloop()
