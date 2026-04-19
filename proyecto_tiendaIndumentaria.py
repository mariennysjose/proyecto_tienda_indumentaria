def menuClientes():
    print("1.- Crear cliente")
    print("2.- Buscar cliente")
    print("3.- Mostrar todos los clientes")
    print("4.- Eliminar cliente")
    print("5.- Modificar cliente")
    return int(input("Selecciona una opción: "))

def menuPrendas():
    print("1.- Agregar prenda al cliente")
    print("2.- Buscar prenda del cliente")
    print("3.- Mostrar prendas del cliente")
    print("4.- Eliminar prenda")
    print("5.- Modificar prenda")
    return int(input("Selecciona una opción: "))

def menuPrincipal():
    print("BIENVENIDA/O A LA TIENDA DE INDUMENTARIA FLORES BOUTIQUE")
    print("--- MENÚ PRINCIPAL ---")
    print("1.- clientes")
    print("2.- prendas del cliente")
    print("3.- Mostrar total de prendas registradas")
    print("9.- Salir")
    return int(input("Selecciona una opción: "))
    
    
def contarPrendas(tienda):
    total = 0
    for cliente in tienda.values():
        total += len(cliente["Prendas"])
    print(f"Total de prendas registradas: {total}")


def creaCliente():
    dni = int(input("DNI: "))
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección: ")
    return dni, {
        "Nombre": nombre,
        "Direccion": direccion,
        "Prendas": []
    }


def buscaCliente(tienda):
    dni = int(input("Buscar cliente por DNI: "))
    if dni in tienda:
        print("Cliente encontrado:", tienda[dni])
        return dni, 1
    else:
        print("Cliente no encontrado.")
        return dni, 0


def creaPrenda():
    nombre = input("Nombre de la prenda: ")
    talle = input("Talle: ")
    color = input("Color: ")
    return {
        "Nombre": nombre,
        "Talle": talle,
        "Color": color
    }


def buscaPrenda(dni, tienda):
    nombrePrenda = input("Nombre de la prenda a buscar: ")
    for prenda in tienda[dni]["Prendas"]:
        if prenda["Nombre"] == nombrePrenda:
            index = tienda[dni]["Prendas"].index(prenda)
            print("Prenda encontrada:", prenda)
            return nombrePrenda, 1, index
    print("Prenda no encontrada.")
    return nombrePrenda, 0, -1


def sistemaClientes(tienda):
    opcion = menuClientes()
    if opcion == 1:
        dni, cliente = creaCliente()
        tienda[dni] = cliente
        print("Cliente creado correctamente.")
    elif opcion == 2:
        buscaCliente(tienda)
    elif opcion == 3:
        print("\n--- LISTA DE CLIENTES ---")
        for dni, datos in tienda.items():
            print(f"{dni}: {datos}")
    elif opcion == 4:
        dni, existe = buscaCliente(tienda)
        if existe:
            tienda.pop(dni)
            print("Cliente eliminado.")
    elif opcion == 5:
        dni, existe = buscaCliente(tienda)
        if existe:
            _, nuevo_cliente = creaCliente()
            tienda[dni] = nuevo_cliente
            print("Cliente modificado.")


def sistemaPrendas(tienda):
    opcion = menuPrendas()
    if opcion == 1:
        dni, existe = buscaCliente(tienda)
        if existe:
            prenda = creaPrenda()
            tienda[dni]["Prendas"].append(prenda)
            print("Prenda agregada al cliente.")
    elif opcion == 2:
        dni, existe = buscaCliente(tienda)
        if existe:
            buscaPrenda(dni, tienda)
    elif opcion == 3:
        dni, existe = buscaCliente(tienda)
        if existe:
            print("\n--- PRENDAS DEL CLIENTE ---")
            for prenda in tienda[dni]["Prendas"]:
                print(prenda)
    elif opcion == 4:
        dni, existe = buscaCliente(tienda)
        if existe:
            _, encontrada, index = buscaPrenda(dni, tienda)
            if encontrada:
                tienda[dni]["Prendas"].pop(index)
                print("Prenda eliminada.")
    elif opcion == 5:
        dni, existe = buscaCliente(tienda)
        if existe:
            _, encontrada, index = buscaPrenda(dni, tienda)
            if encontrada:
                nuevo_talle = input("Nuevo talle: ")
                nuevo_color = input("Nuevo color: ")
                tienda[dni]["Prendas"][index]["Talle"] = nuevo_talle
                tienda[dni]["Prendas"][index]["Color"] = nuevo_color
                print("Prenda modificada.")


tienda = {}
opcion = 0
while opcion != 9:
    opcion = menuPrincipal()
    if opcion == 1:
        sistemaClientes(tienda)
    elif opcion == 2:
        sistemaPrendas(tienda)
    elif opcion == 3:
        contarPrendas(tienda)
print("Programa finalizado.")