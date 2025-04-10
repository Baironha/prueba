# Credenciales de acceso
name_real = "juan"
contra_real = "2525"  # Cambié a string para que coincida con input

# Lista de productos (inicia con uno)
productos = [{
    "id": 1,
    "nombre": "Air Max",
    "talla": 8,
    "color": "Blanco",
    "cantidad": 22
}]

# Función para mostrar productos
def mostrar_productos():
    print("\nLISTA DE PRODUCTOS:") #\n ayuda a dar un salto de linea
    for producto in productos:
        print(producto)
    print()

# Función para agregar un producto con validación por ciclo
def agregar_producto():
    print("\nAGREGAR PRODUCTO")
    while True:# ciclo para Validar ID
        id_input = input("ID: ")
        if id_input.isdigit():
            id_ = int(id_input)
            break
        else:
            print("ID inválido. Debe ser un número entero.")

    # Nombre (se permite cualquier texto)
    nombre = input("Nombre: ")

    
    while True: # ciclo Validar talla
        talla_input = input("Talla: ")
        if talla_input.isdigit():
            talla = int(talla_input)
            break
        else:
            print("Talla inválida. Debe ser un número.")


    # Color del zapato
    color = input("Color: ")


    # Validar cantidad
    while True:
        cantidad_input = input("Cantidad: ")
        if cantidad_input.isdigit():
            cantidad = int(cantidad_input)
            break
        else:
            print("Cantidad inválida. Debe ser un número.")

    productos.append({
        "id": id_,
        "nombre": nombre,
        "talla": talla,
        "color": color,
        "cantidad": cantidad
    })

    print("Producto agregado con éxito.\n")

# Función para eliminar un producto por ID
def eliminar_producto():
    print("\nELIMINAR PRODUCTO")
    while True:
        id_input = input("Ingrese el ID del producto a eliminar: ")
        if id_input.isdigit():
            id_ = int(id_input)
            break
        else:
            print("ID inválido. Intente de nuevo.")
    
    for producto in productos:
        if producto["id"] == id_:
            productos.remove(producto)
            print("Producto eliminado con éxito.\n")
            return
    print("No se encontró un producto con ese ID.\n")

# LOGIN con validación de nombre y contraseña
while True:
    print("\nLOGIN ADMIN")
    name = input("Ingrese su nombre: ")
    contra = input("Ingrese su contraseña: ")

    if name == name_real and contra == contra_real: # validacion para el login
        print("\nACCESO PERMITIDO")
        
        # Menú principal
        while True:
            print("\n---------- MENÚ PRINCIPAL ----------")
            print("1. Mostrar productos")
            print("2. Agregar producto")
            print("3. Eliminar producto")
            print("4. Motívate")
            print("5. Salir")
            
            opcion = input("Ingrese el número de la opción: ")

            if opcion == "1":
                mostrar_productos()

            elif opcion == "2":
                agregar_producto()

            elif opcion == "3":
                eliminar_producto()

            elif opcion == "4":
                print("\n ¡ERES LO MÁXIMO MI AMIGO! TÚ PUEDES CON TODO ")
                print("Ten paciencia, date tu tiempo y lo lograrás.")
                print("Porque si dios existe le gustaria que te hubieras un poco de toda esa fe que le tienes a el")
                seguir = input("¿Deseas volver al menú principal? (si/no): ")
                if seguir.lower() != "si":
                    break

            elif opcion == "5":
                print("\nCERRANDO SESIÓN...")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

        break  # Sale del login si el usuario cierra sesión

    else:
        print("\n Usuario su nombre o contraseña son incorrectos.Por favor Intente nuevamente.")
