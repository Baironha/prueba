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
            print("5. Menu de usuarios")
            print("6. Salir")
            
            
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

            elif opcion == "5" :
                print()

                print("\n-----menu de usuarios-----")
                print("a. usuarios")
                print("b. mensaje de parte de los trabajadores")
                print("c. calculadora")
                print("d. salir")
                print()

                option_usu = str(input("Digite la letra de la opcion que desea selccionar: "))
                usuarios=[
                    {
                        "nombre": "jackson",
                        "peso": "75kg",
                        "edad": "22"
                    },
                    {
                        "nombre": "caled",
                        "peso": "75kg",
                        "edad": "21"
                    }
                ]
                if option_usu == "a" :
                    def mostrar_productos():
                        print("\nLISTA DE USUARIOS:") #\n ayuda a dar un salto de linea
                    for usu in usuarios:
                        print(usuarios)
                    print()

                elif option_usu == "b":
                    print("\n --mensaje--")
                    print("ERES LO MAXIMO, TU PUEDES")

                elif option_usu == "c":
                    print("\n___calculadora___")
                    print("1. sumar")
                    print("2. restar")
                    print("3. multiplicar")
                    print("4. dividir")
                    print("5. salir")

                    seleccion =int(input("ingrese el numero de la opcion que desea utilizar: "))

                    if seleccion == 1 :
                        while True:
                            num1 = float(input("Ingrese un numero a sumar: "))
                            num2 = float(input("Ingrese un numero a sumar: "))

                            def sumando(num1,num2):
                                result= num1 + num2
                                return result

                            resultado = sumando(num1 , num2)
                            print("resultado: ",resultado)

                            salir =str(input("Digite x para salir y si para contimuar: "))
                            if salir.lower() != "si":
                                break
                        
                    elif seleccion == 2 :
                        while True:
                            res1 = int(input("Ingrese un numero a restar: "))
                            res2 = int(input("Ingrese un numero a restar: "))

                            def resta(res1, res2):
                                restando = res1-res2
                                return restando

                            result_resta= resta(res1, res2)
                            print("resultado: ",result_resta)
                            salir =str(input("Digite x para salir y si para contimuar: "))
                            if salir.lower() != "si":
                                break

                        

                    elif seleccion == 3 :
                        while True :
                            digito1 = int(input("ingrese un numero a multiplicar: "))
                            digito2 = int(input("Ingrese un numero a multiplicar: "))

                            def multi(digito1, digito2):
                                multiplicacion = digito1 * digito2
                                return multiplicacion

                            total =multi(digito1, digito2)
                            print ("resultado: ",total)
                            salir =str(input("Digite x para salir y si para contimuar: "))
                            if salir.lower() != "si":
                                break
                            

                    elif seleccion == 4 :
                        while True:
                            div1 = int(input("Ingrese un numero a dividir: "))
                            div2 = int(input("Ingrese un numero a dividir: "))

                            def divi(div1, div2):
                                division= div1 / div2
                                return division

                            total_divi = divi(div1, div2)
                            print("resultado",total_divi)
                            salir =str(input("Digite x para salir y si para contimuar: "))
                            if salir.lower() != "si":
                                break
                    elif seleccion == 5:
                        break

                elif option_usu == "d" :
                    break
                else :
                    continue
            
            elif opcion == "6":
                print("\nCERRANDO SESIÓN...")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

        break  # Sale del login si el usuario cierra sesión

    else:
        print("\n Usuario su nombre o contraseña son incorrectos.Por favor Intente nuevamente.")



