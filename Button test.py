from tkinter import *

master = Tk()

#Primero se define la funcion o metodo

def callback ():
    print ("click!")

B1 = Button(master, text="OK", command=callback)
B1.pack()
B1.flash()

B2 = Button(master, text="NOT WORKING", command=callback, state=DISABLED)
B2.pack()

B3 = Button(master, text="RELIEF", command=callback, relief=SUNKEN)
B3.pack()


mainloop()
