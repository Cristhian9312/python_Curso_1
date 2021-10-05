#ordenar listas de numeros 
cantantes = ["nickel Back","green day","liking park","MEtallica"]
numeros = [1,3,2,5,4,6]
 
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
#print(numeros[2:])

print(numeros.count(5))
print(cantantes)
cantantes.append("Reik")
print(cantantes)
cantantes.insert(2,"Reik")
print(cantantes)
print("Reik" in cantantes)
print(len(cantantes))
 
 # append = agrega un elemento a la lista de ultoma posicion
 # insert = lo agrega en un lugar espesifico (1,"xxx")
 # pop = elimina un cierto lugar de la lista 
 # remove = elimina un elemento espesifico de la lista con el nombre "XXXXXX"
 # reverse = regresa el orden de la lista, de mayor a menor 
 # extend = sirve pra concatenar dos listas 

cantantes.pop(2)
print(cantantes)
cantantes.extend(numeros)
print(cantantes)