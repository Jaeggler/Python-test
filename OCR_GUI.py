#imports
from tkinter import *
import tkinter.filedialog as tkfile
from PIL import Image, ImageTk

#Variables Globales
filepath = None

#Funcion de apertura de archivos
def openfileui():
    global filepath
    filepath = (tkfile.askopenfilename(
        filetypes=[('Imagen', '.png')]
        ))

def cropimage():
   image = Image.open("Z:\OCRTest\serra_angel.jpg")
   cropped = image.crop((25,25,250,125))
   cropped.show()

#Main window
masterw = Tk()
masterw.geometry("1000x1000")

#Botones
B1 = Button(masterw, text="Load", command=openfileui)
B1.pack()
B1.flash()

B2 = Button(masterw, text="Crop", command=cropimage)
B2.pack()
B2.flash()

#Mainloop
mainloop()