# verificar con la funcion (isinstance)
"""
nombre = "cristhian "

print(type(nombre))

comprobar = isinstance(nombre, str)

if comprobar:
    print("es un string")
else:
    print("no es un string")
"""
#limpiar espacion en un string con (.strip)
"""
nombre = "     camilo"
print(nombre)
print(nombre.strip())
"""
#eliminar variables con (del)
"""
year = 2021
print(year)
del year
print(year)
"""

# contar los caracteres de una variable o array o lista con (len), encontrar una cadena espesifica con (find)
"""
nombre = "cristhian"

print(len(nombre))
print(nombre.__len__())
print(nombre.find("thi"))

"""
#reemplazar una palabra dentro de un string y colocarla en mayusculas 
"""
frase = "la programacion en java es muy perra"
print(frase.replace("perra","chevere"))
print(frase.upper())
"""