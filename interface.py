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

# Calculate the width for the left and right frames
left_width = screen_width * 3 // 7
right_width = screen_width * 4 // 7
choices_height = screen_height * 2 // 3
left_height = screen_height * 2 // 5

# Create frames for left and right sections
left_frame = tk.Frame(root, width=left_width, height=screen_height, bg="gray80")
right_frame = tk.Frame(root, width=right_width, height=screen_height, bg="gray50")
choices_frame = tk.Frame(right_frame,width=right_width, height = choices_height, bg = "gray70")
container_frame =  tk.Frame(choices_frame,width=right_width*0.9, height = choices_height*0.9, bg = "white")
best_choices_frame = tk.Frame(left_frame,width=left_width,height=left_height,bg="gray10")
rate_image_frame = tk.Frame(left_frame,width=left_width,height=(screen_height-left_height),bg="gray20")

# Pack the frames to the left and right respectively
left_frame.pack(side=tk.LEFT, fill=tk.Y)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)
choices_frame.pack(side=tk.TOP, fill=tk.X)
best_choices_frame.pack(side=tk.BOTTOM,fill = tk.X)
rate_image_frame.pack(side=tk.TOP,fill=tk.X)

# Create a frame to contain the grid of frames
container_frame.pack(fill="both", expand=True)
container_frame.place(relx=0.5,rely=0.5,anchor="center")


        
# Bind toggle_fullscreen to F11 key
root.bind("<F11>", toggle_fullscreen)


# Run the main loop
root.mainloop()
