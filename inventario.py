import datetime

inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    tipo = input("Tipo: ")
    tamaño = input("Tamaño: ")
    fecha = datetime.date.today()
    producto = {
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio,
        'tipo': tipo,
        'tamaño': tamaño,
        'fecha': fecha,
        'descripcion': ""
    }
    inventario.append(producto)
    print("Producto agregado al inventario.")

def actualizar_cantidad():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Nueva cantidad: "))
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['cantidad'] = cantidad
            print("Cantidad actualizada.")
            return
    print("Producto no encontrado.")

def buscar_producto():
    nombre = input("Nombre del producto: ")
    for producto in inventario:
        if producto['nombre'] == nombre:
            print("Producto encontrado:")
            print(producto)
            return
    print("Producto no encontrado.")

def ordenar_inventario():
    opcion = input("Ordenar por (nombre/cantidad/precio): ")
    if opcion == 'nombre':
        inventario.sort(key=lambda x: x['nombre'])
    elif opcion == 'cantidad':
        inventario.sort(key=lambda x: x['cantidad'])
    elif opcion == 'precio':
        inventario.sort(key=lambda x: x['precio'])
    else:
        print("Opción inválida.")
        return
    print("Inventario ordenado por", opcion)

def generar_informe():
    print("Generando informe de inventario...")

def calcular_valor_total():
    total = 0
    for producto in inventario:
        total += producto['cantidad'] * producto['precio']
    print("Valor total del inventario:", total)

def actualizar_descripcion():
    nombre = input("Nombre del producto: ")
    descripcion = input("Nueva descripción: ")
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['descripcion'] = descripcion
            print("Descripción actualizada.")
            return
    print("Producto no encontrado.")

def añadir_descuento():
    nombre = input("Nombre del producto: ")
    descuento = float(input("Descuento (%): "))
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['precio'] -= producto['precio'] * (descuento / 100)
            print("Descuento añadido.")
            return
    print("Producto no encontrado.")

while True:
    print("==== Sistema de Inventario ====")
    print("1. Agregar producto")
    print("2. Actualizar cantidad")
    print("3. Buscar producto")
    print("4. Ordenar inventario")
    print("5. Generar informe de inventario")
    print("6. Calcular valor total del inventario")
    print("7. Actualizar descripción del producto")
    print("8. Añadir descuento a un producto")
    print("0. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        actualizar_cantidad()
    elif opcion == '3':
        buscar_producto()
    elif opcion == '4':
        ordenar_inventario()
    elif opcion == '5':
        generar_informe()
    elif opcion == '6':
        calcular_valor_total()
    elif opcion == '7':
        actualizar_descripcion()
    elif opcion == '8':
        añadir_descuento()
    elif opcion == '0':
        break
    else:
        print("Opción inválida. Intente nuevamente.")

print("¡Gracias por usar el sistema de inventario!")
