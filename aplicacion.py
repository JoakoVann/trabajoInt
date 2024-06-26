from Tad_Empresa import *
from Tad_Cola import *
import datetime


empresa = CrearEmpresa()
cliente = crearCliente()
cliente1 = crearCliente()
cliente2 = crearCliente()
cargarCliente(cliente, 1, 242532, "ch", "va", datetime.datetime(2024,4,15), "ele", 2000)
cargarCliente(cliente1, 2, 352532, "bf", "jo", datetime.datetime(2024,4,29), "ele", 3000)
cargarCliente(cliente2, 3, 672532, "cj", "gr", datetime.datetime(2024,4,9), "fer", 4000)
AgregarCliente(empresa, cliente)
AgregarCliente(empresa, cliente1)
AgregarCliente(empresa, cliente2)

def menu ():
    print("1. Para agregar un cliente\n")
    print("2. Para modificar un cliente\n")
    print("3. Para eliminar un cliente\n")
    print("4. Para ver el listado completo de los clientes\n")
    print("5. Para eliminar la lista de clientes por el tipo de servicio adquirido\n")
    print("6. Para aplicar descuento a clientes con 3 años de antiguedad\n")
    print("7. Para mostrar listado de clientes con promoción vigente\n")
    print("8. Para generar una cola con las altas de los clientes del último mes\n")
    print("0. Para salir\n")
    op = int(input("Ingrese a continuacion la opcion que desea realizar: "))
    return op

def agregarCliente(): #Punto a
    cliente = crearCliente()
    num= int(input("Ingrese el numero de cliente: "))
    dni= int(input("Ingrese el dni del cliente: "))
    ape=input("Ingrese el apellido del cliente: ")
    nom=input("Ingrese el nombre del cliente: ")
    fecha=input("Ingrese la fecha de alta del cliente ddmmaaaa: ")
    service=input("Ingrese el tipo de servicio: ")
    price=float(input("Ingrese el precio del servicio contratado: "))
    cargarCliente(cliente,num,dni,ape,nom,formatearFecha(fecha),service,price)
    AgregarCliente(empresa,cliente)

def buscarCliente(num):
    tam = Tamanio(empresa)
    encontro = True
    for i in range (0, tam): 
        clienteB=RecuperarCliente(empresa, (i+1))
        if (verNumero(clienteB) == num):
            return clienteB
            break
    return False #tomamos false como si el numero de cliente que se busca no se encontro

def modificarCliente(numero): #Punto a
    c = buscarCliente(numero)
    if c == False:
        print("-------------------------------------------")
        print("No existe cliente con el numero ingresado")
        print("-------------------------------------------")
    else:
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

def borrarCliente(numero): #Punto a
    cliente = buscarCliente(numero)
    if  cliente == False :
        print("-------------------------------------------")
        print("No existe cliente con el numero ingresado")
        print("-------------------------------------------")
    else: 
        EliminarCliente(empresa,cliente)
        print("-------------------------------------------")
        print("\nCliente eliminado con exito\n")
        print("-------------------------------------------")
        
def mostrarCliente(e):#Punto b
    if(Tamanio(e) != 0):
        for i in range (0, Tamanio(e)):
            cliente = RecuperarCliente(e, (i+1))
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


def borrarServicio(e, tipo_serv): #Punto c
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

def formatearFecha(f): #funcion que guarda la fecha en la que se anoto el cliente 
    a= int(f[4:])
    m=int(f[2:4])
    d=int(f[0:2])
    fecha = datetime.datetime(a,m,d)
    return fecha

def calcularFechaDescuento (fechaCliente,hoy,op):
    if op == 6: 
        anioAtras = hoy - datetime.timedelta(days=1095) #retorna 3 años atras a la fecha actual
        if (fechaCliente < anioAtras): 
            return True
        else:
            return False
    elif op == 7:
        mesesAtras = hoy - datetime.timedelta(days=90)#retorna 3 meses atras a la fecha actual
        if (fechaCliente >= mesesAtras):
            return True #si es mayor nos da true 
        else:
            return False
    else:
        return False #si se llega a esta instancia es pq no hay clientes o la fecha es invalida

def descuento (e,d,op): #Punto d
    if(Tamanio(e) != 0):
        hoy = datetime.datetime.now()
        for i in range (0, Tamanio(e)):
            c=RecuperarCliente (e,i + 1)
            if calcularFechaDescuento(verFecha(c),hoy,op):
                pre = verPrecio(c)-d
                ModiPrecio(c,pre)
        print("-------------------------------------------")
        print("\nSe ha aplicado el descuento\n")
        print("-------------------------------------------")
    else:
        print("-------------------------------------------")
        print("\nNo hay clientes \n")
        print("-------------------------------------------")

def promocion (e,op): #Punto e
    if(Tamanio(e) != 0):
        hoy=datetime.datetime.now()
        aux = True
        for i in range (0, Tamanio(e)):
            c=RecuperarCliente (e,i) 
            #compara si la fecha de alta del cliente es posterior a tres meses
            if (calcularFechaDescuento(verFecha(c),hoy,op)):
                print("\nNumero del cliente: ", verNumero(c))
                print("DNI: ", verDni(c))
                print("Apellido: ", verApellido(c))
                print("Nombre: ", verNombre(c))
                print("Fecha de alta: ", verFecha(c))
                print("Tipo de servicio contratado: ", verTipo(c))
                print("Precio del servicio: ", verPrecio(c))
                print("\n-------------------------------------------")
                aux = False
        if(aux):
            print("-------------------------------------------")
            print("\nNo hay clientes con promocion \n")
            print("-------------------------------------------")


    else:
        print("-------------------------------------------")
        print("\nNo hay clientes \n")
        print("-------------------------------------------")


def clientesDelMesAnterior(e): 
    clientesMes = CrearCola()
    if(Tamanio(e) != 0):
        hoy= datetime.datetime.now()
        mesAnt = hoy - datetime.timedelta(days=30) #es una aprox 
        aux = False
        cantC = 0
        recaudado = 0
        for i in range (0, Tamanio(e)):
            cliente = RecuperarCliente(e, i+1)
            if (verFecha(cliente) >= mesAnt):
                aux = True
                c = [verDni(cliente), verPrecio(cliente)]
                Encolar(clientesMes, c)
                cantC += 1
                recaudado += verPrecio(cliente)
        if (aux == False):
            print("-------------------------------------------")
            print("\nNo hay clientes este ultimo mes\n")
            print("-------------------------------------------")
        else: 
            print("-------------------------------------------")
            print("\nEl ultimo mes se registraron: ", cantC)
            print("Los ingresos del ultimo mes fueron: ", recaudado,"\n")
            print("-------------------------------------------")
    else:
        print("-------------------------------------------")
        print("\nNo hay clientes con promos\n")
        print("-------------------------------------------")
    return clientesMes



print("--------------- BIENVENIDO ---------------\n")
#cambiarOrdenFecha(20052001)
op = menu()
while (op != 0): 
    #invoca a la funcion que elija el usuario
    if op == 1: 
        agregarCliente()
    elif op == 2: 
        numCliente = int(input("Ingrese el numero del cliente que desea modificar: "))
        modificarCliente(numCliente)
    elif op == 3:
        numCliente = int(input("Ingrese el numero del cliente que desea eliminar: "))
        borrarCliente(numCliente)
    elif op == 4:
        mostrarCliente(empresa)
    elif op == 5:
        tipo_serv = str(input("ingresar el tipo de servicio: "))
        borrarServicio(empresa,tipo_serv)    
    elif op == 6: 
        des = float(input("ingrese descuento: "))
        descuento (empresa,des,op)
    elif op == 7: 
        promocion (empresa,op)
    elif op == 8:
        colaClientesM =  clientesDelMesAnterior(empresa)
    else:
        print("Opcion incorrecta, vuelva a seleccionar otra\n")
    op = int(menu())
