''' ejemplo 1-------------
contador = 0 
resultado = 0

for contador in range ( 0,5):
    print(f"voy por el {contador}")
    resultado +=  contador

print(f"el resultado de la suma es de: {resultado}")
'''
# Ejemplo 2 

usuario = int(input('Ingrese un numero para mostrar su tabla de multiplicar: '))
contador = 0
resultado = 0
resultado2 = 0
flag = True
muestrame = ""

while flag:

    if usuario > 1 and usuario <= 10:

        for contador in range(1 , 11):
            resultado = usuario*contador
            resultado2 += resultado
            print(f"{usuario} x {contador} = {resultado}")
            flag=False 
            continue        
    else:
        usuario = int(input("ingrese un numero entre el rango: "))

for contador in range(0, 10):
    muestrame = muestrame  + str(usuario*(contador+1))+ ", "
print(muestrame [:-2])

print(f"la suma de los numeros es de: {resultado2}") 