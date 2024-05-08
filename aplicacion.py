from Tad_Empresa import *
from Tad_Cola import *

empresa=CrearEmpresa()
cliente = crearCliente()
cliente1 = crearCliente()
cliente2 = crearCliente()
cargarCliente(cliente, 1, 242532, "ch", "va", 20052024, "ele", 2000)
cargarCliente(cliente1, 2, 352532, "bf", "jo", 11052024, "ele", 3000)
cargarCliente(cliente2, 3, 672532, "cj", "gr", 24052024, "fer", 4000)
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

def agregarCliente():
    cliente = crearCliente()
    num= int(input("Ingrese el numero de cliente: "))
    dni= int(input("Ingrese el dni del cliente: "))
    ape=input("Ingrese el apellido del cliente: ")
    nom=input("Ingrese el nombre del cliente: ")
    fecha=int(input("Ingrese la fecha de alta del cliente ddmmaaaa: "))
    service=input("Ingrese el tipo de servicio: ")
    price=float(input("Ingrese el precio del servicio contratado: "))
    cargarCliente(cliente,num,dni,ape,nom,fecha,service,price)
    AgregarCliente(empresa,cliente)

def buscarCliente(num):
    tam = Tamanio(empresa)
    for i in range (0, tam): 
        c=RecuperarCliente(empresa, i)
        if (verNumero(c) == num):
            return c
    return -1 #tomamos -1 como si el numero de cliente que se busco no se encontro

def modificarCliente(numero):
    c = buscarCliente(numero)
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

def borrarCliente(numero):
    c = RecuperarCliente(empresa, numero)
    if (Existe(empresa,c)):
        EliminarCliente(empresa,c)
        print("Cliente eliminado con exito\n")
    else: 
        print("No se encontro el cliente, volviendo al menu\n")

def mostrarCliente(e):
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


def cambiarOrdenFecha(f):
    f = str(f)
    #este if esta pq si hay un dia que empiece con 0 el strin no toma el 0 inicial
    if len(f) < 8:
        o = "0"
        f = o + f
    aux = f[4:] + f[2:4] + f[0:2]
    aux = int(aux)
    return aux

def calcularFechaDescuento (f,h):
    #calcula 3 años atras de la fecha de hoy
    #puede que haya que sumarle 3 a la fecha del cliente en vez de restar a la fecha actual
    f = cambiarOrdenFecha(f)
    h = str(h)
    a = int (h[4:]) -3
    a2 = str (a)
    t = a2 + h[2:4] + h[:2]
    t = int(t)
    #compara si la fecha de alta del cliente es posterior a tres años atras
    if f > t:
        return True
    else:
        return False
    

def descuento (e,d):
    if(Tamanio(e) != 0):
        hoy = int(input("Ingrese la fecha de hoy ddmmaaaa: "))
        for i in range (0, Tamanio(e)):
            c=RecuperarCliente (e,i + 1)
            if not calcularFechaDescuento(verFecha(c),hoy):
                pre = verPrecio(c)-d
                ModiPrecio(c,pre)
        print("-------------------------------------------")
        print("\nSe ha aplicado el descuento\n")
        print("-------------------------------------------")
    else:
        print("-------------------------------------------")
        print("\nNo hay clientes \n")
        print("-------------------------------------------")

def promocion (e):
    if(Tamanio(e) != 0):
        hoy=input("Ingrese la fecha de hoy ddmmaaaa: ")
        #calcula 3 meses atras de la fecha de hoy
        a = int (hoy[2:4]) -3
        a = str (a)
        # 05 - 3 = 2 => hay que agregarle un 0 para no romper la fecha
        a = "0" + a
        t = hoy[4:] + a + hoy[0:2]
        t = int(t)
       
        for i in range (1, Tamanio(e)):
            c=RecuperarCliente (e,i) 
            #compara si la fecha de alta del cliente es posterior a tres meses
            if (cambiarOrdenFecha(verFecha(c)) >= t):
                print("\nNumero del cliente: ", verNumero (c))
                print("DNI: ", verDni (c))
                print("Apellido: ", verApellido (c))
                print("Nombre: ", verNombre (c))
                print("Fecha de alta: ", verFecha (c))
                print("Tipo de servicio contratado: ", verTipo(c))
                print("Precio del servicio: ", verPrecio (c))
                print("\n-------------------------------------------")
            else:
                print("-------------------------------------------")
                print("\nNo hay clientes \n")
                print("-------------------------------------------")


def clientesDelMesAnterior(e):
    clientesMes = CrearCola()
    if(Tamanio(e) != 0):
        hoy= input("Ingrese la fecha de hoy ddmmaaaa: ")
        mesAnt = str(int(hoy[2:4]) - 1) + hoy[4:]
        mesAnt = int(mesAnt)
        aux = False
        cantC = 0
        recaudado = 0
        for i in range (0, Tamanio(e)):
            cliente = RecuperarCliente(e, i)
            mCliente = str(verFecha(cliente))
            if(len(mCliente) != 8):
                mCliente = "0" + mCliente
            mCliente = int(mCliente[2:])
            
            if (mesAnt == mCliente):
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
        des = float(input("ingrese descuento: "))
        descuento (empresa,des)
    elif op == 7: 
        promocion (empresa)
    elif op == 8:
        colaClientesM =  clientesDelMesAnterior(empresa)
    else:
        print("Opcion incorrecta, vuelva a seleccionar otra\n")
    op = menu()