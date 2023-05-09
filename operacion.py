#El dueño de la licorera "El guaracheo", lleva un registro manual de lo que consumen sus clientes. Desea realizar un estudio para verificar
#que productos son los mas vendidos y que clientes son los que mas consumen. Para esto, desea tener un registro de su inventario y sus clientes.
#Al igual que registrar cada consumo de cada cliente.

import random
from models import customer as sqlserver
from models import inventario as sqlite

#generar un numero aleatorio que funcione como numero de orden.
def generarnumero():
    return random.randint(1000, 9999999)

#almacena el servicio de cada cliente.
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
    print("Esta es tu orden: "+sqlserver.readOrders(numeroOrden))

#almacena el registro de un nuevo cliente.
def registro(name,phone):
    sqlserver.insertCustomer(name,phone)

#valida un cliente, en caso tal de no existir lo crea. Y por ultimo, toma el servicio y lo almacena como orden.
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
        registro(username,phone)
        servicio(username)
        
start()