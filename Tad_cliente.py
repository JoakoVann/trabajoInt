def crearCliente ():
    cliente = [0,0,"","",0,"",0]
    return cliente


def cargarCliente (cliente,num,dni,ape,nom,fa,tipo,precio):
    cliente [0] = num
    cliente [1] = dni
    cliente [2] = ape
    cliente [3] = nom
    cliente [4] = fa
    cliente [5] = tipo
    cliente [6] = precio


def verNumero (cliente):
    return cliente [0]


def verDni (cliente):
    return cliente [1]


def verApellido (cliente):
    return cliente [2]


def verNombre (cliente):
    return cliente [3]


def verFecha (cliente):
    return cliente [4]


def verTipo (cliente):
    return cliente [5]


def verPrecio (cliente):
    return cliente [6]


def ModiNumero (cliente,otroNu):
    cliente [0] = otroNu


def ModiDni (cliente,otroDni):
    cliente [1] = otroDni


def ModiApellido (cliente,otroA):
    cliente [2] = otroA


def ModiNombre (cliente,otroNom):
    cliente [3] = otroNom


def ModiFecha (cliente,otraF):
    cliente [4] = otraF


def ModiTipo (cliente,otroT):
    cliente [5] = otroT


def ModiPrecio (cliente,otroP):
    cliente [6] = otroP


def Copiar (c1,c2):
    c2 [0] = c1 [0]
    c2 [1] = c1 [1]
    c2 [2] = c1 [2]
    c2 [3] = c1 [3]
    c2 [4] = c1 [4]
    c2 [5] = c1 [5]
    c2 [6] = c1 [6]


