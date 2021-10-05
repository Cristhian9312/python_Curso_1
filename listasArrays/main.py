# como estructurar listas 
"""
nombre = "santiago"
persona = ["santiago","mariño",22]
persona2 = list([("cristhian","carrero",27),("santiago","mariño",22)])
años = list(range(1,30))

print(nombre)
print(persona)
print(persona2)
print(años)
"""
# como seleccionar parametros dentro del array y modificarlos 
"""
personas = ["cristhian","yeison","santiago","julian","esperanza"]
print(personas[1:4])
print(personas[3])
print(personas[1:])
personas[3] = "jonathan"
print(personas)
"""

# añadir contenido elementos a una lista 
"""
cosas = ["PC","TV","XBOX","WII","lavadora","equipo","celular"]
print(cosas)
cosas.append("bici")
print(cosas)
""" 

# recorrer listas
"""
cosas = ["PC","TV","XBOX","WII","lavadora","equipo","celular"]

nuevaPelicula = ""
 
while nuevaPelicula != "parar":
    nuevaPelicula = input("Que pelicula quiere agregar: ")
    if nuevaPelicula != "parar":
        cosas.append(nuevaPelicula) 

for cosa in cosas:
    print(f"{cosas.index(cosa)+1}. {cosa}")
"""

#lista multidimencional, lista dentro de otra lista y recorrerla 

familia = [
    ["esperanza","madre"],
    ["cristhian","hijo"],
    ["julian","hijo"],
    ["jonathan","sobrino"]
]
print(familia[2][1])

for persona in familia:
    for elemento in persona:
        print(f"{persona[0]} y su rol es {persona[1]} ")
        print(elemento)
    print("\n")
