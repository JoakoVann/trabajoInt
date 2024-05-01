from Tad_cliente import *
from Tad_Empresa import *


def CrearCola ():
    cola = []
    return cola


def EsVacia (cola):
    return len (cola) == 0


def Encolar (cola,Elem):
    cola.append (Elem)


def Desencolar (cola):
    e = cola [0]
    del cola [0]
    return e


def tamanio (cola):
    return len (cola)


def Copiar (cola1,cola2):
    aux = CrearCola ()
    while not EsVacia (cola2):
        e = Desencolar (cola2)
        Encolar (aux,e)
    while not EsVacia (aux):
        e = Desencolar (aux)
        Encolar (cola1,e)
        Encolar (cola2,e)


