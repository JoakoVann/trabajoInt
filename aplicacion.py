from Tad_Empresa import *
from Tad_Cola import *

empresa=CrearEmpresa()

def menu ():
    print("1. Para agregar un cliente\n")
    print("2. Para modificar un cliente\n")
    print("3. Para eliminar un cliente\n")
    print("4. Para ver el listado completo de los clientes\n")
    print("5. Para eliminar la lista de clientes por el tipo de servicio adquirido\n")
    print("6. Para aplicar descuento a clientes con 3 años de antiguedad\n")
    print("0. Para salir\n")
    op = int(input("Ingrese a continuacion la opcion que desea realizar: "))
    return op

def agregarCliente():
    cliente = crearCliente()
    num= int(input("Ingrese el numero de cliente: "))
    dni= int(input("Ingrese el dni del cliente: "))
    ape=input("Ingrese el apellido del cliente: ")
    nom=input("Ingrese el nombre del cliente: ")
    fecha=input("Ingrese la fecha de alta del cliente ddmmaaaa: ")
    service=input("Ingrese el tipo de servicio: ")
    price=float(input("Ingrese el precio del servicio contratado: "))
    cargarCliente(cliente,num,dni,ape,nom,fecha,service,price)
    AgregarCliente(empresa,cliente)

def buscarCliente(num):
    tam = Tamanio(empresa)
    for i in range (1, tam): 
        c=RecuperarCliente(empresa, i)
        if (verNumero(c) == num):
            return c
    return -1 #tomamos -1 como si el numero de cliente que se busco no se encontro

def modificarCliente(numero):
    c = buscarCliente(numero)
    if (c != -1): 
        mod = input("que aspecto desea modificar: Nombre, Apellido, DNI, Tipo de servicio (tipo) o Precio: ").lower()
        if mod == "nombre" : 
            ModiNombre(c, input("Ingrese el nuevo nombre: "))
        elif mod == "apellido":
            ModiApellido(c, input("Ingrese el nuevo apellido: "))
        elif mod == "dni":
            ModiDni(c,int(input("Ingrese el nuevo DNI: ")))
        elif mod == "tipo":
            ModiTipo(c,input("Ingrese el nuevo tipo de servicio: "))
        elif mod == "precio":
            ModiPrecio(c,float(input("Ingrese el nuevo precio del servicio: ")))
        else:
            print("El dato ingresado no es valido\n")
    else:
        print("No existe el usuario ingresado, regresando al menu\n")

def borrarCliente(numero):
    c = buscarCliente(numero)
    if (c!=-1):
        EliminarCliente(empresa,c)
        print("Cliente eliminado con exito\n")
    else: 
        print("No se encontro el cliente, regresando al menu\n")

def mostrarCliente(e):
    if(Tamanio(e) != 0):
        for i in range (0, Tamanio(e)):
            cliente = RecuperarCliente(e, i)
            print("\nNumero del cliente: ", verNumero (cliente))
            print("DNI: ", verDni (cliente))
            print("Apellido: ", verApellido (cliente))
            print("Nombre: ", verNombre (cliente))
            print("Fecha de alta: ", verFecha (cliente))
            print("Tipo de servicio contratado: ", verTipo (cliente))
            print("Precio del servicio: ", verPrecio (cliente))
            print("-------------------------------------------")
    else:
        print("-------------------------------------------")
        print("\nNo hay clientes \n")
        print("-------------------------------------------")    

def borrarServicio(e, tipo_serv):
    i = 0
    while (i < Tamanio(e)):
        cliente = RecuperarCliente(e, (i+1))
        if (verTipo(cliente) == tipo_serv):
            EliminarCliente(e, cliente)
        else:
            i+=1
    print("-------------------------------------------")
    print("\nYa no hay mas clientes con el servicio: ", tipo_serv, "\n")
    print("-------------------------------------------")

def Calcular (f,h):
    #calcula 3 años atras de la fecha de hoy
    fechaAct = int(str(h)[-4:])
    fechaServ = int(str(f)[-4:])
    print(f"año servicio {fechaServ} año act {fechaAct} resta de años {fechaAct-fechaServ}")
    #compara si la fecha de alta del cliente es posterior a tres años atras
    if (fechaAct-fechaServ) >= 3:
        return True
    else:
        return False

def descuento (e,desc):
    if(Tamanio(e) != 0):
        hoy=input("Ingrese la fecha de hoy ddmmaaaa: ")
        for i in range (1, Tamanio(e)):
            cliente = RecuperarCliente (e,i)
            if Calcular (verFecha(cliente),hoy):
                pre = verPrecio(cliente) - desc
                ModiPrecio (cliente,pre)
                print("Descuento realizado con exito\n")


print("--------------- BIENVENIDO ---------------\n")
op = menu()
while (op != 0): 
    #invoca a la funcion que elija el usuario
    if op == 1: 
        agregarCliente()
    elif op == 2: 
        numCliente = int(input("Ingrese el numero del cliente que desea modificar: "))
        modificarCliente(numCliente)
    elif op == 3:
        numCliente = int(input("Ingrese el numero del cliente que desea modificar: "))
        borrarCliente(numCliente)
    elif op == 4:
        mostrarCliente(empresa)
    elif op == 5:
        tipo_serv = str(input("ingresar el tipo de servicio: "))
        borrarServicio(empresa,tipo_serv)
    elif op == 6: 
        desc = float(input("ingrese descuento "))
        descuento(empresa,desc)
    else:
        print("Opcion incorrecta, vuelva a seleccionar otra\n")
    op = menu()