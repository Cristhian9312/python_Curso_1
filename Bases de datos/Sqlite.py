# importar el fichero para trabajar las bases de datos
import sqlite3
# se inicia y abre la conexion a la base de datos 
conexion = sqlite3.connect('pruebas.db')
# crear cursor 
cursor = conexion.cursor()
# crear una tabla 
cursor.execute("create table if not existS productos (" +
"id integer primary key AUTOINCREMENT ," +
"titulo varchar(50)," +
"descripcion text," +
"precio int"
")")
# guardar cambios 
conexion.commit()
# insertar datos
"""
cursor.execute("insert into productos values(NULL, 'Mi primer dato', 'es una prueba', 500)")
conexion.commit()
"""
# borrar datos de una tabla 
cursor.execute("delete from productos")
conexion.commit()
# lectura o listar datos

# insertar muchos registros de golpe

productitos = [
    ( 'portatil','buen pc',700),
    ( 'celular','buen telefono',800),
    ( 'tv','buen tv',1000)
] 
cursor.executemany("insert into productos values(NULL,?,?,?)", productitos)
conexion.commit()
cursor.execute("select * from productos;")


productos = cursor.fetchall()
for i in productos:
    #print("este es titulo: ", i[1])
    #print("este es descripcion: ", i[2])
    #print("este es precio: ", i[3])
    #print("\n")
    print("Este es:", i)

cursor.execute("select titulo from productos")
producto = cursor.fetchone()
print(producto)

# cerrar conexion
conexion.close()

