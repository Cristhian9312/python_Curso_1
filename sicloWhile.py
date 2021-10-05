usuario = int(input("ingrese un numero: "))
contador = 1
muestrame = str(0)

while contador <= usuario:
    muestrame = muestrame +", "+ str(contador)
    contador = contador + 1
print(muestrame)

muestrame = "0"

for contador in range (1, usuario):
    muestrame = muestrame +", "+ str(contador)
print(muestrame)