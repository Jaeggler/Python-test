from tkinter import *
import tkinter.filedialog as tkfile
import serial
import time

#ventana principal
masterw = Tk()
masterw.geometry("300x300")

filepath = StringVar()

#Open ports
port1 = serial.Serial("COM8", 115200)

# Wake up grbl
port1.write("\r\n\r\n".encode())
time.sleep(2)   # Wait for grbl to initialize
port1.flushInput()  # Flush startup text in serial input

#Interfaz de seleccion de archivo
def openfileui():
    global filepath
    filepath.set( (tkfile.askopenfilename(
        filetypes=[('gcode', '.nc')]
        )))
    
#Enviar data al GRBL
def senddata():
    # Stream g-code to grbl
    ofile = open(filepath)
    for line in ofile:
        l = line.strip() # Strip all EOL characters for consistency
        print('Sending: ' + l)
        port1.write((l + '\n').encode()) # Send g-code block to grbl
        grbl_out = port1.readline() # Wait for grbl response with carriage return
        print(' : ' + (grbl_out.strip()).decode())
    
    # Wait here until grbl is finished to close serial port and file.
    input("Enter to exit and disable grbl.")
    ofile.close() #close file
 
#Logo
logo = PhotoImage(file="logofab100px.gif")
L1 = Label(masterw, image=logo)
L1.photo = logo
L1.pack()

#Primero se define la funcion o metodo
B1 = Button(masterw, text="Load", command=openfileui)
B1.pack()
B1.flash()

L2 = Label(masterw, textvariable = filepath)
L2.pack()

B3 = Button(masterw, text="Send Data", command=senddata)
B3.pack()
B3.flash()

B4 = Button(masterw, text="Quit", command=quit)
B4.pack()
B4.flash()



#Funcion loop!
mainloop()