# los pares de 2 a 100
""" 
numero = 0

for numero in range (0,100):
    if numero/2 == 0:
        print(numero)

print("ULTIMO NUM DE LA SECUENCIA " + str(numero))

while numero < 100:
    numero += 2
    print(numero)
"""
# mostrar los cuadrados de los primeros 60 numeros naturales 
"""
contador = 0
cuadrados = 0
resultado = 2
flag = True

for contador in range(1,61):
    cuadrados = contador*contador
    print(cuadrados)

contador = 0 

while contador <= 60:
    cuadrados2 = contador*contador
    contador +=1
    print(cuadrados2)
"""
# cacular todas las operaciones matematicas por pantalla
"""
primerNumero = int(input("ingrese el 1er numero: "))
segundoNumero = int(input("ingrese el 2do numero: "))    

print(f"LA suma es {primerNumero+segundoNumero}")
print(f"LA resta es {primerNumero-segundoNumero}")
print(f"LA multiplicacion es {primerNumero*segundoNumero}")
print(f"LA devision es {primerNumero/segundoNumero}")
"""
# mostrar numeros entre dos numeros
"""
primerNumero = int(input("ingrese el 1er numero: "))
segundoNumero = int(input("ingrese el 2do numero: "))
contador = 0
muestrame = str(0)

if primerNumero > segundoNumero:
    print("el primer numero debe ser menor, intentelo de nuevo")
    primerNumero = int(input("ingrese el 1er numero: "))
    segundoNumero = int(input("ingrese el 2do numero: "))

for contador in range(primerNumero+1, segundoNumero):
    muestrame = muestrame + ", " + str(contador)
    print(contador)
    contador += 1
print(muestrame)
"""
# mostrar todas las tablas de multiplcar del 1 al 10
"""
contador = 0
tabla = 0

for contador in range (0,11):
    print(f"## la tabla del {contador} ##\n")
    for tabla in range (0,11):
        print(f"{contador} x {tabla} = {contador*tabla}")
        tabla += 1
"""
# mostrar todos los numeros impares dentro de dos numeros pedidos por consola
"""
primerNumero = int(input("ingrese el 1er numero: "))
segundoNumero = int(input("ingrese el 2do numero: "))

while primerNumero > segundoNumero:
    print("El primer numero tiene que ser mayor al segundo, intentelo de nuevo")
    primerNumero = int(input("ingrese el 1er numero: "))
    segundoNumero = int(input("ingrese el 2do numero: "))

for contador in range (primerNumero,segundoNumero):
    if contador%2 == 0:
        print(contador + 1) 
"""
# ejercicios de porcentaje
"""         
primerNumero = int(input("ingrese el numero: "))
segundoNumero = int(input(f"ingrese el porcentaje que quiera sacarle a: ({primerNumero}) "))

operacion = primerNumero * (segundoNumero/100)
print(f"el porcentaje es: {operacion}")
"""
# pedir un numero hasta que no sea 11
"""
numero = int(input("ingrese el primer numero"))
contador = numero
while numero != 11:
    numero=int(input("no es el numero solicidato, intentelo de nuevo: "))
    contador += numero

print(f"Correcto el numero a adivinar era {numero}")
print(f"la suma de los numeros que ingreso mal es de: {contador}")
"""
# pedir por pantalla la nota de 15 alumnos y mostrar los que pasan y los que pierden
"""
aprobados = 0
suspendidos = 0
alumnos = int(input("ingrese la cantidad de alumnos: ))
for contador in range(1,alumnos):
    nota = int(input("nota de los 15 alumnos: "))
    if nota < 3:
        suspendidos += 1
    elif nota >= 3:
        aprobados += 1

print(f"la cantidad de alumnos aprobados fue de {aprobados}")
print(f"la cantidad de alumnos suspendidos fue de {suspendidos}")
"""
"""
aprobados = 0
suspendidos = 0
contador = 0
cantidadAlumnos = int(input("ingrese la cantidad de alumnos: "))

while contador <= cantidadAlumnos:
    nombre = str(input("nombre del alumno: "))
    nota = int(input("nota del alumno: "))
    if nota < 3:
        suspendidos += 1
        print(f"el alumno {nombre} saco una nota de {nota} po lo tanto esta (SUSPENDIDO)")
    elif nota >= 3:
        aprobados += 1
        print(f"el alumno {nombre} saco una nota de {nota} po lo tanto esta (APROBADO)")
    contador += 1

print(f"la cantidad de alumnos suspendidos es de: {suspendidos}")
print(f"la cantidad de alumnos aprobados es de: {aprobados}")
"""
    


            

