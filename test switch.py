import tkinter as tk
from PIL import Image, ImageTk

class DragDropApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Drag and Drop Example")

        self.frame1 = tk.Frame(master, width=200, height=200, bg="lightgray")
        self.frame1.grid(row=0, column=0, padx=5, pady=5)

        self.frame2 = tk.Frame(master, width=200, height=200, bg="lightgray")
        self.frame2.grid(row=0, column=1, padx=5, pady=5)

        self.image = Image.open("down.png")  # Change "image.jpg" to the path of your image
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.frame1, image=self.photo)
        self.image_label.image = self.photo
        self.image_label.place(x=0, y=0)

        self.image_label.bind("<ButtonPress-1>", self.on_drag_start)

        self.drag_data = {"x": 0, "y": 0}

    def on_drag_start(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        self.image_label.bind("<B1-Motion>", self.on_drag_motion)
        self.image_label.bind("<ButtonRelease-1>", self.on_drag_release)

    def on_drag_motion(self, event):
        x = self.image_label.winfo_x() - self.drag_data["x"] + event.x_root
        y = self.image_label.winfo_y() - self.drag_data["y"] + event.y_root
        self.image_label.place(x=x, y=y)

    def on_drag_release(self, event):
        self.image_label.unbind("<B1-Motion>")
        self.image_label.unbind("<ButtonRelease-1>")

        if (self.master.winfo_rootx() <= event.x_root <= self.master.winfo_rootx() + self.master.winfo_width() and
            self.master.winfo_rooty() <= event.y_root <= self.master.winfo_rooty() + self.master.winfo_height()):
            # Inside the main window
            if (self.frame1.winfo_rootx() <= event.x_root <= self.frame1.winfo_rootx() + self.frame1.winfo_width() and
                self.frame1.winfo_rooty() <= event.y_root <= self.frame1.winfo_rooty() + self.frame1.winfo_height()):
                # Inside frame1
                self.image_label.place(x=self.drag_data["x"], y=self.drag_data["y"])
            elif (self.frame2.winfo_rootx() <= event.x_root <= self.frame2.winfo_rootx() + self.frame2.winfo_width() and
                  self.frame2.winfo_rooty() <= event.y_root <= self.frame2.winfo_rooty() + self.frame2.winfo_height()):
                # Inside frame2
                self.image_label.place(x=self.drag_data["x"], y=self.drag_data["y"])
            else:
                # Inside the main window but outside frames
                self.image_label.place_forget()
        else:
            # Outside the main window
            self.image_label.place_forget()


def main():
    root = tk.Tk()
    app = DragDropApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
