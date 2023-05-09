#instalar la dependencia de python que permite la conexion a SQL SERVER "pip installl pyodbc" e importarla
import pyodbc

#Establecer los parametros para la conexion con SQL SERVER
server = 'DESKTOP-K50KJKV\MSSQLSERVER01'
bd = 'users'
user = 'sa'
password = '12345678'

#Intentar la conexion a SQL Server, cadena de la documentacion oficial => 'DRIVER={SQL Server}; SERVER='YourServer';DATABASE='DatabaseName';UID='SQLServerUser';PWD='Password'
try:
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)
    print('Connection is successful.')
    cursor = conn.cursor()
except:
    print('Connection was unsuccessful.')

#Crear funcion para leer la tabla Customer de la base de datos
def readCustomers():
    instruction = "Select * from Customer;"
    cursor.execute(instruction)
    customers = cursor.fetchall()
    return customers

#Crear funcion para leer un Customer de la base de datos
def readCustomer(fullname):
    instruction = f"Select * from Customer where fullname = '{fullname}';"
    cursor.execute(instruction)
    customer = cursor.fetchall()
    return customer

    
#Crear funcion para insertar un nuevo registro en la tabla Customer de la base de datos
def insertCustomer(name, phone):
    instruction = f"INSERT INTO Customer VALUES ('{name}','{phone}');"
    cursor.execute(instruction)
    conn.commit()

#Crear funcion para modificar un registro en la tabla Customer de la base de datos
def updateCustomer(id,name, phone):
    instruction = f"UPDATE Customer SET fullname = '{name}', phone = '{phone}' WHERE Id = {id};"
    cursor.execute(instruction)
    conn.commit()
    
#Crear funcion para eliminar un registro en la tabla Customer de la base de datos
def deleteCustomer(id):
    instruction = f"DELETE from Customer WHERE Id = {id};"
    cursor.execute(instruction)
    conn.commit()

#readCustomers()
#insertCustomer("Juan","+573012888888")
#readCustomers()
#updateCustomer("1","Ramiro","+573128765432")
#readCustomers()
#deleteCustomer("7")
#readCustomers()
#----------------------------------------------------------------------------------------------------------------------------
#Crear funcion para leer la tabla Orders de la base de datos
def readOrders(orderNumber):
    instruction = f"Select * from Orders WHERE OrderNumber = '{orderNumber}';"
    cursor.execute(instruction)
    orders = cursor.fetchall()
    return orders
    
#Crear funcion para insertar un nuevo registro en la tabla Orders de la base de datos
def insertOrders(number,product, id):
    instruction = f"INSERT INTO Orders VALUES ('{number}','{product}','{id}');"
    cursor.execute(instruction)
    conn.commit()
    
#Crear funcion para eliminar un registro en la tabla Orders de la base de datos
def deleteOrders(orderid):
    instruction = f"DELETE from Orders WHERE OrderNumber = '{orderid}';"
    cursor.execute(instruction)
    conn.commit()

#readOrders()
#insertOrders("8374BD2746","1")
#readOrders()
#deleteOrders("8374BD2746")
#readOrders()