import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

########## __FONCTIONS__ ##########

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

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
suspect_1 = tk.Button(choices_container_frame, text='suspect1' )
suspect_1.grid(row=0,column=0)
suspect_2 = tk.Button(choices_container_frame, text='suspect2' )
suspect_2.grid(row=0,column=1)
suspect_3 = tk.Button(choices_container_frame, text='suspect3' )
suspect_3.grid(row=0,column=2)
suspect_4 = tk.Button(choices_container_frame, text='suspect4' )
suspect_4.grid(row=1,column=0)
suspect_5 = tk.Button(choices_container_frame, text='suspect5' )
suspect_5.grid(row=1,column=1)
suspect_6 = tk.Button(choices_container_frame, text='suspect6' )
suspect_6.grid(row=1,column=2)
suspect_7 = tk.Button(choices_container_frame, text='suspect7' )
suspect_7.grid(row=2,column=0)
suspect_8 = tk.Button(choices_container_frame, text='suspect8' )
suspect_8.grid(row=2,column=1)
suspect_9 = tk.Button(choices_container_frame, text='suspect9' )
suspect_9.grid(row=2,column=2)
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






###############################################################################

# Bind toggle_fullscreen to F11 key
root.bind("<F11>", toggle_fullscreen)


# Run the main loop
root.mainloop()
