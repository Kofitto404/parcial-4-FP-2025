comprador = []
funcion1 = []
funcion2 = []
catsviernes = 150
viernescomprado = 0
catssabado = 180
sabadocomprado = 0

while True:
    print("TOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats")
    print("2.- Cambio de función")
    print("3.- Mostrar stock de funciones")
    print("4.- Salir")

    opcion = input(f"Seleccionar opcion\n\t> ")

# COMPRAR BOLETO

    if opcion == "1":
        nombre = input(f"Nombre del comprador\n\t> ").strip().lower()
        if nombre not in comprador:
            comprador.append(nombre)
            print("Seleccione la función")
            print(f"Cats 1 = {catsviernes} boletos")
            print(f"Cats 2 = {catssabado} bletos")

            opcion2 = input(f"Seleccione una función\n\t> ")
            if opcion2 == "1":
                if catsviernes > 0:
                    viernescomprado += 1
                    catsviernes -= 1
                    funcion1.append(nombre)
                    print("Entrada registrada en función 1")
                else:
                    print("No quedan boletos!!!")
            if opcion2 == "2":
                if catssabado > 0:
                    sabadocomprado += 1
                    catssabado -= 1
                    funcion2.append(nombre)
                    print("Entrada registrada en función 2")
                else:
                    print("No quedan boletos!!!")
        else:
            print("Solo un boleto por persona!")

# CAMBIO DE FUNCION

    elif opcion == "2":
        nombre = input(f"Nombre del comprador\n\t> ").strip().lower()
        # De 1 a la 2
        if nombre in funcion1:
            yn1 = input("Desea cambiar de funcion 1 a 2? (Y/N): ")
            yn1fix = yn1.lower()
            if yn1fix == "y":
                sabadocomprado += 1
                catssabado -= 1
                viernescomprado -= 1
                catsviernes += 1
                funcion1.remove(nombre)
                funcion2.append(nombre)
                print("Cambio realizado con exito")
            if yn1fix == "n":
                print("Cancelado")
        # De 2 a 1
        elif nombre in funcion2:
            yn2 = input("Desea cambiar de funcion 2 a 1? (Y/N): ")
            yn2fix = yn2.lower()
            if yn2fix == "y":
                sabadocomprado -= 1
                catssabado += 1
                viernescomprado += 1
                catsviernes -= 1
                funcion2.remove(nombre)
                funcion1.append(nombre)
                print("Cambio realizado con exito")
            if yn2fix == "n":
                print("Cancelado")
        else:
            print("El nombre no esta registrado en ninguna funcion")


# MOSTRAR STOCK

    elif opcion == "3":
        print("-- Stock de Funciones --")
        print(f"Función 1 (Viernes): Disponibles {catsviernes}, Vendidas {viernescomprado}")
        print(f"Función 2 (Sabado): Disponibles {catssabado}, Vendidas {sabadocomprado}")
        
# SALIR

    elif opcion == "4":
        print("Adios...")
        print(comprador)
        break
    else:
        print("Opcion Invalida")
        