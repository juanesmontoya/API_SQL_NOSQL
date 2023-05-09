import random
from models import customer as sqlserver
from models import inventario as sqlite

def generarnumero():
    return random.randint(1000, 9999999)

def servicio(username):
    user = sqlserver.readCustomer(str(username))
    print('Que deseas Tomar?   (Digita el nombre)')
    print(sqlite.readGaseosa())
    gaseosa = input()
    cantidad = sqlite.readGaseosaCantidad(gaseosa)
    nuevaCantidad = int(cantidad)-1
    sqlite.updateGaseosa(gaseosa,nuevaCantidad)
    numeroOrden = str(generarnumero())
    sqlserver.insertOrders(numeroOrden,gaseosa,user[0][0])
    print("Registro almacenado.")
    print(sqlserver.readOrders(numeroOrden))
    
def registro(name,phone):
    print("Cliente no registrado, porfavor digita tu nombre: ")
    name = input()
    print("Digita tu numero de telefono: ")
    phone = input()
    sqlserver.insertCustomer(name,phone)

def start():
    print('Bienvenid@, porfavor identificate')
    username = input()
    user = sqlserver.readCustomer(str(username))

    if user:
        servicio(username)
    else:
        print('Registro')
        print("El usuario no esta registrado")
        print("Digita tu numero de telefono: (Con indicativo, sin espacios ni puntos)")
        phone = input()
        sqlserver.insertCustomer(username,phone)
        servicio(username)
        
start()