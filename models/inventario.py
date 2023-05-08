#Importar la libreria de sqlite3 de python
import sqlite3 as sql

#Funcion para crear una base de datos
def createDB():
    conn = sql.connect("inventario.db")
    conn.commit()
    conn.close()

#Funcion para crear una tabla para la base de datos NOSQL
def createTable():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE gaseosas(
            name text,
            brand text,
            quantity integer
            )"""
    )
    conn.commit()
    conn.close()

#Funcion para insertar un registro en la tabla gaseosas
def insertGaseosa(name, brand, quantity):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO gaseosas VALUES ('{name}','{brand}',{quantity})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
#Funcion para insertar varios registros en la tabla gaseosas
def insertGaseosas(listGaseosa):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO gaseosas VALUES (?, ?, ?)"
    cursor.executemany(instruction, listGaseosa)
    conn.commit()
    conn.close()

#Funcion para leer los registros de la tabla gaseosas
def readGaseosas():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"SELECT * from gaseosas"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
    
#Funcion para leer los nombres de la tabla gaseosas
def readGaseosa():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"SELECT name from gaseosas"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
    
#Funcion para leer los registros de la tabla gaseosas
def readGaseosaCantidad(gaseosa):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"SELECT quantity from gaseosas WHERE name like'{gaseosa}%'"
    cursor.execute(instruction)
    datos = cursor.fetchone()
    dato = datos[0]
    conn.commit()
    conn.close()
    return dato

#Funcion para leer los registros de la tabla gaseosas  en orden descendiente por columna
def readOrdered(field):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"SELECT * from gaseosas ORDER BY {field} DESC"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

#Funcion para leer los registros de la tabla gaseosas por nombre
def searchName(name):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"SELECT * from gaseosas WHERE name like '{name}%'"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

#Funcion para leer los registros de la tabla gaseosas por Marca
def searchBrand(name):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"SELECT * from gaseosas WHERE brand like '{name}%' ORDER BY quantity DESC"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

#Funcion para actualizar un registro de la tabla gaseosas
def updateGaseosa(name,quantity):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"UPDATE gaseosas set quantity = {quantity} WHERE name like '{name}%'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

#Funcion para eliminar un registro de la tabla gaseosas
def deleteGaseosa(name):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruction = f"DELETE from gaseosas WHERE name = '{name}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertGaseosa("Quatro","Coca-Cola", 10)
    #readGaseosas()
    #readOrdered("quantity")
    #listGaseosa = [("Manzana","Postobon",15),
    #               ("Mr. Tea","Coca-Cola",5),
    #               ("Malta Leona","Bavaria",7)
    #               ]
    #insertGaseosas(listGaseosa)
    #searchName("manzana")
    #searchBrand("coca-cola")
    #updateGaseosa("Manzana", 7)
    #searchName("manzana")
    #deleteGaseosa("Quatro")
    #readGaseosas()
    pass