#importar libreria tkinter
from tkinter import *

#crea un archivo.txt. Doble argumento de open, el nombre y el permiso (Write o Read). Se usa el signo mas para crear el archivo si no exite.
f= open("test.txt","w+")

#funcion for para agregar lineas de texto al archivo txt.
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))

#cierra la instancia
f.close() 