import random
from models import customer as sqlserver
from models import inventario as sqlite

def generarnumero():
    return random.randint(1000, 9999999)

print('Bienvenid@, porfavor identificate')
user = input()
username = sqlserver.readCustomer(int(user))

print('Que deseas Tomar?')
gaseosas = sqlite.readGaseosa()
print(sqlite.readGaseosa())
gaseosa = input()

cantidad = sqlite.readGaseosaCantidad(gaseosa)
nuevaCantidad = int(cantidad)-1

sqlite.updateGaseosa(gaseosa,nuevaCantidad)



sqlserver.insertOrders(generarnumero(),gaseosa,user)