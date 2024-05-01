# trabajoInt


## Especificacion del Tad cliente 

Guarda los datos personales de cada cliente, incluyendo su numero de cliente, DNI, apellido, 	 nombre, fecha de alta, tipo de servicio contratado y precio del servicio.

crearCliente ():
#crea y retorna un cliente sin datos

cargarCliente (cliente,num,dni,ape,nom,fa,tipo,precio):
#carga los datos del cliente

verNumero (cliente):
#retorna el numero de cliente

verDni (cliente):
#retorna el DNI del cliente

verApellido (cliente):
#retorna el apellido del cliente

verNombre (cliente):
#retorna el nombre del cliente

verFecha (cliente):
#retorna la fecha de alta del cliente

verTipo (cliente):
#retorna el tipo de servicio contratado por el cliente

verPrecio (cliente):
#retorna el precio del servicio

ModiNumero (cliente,otroNu):
#modifica el numero de cliente

ModiDni (cliente,otroDni):
#modifica el DNI del cliente

ModiApellido (cliente,otroA):
#modifica el apellido del cliente

ModiNombre (cliente,otroNom):
#modifica el nombre del cliente

ModiFecha (cliente,otraF):
#modifica la fecha de alta del cliente

ModiTipo (cliente,otroT):
#modifica el tipo de servicio contratado por el cliente

ModiPrecio (cliente,otroP):
#modifica el precio del servicio

Copiar (c1,c2):
#copia los datos del cliente 1 en el cliente 2


## Especificacion del TAD Empresa

Guarda la informacion de sus clientes registrados en el servicio que brinda.

CrearEmpresa ():
#crea y retorna la empresa sin clientes

AgregarCliente (E,cliente):
#agrega al cliente a la empresa

EliminarCliente (E,cliente):
#elimina al cliente de la empresa

Tamanio (E):
#retorna la cantidad de clientes dentro de la empresa

RecuperarCliente (E,i):
#retorna el cliente de la posicion i-esima

Existe (E,cliente):
#retorna true o false si el cliente pertenece o no a la empresa


## Especificacion TAD Cola

CrearCola ():
#crea y retorna una cola vacia

EsVacia (cola):
#retorna verdadero si la cola no tiene elementos

Encolar (cola,Elem):
#agrega un elemento al final de la cola

Desencolar (cola):
#elimina y retorna el primer elemento de la cola

Tamanio (cola):
#retorna la cantidad de elementos de la cola

Copiar (cola1,cola2):
#copia la cola2 en la cola1

