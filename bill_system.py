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
    bar_categories = ['2018', '2019', '2020', '2021', '2022']
    bar_values = [25, 20, 25, 20,35]

    # Sample data for pie chart
    pie_labels = ['A', 'B', 'C', 'D']
    pie_sizes = [15, 30, 45, 10] 
   

    # Create a figure object with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.12, 7.5))

    # Bar chart setup
    ax1.bar(bar_categories, bar_values, color='skyblue')
    ax1.set_xlabel('')
    ax1.set_ylabel('')
    ax1.set_title('Bar Chart Of Sales')

    # Pie chart setup
    ax2.pie(pie_sizes, labels=pie_labels, autopct='%1.1f%%', startangle=140)
    ax2.set_title('Pie Chart Of Product')

    # Embed the plot into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=Framedisplay)
    canvas.draw()
    canvas.get_tk_widget().pack()    



fontlabel = ('Calisto MT',20,'')

def bill():
    Framedisplay = tk.Frame(root,height=750,width=1412,bg='#8ecae6')
    Framedisplay.place(x=60,y=170)
    invoicelbl = tk.Label(Framedisplay, text='Invoice No', font=fontlabel, bg='#8ecae6')
    invoicelbl.place(x=15,y=15)
    invoiceEntry = tk.Entry(Framedisplay, font=fontlabel, width=5)
    invoiceEntry.place(x=160,y=15)

    datelbl = tk.Label(Framedisplay, text='Date', font=fontlabel, bg='#8ecae6')
    datelbl.place(x=1180,y=15)
    dateEntry = tk.Entry(Framedisplay, font=fontlabel, width=10)
    dateEntry.place(x=1250,y=15)

    namelbl = tk.Label(Framedisplay, text='Name', font=fontlabel, bg='#8ecae6')
    namelbl.place(x=15,y=100)
    nameEntry = tk.Entry(Framedisplay, font=fontlabel, width=15)
    nameEntry.place(x=100,y=100)

    phonelbl = tk.Label(Framedisplay, text='Phone No.', font=fontlabel, bg='#8ecae6')
    phonelbl.place(x=520,y=100)
    phoneEntry = tk.Entry(Framedisplay, font=fontlabel, width=15)
    phoneEntry.place(x=650,y=100)

    
    Addlbl = tk.Label(Framedisplay, text='Address', font=fontlabel, bg='#8ecae6')
    Addlbl.place(x=1050,y=100)
    AddEntry = tk.Entry(Framedisplay, font=fontlabel, width=15)
    AddEntry.place(x=1150,y=100)

    Citylbl = tk.Label(Framedisplay, text='City', font=fontlabel, bg='#8ecae6')
    Citylbl.place(x=30,y=250)
    CityEntry = tk.Entry(Framedisplay, font=fontlabel, width=15)
    CityEntry.place(x=100,y=250)

    statelbl = tk.Label(Framedisplay, text='State', font=fontlabel, bg='#8ecae6')
    statelbl.place(x=520,y=250)
    statecombo = ttk.Combobox(Framedisplay,width=16,font=fontlabel ,values=["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"])
    statecombo.set("Select Here")  # Set the default value
    statecombo.place(x=600,y=250)   


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
