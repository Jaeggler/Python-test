from tkinter import *
import tkinter.filedialog as tkfile
import serial
import time

#ventana principal
masterw = Tk()
masterw.geometry("300x300")

filepath = StringVar()
portentry = ""
serialport = None

#Interfaz de seleccion de archivo
def openfileui():
    global filepath
    filepath.set(tkfile.askopenfilename(
        filetypes=[('gcode', '.nc')]
        ))
    
    

#Enviar data al GRBL
def senddata():
    # Stream g-code to grbl
    ofile = open(filepath)
    for line in ofile:
        l = line.strip() # Strip all EOL characters for consistency
        print('Sending: ' + l)
        serialport.write((l + '\n').encode()) # Send g-code block to grbl
        grbl_out = serialport.readline() # Wait for grbl response with carriage return
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

#Texto de la ruta
L2 = Label(masterw, textvariable=filepath)
L2.pack()

#Texto de puerto de comunicacion
E1 = Entry(masterw)
E1.pack()


#Open ports
def connectport():
        global portentry
        portentry = E1.get()
        global serialport
        serialport = serial.Serial(portentry, 115200)
        # Wake up grbl
        serialport.write("\r\n\r\n".encode())
        time.sleep(2)   # Wait for grbl to initialize
        serialport.flushInput()  # Flush startup text in serial input


B2 = Button(masterw, text="Connect", command=connectport)
B2.pack()
B2.flash()

B3 = Button(masterw, text="Send Data", command=senddata)
B3.pack()
B3.flash()

B4 = Button(masterw, text="Quit", command=quit)
B4.pack()
B4.flash()



#Funcion loop!
mainloop()