class Cliente:
    def __init__(self, nombre,dni, email):
        self.nombre = nombre
        self.email = email
        self.dni = dni
    def __str__(self):
        return f'Cliente: {self.nombre} con el email {self.email} y el dni {self.dni}'

#nombre, marca, categoría y precio
class Producto:
    def __init__(self, nombre, marca, categoria, precio):
        self.nombre = nombre
        self.marca = marca
        self.categoria = categoria
        self.precio = precio
    def __str__(self):
        return f"El producto {self.nombre}, marca {self.marca}, categoría {self.categoria}, a un precio de {self.precio}"

categorias = set()
clientes = {}
lista_clientes = [] #--> Guarda objetos
lista_productos = [] #--> Guarda objetos
productos = {}

def _norm(nombre: str) -> str: #--> Para que lo que se ingrese quede en minusculas
    return nombre.strip().casefold()

#Diccionarios para almacenar clientes por nombre y email

def nuevo_prod():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        categoria = input("Ingrese la categoría del producto:")
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("El precio tiene que ser un número")

    
    """
    clave = _norm(nombre)
    if clave in productos:
        print(" Ya existe un producto con ese nombre (sin distinguir mayúsculas/minúsculas).")
        return
        """
    
    categorias.add(categoria)
    
    #productos[clave] = (marca,categoria,precio) #Para tenerlo en minusculas adentro del diccionario
    productos[nombre] = (marca,categoria,precio)
    producto =Producto(nombre,marca,categoria,precio)
    lista_productos.append(producto)
    print("Producto registrado:", str(producto))

def eliminar_prod():
        
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    
    if nombre not in productos:
        print("No existe un producto con ese nombre.")
        return
    
    datos = productos.pop(nombre)

    # Eliminar de la lista de objetos Cliente
    for c in lista_productos:
        if c.nombre == nombre:
            lista_productos.remove(c)
            break

    print(f"✅ Producto {nombre} eliminado: Marca {datos[0]}, Categoría {datos[1]}, Precio {datos[2]}")

def nuevo_cliente():
    nombre = input('Ingrese el nombre del cliente:')

    while True:
        try:
            dni = int(input('Ingrese el DNI:'))
            break
        except ValueError:
            print('Debe ingresar un número')

    while True:
        email = input('Ingrese el email:')
        if '@' not in email:
            print('El email no es correcto!')
        else:
            break
    nuevo_cliente = Cliente(nombre,dni,email)
    clientes[nombre] = (nombre, email)
    lista_clientes.append(nuevo_cliente)
    print('Nuevo cliente creado!', nuevo_cliente)
    return

def eliminar_cliente():
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    
    if nombre not in clientes:
        print("No existe un cliente con ese nombre.")
        return
    
    datos = clientes.pop(nombre)

    # Eliminar de la lista de objetos Cliente
    for c in lista_clientes:
        if c.nombre == nombre:
            lista_clientes.remove(c)
            break

    print(f"✅ Cliente eliminado: Nombre {datos[0]}, Email {datos[1]}")

def buscar_prod():
    nombre_prod = input("Ingrese el nombre del producto a buscar ")
    #clave = _norm(nombre_prod)
    
    if nombre_prod not in productos:
        print("No existe un producto con ese nombre.")
        return
    else:
        #productos[clave] = (marca,categoría,precio) --> Nombre del producto normalizado en minus
        print("El producto", nombre_prod, "Es de la marca", 
              productos[nombre_prod][0], "categoría", productos[nombre_prod][1], 
              "y precio", productos[nombre_prod][2])

def estadisticas():
    print('MENU DE OPCIONES')
    print('================')
    print("1. Cantidad de productos.")
    print("2. Categorías existentes en la ferretería.")
    print("3. Cantidad de clientes.")
    print("4. Promedio de precios de todos los productos de la ferretería.")
    print("5. Mostrar el máximo precio.")
    print("6. Mostrar el mínimo precio.")
    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        print("La cantidad de productos que hay es de:", len(productos))
    elif opcion == '2':
        print("Las categorías existentes son:", categorias)
    elif opcion == '3':
        print("La cantidad de clientes que hay es de:", len(clientes))
    elif opcion == '4':
        suma = 0
        cantidad = 0
        for precios in productos.values: #Acceder a los valores del diccionario, el for va a iterar la cantidad 
                                             #de productos que hayan en el mismo
            precio = precios[2] #Asi se itera en todas las distintas partes del diccionario, entra a cada tupla
            suma += precio
            cantidad += 1 
        promedio = suma / cantidad
        print("El promedio de los precios de los productos de la ferretería es de:", promedio)
    elif opcion == '5':
        precio_max = max(valor[2] for valor in productos.values()) #productos.values() devuelve todas las tuplas completas del diccionario
        print("El precio del producto más caro es:", precio_max) #valor[2] for valor in productos.values() lo que hace es generar 
    elif opcion == '6':                                           #una lista de todos los precios y el max toma el valor mas grande de esa lista.
        precio_min = min(valor[2] for valor in productos.values()) 
        print("El precio del producto más barato es:", precio_min)
    else:
        print('Valor de opción inválida. Ingrese un número del 1 al 6.')


def menu_opciones():
    while True:
        print('MENU DE OPCIONES')
        print('================')
        print('1. Agregar nuevo producto')
        print("2. Eliminar producto")
        print('3. Agregar nuevo cliente.')
        print('4. Eliminar cliente.')
        print('5. Buscar producto por nombre.')
        print("6. Mostrar estadísticas.")
        print('7. Salir.')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            nuevo_prod()
        elif opcion == '2':
            eliminar_prod()
        elif opcion == '3':
            nuevo_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == "5":
            buscar_prod()
        elif opcion == "6":
            estadisticas()
        elif opcion == '7':
            print('Gracias por utilizar el sistema!')
            break
        else:
            print('Valor de opción inválida. Ingrese un número del 1 al 7.')


menu_opciones()