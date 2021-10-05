# diccionario o archivos Json
"""
personas = {
    "nombre" : "Cristhian",
    "apellido" : "carrero",
    "edad" : 27
}

print(personas)
print(type(personas))
print(personas["edad"])
"""

# lista con diccionarios 

contactos = [
    {
        "nombre" : "cristhian",
        "apellido" : "carrero",
        "edad" : 27
    },
    {
        "nombre" : "esperanza",
        "apellido" : "morales",
        "edad" : 27
    },
    {
        "nombre" : "rocip",
        "apellido" : "morales",
        "edad" : 55
    }
]

print(contactos)
print(contactos[1]["nombre"])
contactos[1]["nombre"]="esperancita"
print(contactos[1]["nombre"])