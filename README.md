# Ispc-emygut-2022
#--------------------------------Funciones--------------------------------------

# Funcion sumar 3 valores
def suma_3_parametros():
    a=input("Ingrese el 1° numero: ")
    b=input("Ingrese el 2° numero: ")
    c=input("Ingrese el 3° numero: ")
    print("El resutado de la suma es:",(float(a)+float(b)+float(c)))


# Funcion restar 2 valores
def resta_2_parametros():
    a=input("Ingrese el 1° numero: ")
    b=input("Ingrese el 2° numero: ")
    print("El resutado de la resta es:",(float(a)-float(b)))

# Funcion producto 4 valores
def producto_4_parametros():
    a=input("Ingrese el 1° numero: ")
    b=input("Ingrese el 2° numero: ")
    c=input("Ingrese el 3° numero: ")
    d=input("Ingrese el 4° numero: ")
    print("El producto es:",(float(a)*float(b)*float(c)*float(d)))

# Funcion cociente 2 valores
def cociente_2_parametros():
    a=input("Ingrese el 1° numero: ")
    b=input("Ingrese el 2° numero: ")
    print("El cociente es:",(float(a)/float(b)))
#-----------------------Operaciones segun opcion elegida ----------------------------

def main() :
    opcion_elegida = 0
    while opcion_elegida != 9:
        print("Hola, selecione la operacion que desea realizar\n 1 - Sumar\n 2 - Restar\n 3 - Multiplicar\n 4 - Dividir\n 9 - Salir\n  ")
        opcion_elegida = input('Elegir opcion :  ')
        if int(opcion_elegida) == 1:
            suma_3_parametros()
        if int(opcion_elegida) == 2:
            resta_2_parametros()
        if int(opcion_elegida) == 3:
            producto_4_parametros()
        if int(opcion_elegida) == 4:
            cociente_2_parametros()
        if int(opcion_elegida) == 9:
            print('Adios! ')
            exit()
if __name__ == '__main__':
    main();
