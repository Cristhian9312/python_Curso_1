# Ejemplo de pedir nombre y edad por parametros
"""
nombre = input("Cual es tu nombre: ")
edad = int(input("Cual es tu edad: "))

def mostrarMiNombre (nombre, edad):
    if edad >= 18:
        print(f"Hola {nombre}, tienes {edad} años y eres mayor de edad")
    else:
        print(f"Hola {nombre}, tienes {edad} años y eres menor de edad")    

mostrarMiNombre(nombre,edad)
"""
#ejemplo de hacer las tablas de multiplicar ejecutando la funcion con parametros de entrada
"""
tabla = int(input("que tabala de multiplicar quieres: "))
print(f"la tabla de multiplicar del {tabla} \n")
def tablaDeMultiplicar (tabla):
    for contador in range (1,11):
        operacion = tabla * contador
        print(f"{tabla} x {contador} = {operacion}")

tablaDeMultiplicar(tabla)        
print("-------------------")
for contador in range (1,tabla+1):
    tablaDeMultiplicar(contador)
    contador += 1
"""
# parametros opcionales 
"""
empleado = input("cual es tu nombre: ")
nit = input("cual es tu nit: ")

def saludar (empleado, nit = None):
    if nit == '':
        print(f"hola {empleado}, buen dia")    
    else:
        print(f"hola {empleado} tu nit es {nit}")

saludar(empleado,nit)
"""
# funciones con retur
"""
def saludar (nombre):
    saludo = f"hola {nombre}"
    return saludo

print(saludar("camilo"))
"""
# ejercicio de calculadora con return 
"""
primerNumero = int(input("cual es el primer numero: "))
segundoNumero = int(input("cual es el segundo numero: "))

def calculadora (primerNumero, segundoNumero):
    suma = primerNumero + segundoNumero
    resta = primerNumero - segundoNumero
    multiplicacion = primerNumero * segundoNumero
    division = primerNumero / segundoNumero

    cadena = ''
    cadena = cadena + f"la suma es ({str(suma)})" + f"la resta es ({str(resta)})" + f"la multiplicacion es ({str(multiplicacion)})" + f"la division es ({str(division)})"
    return cadena

print(calculadora(primerNumero,segundoNumero))
"""
# funcion llamando otra funcion 
"""
def nombre(nombres):
    texto = f"tu nombre es {nombres}"
    return texto

def apellido (apellidos):
    texto = f"tu apellido es {apellidos}"
    return texto     

def regresaTodo (nombres, apellidos):
    texto = nombre(nombres) + apellido(apellidos)
    return texto

print(nombre("camilo"))
print(apellido("carrero"))
print(regresaTodo("cristhian","camilo"))
"""
