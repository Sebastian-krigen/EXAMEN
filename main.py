from funciones import *


while True:

    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Listado de productos.")
    print("4. Salir.")

    opciones = input("Ingrese opción: ")

    if opciones=='1':
        print("stock marca")
        marca = input("Ingrese marca a consultar: ").lower().isalpha()    
        stock_marca(marca)
    elif opciones=='2':
        print("busqueda por precio")
        p_min = validar_p_min()
        p_max = validar_p_max()
        búsqueda_precio(p_min,p_max)
    elif opciones=='3':
        ordenar_productos()
    elif opciones=='4':
        print("Programa finalizado.")
        break
    else:
        print("error elija una opcion entre (1-4)")

        
