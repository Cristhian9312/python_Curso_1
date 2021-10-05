"""
from io import open
import pathlib

#ruta = str(pathlib.Path().absolute()) + "/nuevo-archivo.txt"
ruta = "D:\Dell_10\Desktop\curso python\CursoPython\sistemas-de-archivos/nuevo-archivo.txt"
archivo = open(ruta, "a+")
variable = 0
while variable < 100:
    archivo.write("este es mi primer archivo\n")
    variable += 1


ruta = "D:\Dell_10\Desktop\curso python\CursoPython\sistemas-de-archivos/nuevo-archivo.txt"
lectura = open(ruta, "r+")

lista = lectura.readlines()
contador = 1
for frases in lista:    
    print(": "+ str(contador)+ " " + frases.center(35))
    contador += 1
"""
