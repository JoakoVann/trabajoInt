from Tad_cliente import *

def CrearEmpresa ():
    E = []
    return E


def AgregarCliente (E,cliente):
    E.append (cliente)


def EliminarCliente (E,cliente):
    E.remove (cliente)


def Tamanio (E):
    return len (E)


def RecuperarCliente (E,i):
    return E[i-1]


def Existe (E,cliente):
    return cliente in E

