#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]

stock = {
'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca(marca):
    contador = 0
    for p in stock:
        if marca==stock[p][0]:
            contador += 1
        print(f"El stock es: {contador}")

def búsqueda_precio(p_min, p_max):
    contador = 0
    for p in productos:
        if p_min==productos[p][0]>=0 and p_max==productos[p][0]:
            contador += 1
    print(f"Los notebooks entre los precios consultados son: {contador}")

#HP - 8475HD - 8GB - 1T
#Acer - 2175HD - 4GB - 512GB
#Asus - JjfFHD - 16GB - 256GB:

def ordenar_productos():
    while True:
        marca = validar_marca()
        for m in productos:
            if marca==productos[m][0]:
                return marca
            else:
                print("“No hay notebook disponibles para mostrar”")   
              
        modelo = input("ingrese modelo: ")
        for m in productos:
            if modelo==productos[m][0]:
                return modelo
            else:
                print("“No hay notebook disponibles para mostrar”")
    
        ram = input("ingrese ram: ")
        for r in productos:
            if ram==productos[r][2]:
                return ram
            else:
                print("“No hay notebook disponibles para mostrar”")
    
        disco = input("ingrese disco: ")
        for d in productos:
            if disco==productos[d][3]:
                return disco
            else:
                print("“No hay notebook disponibles para mostrar”")
    
        print(f"orden de los productos: {marca} - {modelo} - {ram} - {disco}")


#validaciones con try except:
def validar_p_min():
    while True:
        try:
            p_min = int(input("ingrese precio mínimo: "))
            if p_min>=0:
                return
            print("“Debe ingresar valores enteros!!")
        except:
            print("No hay notebooks en ese rango de precios.")

def validar_p_max():
    while True:
        try:
            p_max = int(input("ingrese precio maximo: "))
            if p_max>=0:
                return
            print("“Debe ingresar valores enteros!!")
        except:
            print("No hay notebooks en ese rango de precios.")

def validar_marca():
    while True:
        try:
            marca = input("ingrese marca: ")
            if marca==len(marca)>=2:
                return marca
            print("opcion invalida")
        except:
            print("debe escribir letras")