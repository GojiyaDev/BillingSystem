import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk



# Create the main window
root = tk.Tk()
# Remove window decorations (title bar, borders)
root.overrideredirect(True)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size of the window to full screen
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Exit full screen mode and restore window decorations on pressing Escape key
def exit_fullscreen(event):
    root.attributes("-fullscreen", False)
    root.overrideredirect(False)
    root.geometry("800x600+100+100")  # Restore to a smaller size
    root.quit()

root.bind("<Escape>", exit_fullscreen)


def home():
    Framedisplay = tk.Frame(root, height=750,  width=1412, bg='#8ecae6', relief=tk.SUNKEN)
    Framedisplay.place(x=60,y=170)   


fontlabel = ('Calisto MT',20,'')

def bill():
    Framedisplay = tk.Frame(root,height=750,width=1412,bg='#8ecae6')
    Framedisplay.place(x=60,y=170)


def records():
    Framedisplay = tk.Frame(root,height=750,width=1412,bg='#8ecae6')
    Framedisplay.place(x=60,y=170)
    demolabel = tk.Label(Framedisplay,text='')
    demolabel.place(x=100,y=20)

def exits():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

custom_font = ('Monotype Corsiva',55,'')

CpyNameLbl = tk.Label(root,bg='red', width=38,text='Ram Construction', fg='white',font=custom_font)
CpyNameLbl.place(x=60,y=10) 

bill()
fontMenu = ('Algerian',20,'')
Btnhome = tk.Button(root,text='Home',font=fontMenu, width=10, command=home)
Btnhome.place(x=60,y=110)

Btnhome = tk.Button(root,text='Bill',font=fontMenu, width=10, command=bill)
Btnhome.place(x=250,y=110)

Btnhome = tk.Button(root,text='Records',font=fontMenu, width=10, command=records)
Btnhome.place(x=440,y=110)

Btnhome = tk.Button(root,text='Exits',font=fontMenu, width=10, command=exits)
Btnhome.place(x=1292,y=110)



# Run the Tkinter event loop
root.mainloop()