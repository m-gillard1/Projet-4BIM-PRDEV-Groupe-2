import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

# Create the main window
root = tk.Tk()
root.title("Face Determination Software")

# Define the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()




        
# Bind toggle_fullscreen to F11 key
root.bind("<F11>", toggle_fullscreen)


# Run the main loop
root.mainloop()
