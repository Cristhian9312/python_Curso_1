# una lista con8 numeros enteros,
# - recorrerla y mostrarla 
# - ordenarla y mostrarla 
# - mostrar su longitud
# - buscar un elemento dentro de esta que el usuario pida por teclado 
"""
numeros = [3,5,2,4,2,6,2,7]
"""
"""
for contador in range (1,9):
    valor2 = int(input("numero: "))
    numeros.append(valor2)
"""
"""
for contador in numeros:
    print(contador)

print(numeros)
numeros.sort()
print(numeros)
print(len(numeros))

busqueda = int(input("desde que valor quiere ver la lista: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("desde que valor quiere ver la lista: "))
else:
    print(f"has introducido el {busqueda}")

print(numeros[busqueda:])
print(busqueda in numeros)
print(numeros.index(busqueda+1))
print(numeros.count(busqueda))
"""

# Escribir un programa que añada valores a una lista y que la longitud sea menor a 120
# mostrar la lista
# usar while y for 
"""
coleccion = []

for contador in range (1,121):
    coleccion.append(f"(elemento-{contador} hola mundo)")
    #print("mostrar el: " + coleccion[contador])

def mostrarLista(lista):
    resultado = ""
    for contador in lista:
        resultado = resultado + str(contador) + "\n"  
        print(f"mostrar el {contador}, ")      
    return resultado

print(coleccion)
print(mostrarLista(coleccion))
"""
"""
numeros = []

for contador1 in range (1,21):
    numeros.append(f"(iteral: el numero y su iteracion {contador1})")

#def recorrerLista (lista):

for contador2 in numeros:
    resultado = ""
    #resultado = "este es el: "+ resultado + str(contador2)
    print(f"este es el - {contador2}")
#    return resultado

#recorrerLista(numeros)
"""

# un programa que verifique si una variable esta vacia 
# si esta vacia mostrar un texto 
# ingresarlo en minisculas y pasarlo a mayusculas 
"""
variable = ""

if len(variable.strip()) <= 0:
    variable = "soy una texto en minisculas"
    print(variable.upper())
else:
    print(f"la variable tiene un texto en {variable}")
"""
"""
variable =  "     hola"
print(variable)
#print(variable.strip(" "))
variable = variable.strip(" ")
print(variable)
"""
"""
variable = "*****hola mundo*****"
print(variable)
variable = variable.strip("*")
print(variable)
"""
# crear un scrip que tenga 4 variables, string, entera, boleana y una lista
# imprimir que tipo de variable son y que compruebe que tipo de variable es 
"""
miTexto = "cristhian"
miLista = ["cristhain", "carrero"]
miEntero = 27
miBoleano = True
resultado = ""
resultTipo = ""

escrito = input("ingrese lo que quiera: ")

def tipos(tipo):
    if tipo == str:
        resultTipo ="ES UN STRING"
    elif tipo == list:
        resultTipo = "ES UNA LISTA"
    elif tipo == int:
        resultTipo = "ES UN ENTERO"
    elif tipo == bool:
        resultTipo = "ES UN BOLLEANO"
    return resultTipo

def comprobar(dato, tipo):
    test = isinstance(dato, tipo)
    if test:
        print(f"El tipo de dato es: {tipos(tipo)}")
    else:
        print("el dato no es correcto")
    
    return resultado 

print(comprobar(escrito,str))
print(comprobar(miEntero,int))
print(comprobar(miBoleano,bool))
"""
"""
var2 = isinstance(escrito,int)
var3 = isinstance(escrito,str)
if var2:
    print("es un puto entero")
elif var3:
    print("es un puto string")
"""
# crear un diccionario como tabla que tenga tres columnas
# pede ser de juegos de accion deportes y aventuras

tabla = [
    {
        "categoria": "accion",
        "juegos": ["gta", "got", "pugb"]
    },
    {
        "categoria": "aventura",
        "juegos": ["assasing","crash","pof"]
    },
    {
        "categoria": "deportes",
        "juegos": ["fifa21","pro21","motogp21"]
    }
]

for categoria in tabla:
    print(f"\nla categoria es de {categoria['categoria']}")
    for contador in categoria['juegos']:
        print(f"el juego de: {contador}")

