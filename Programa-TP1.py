Crear un programa en Python que tendrá 3 o 4 funciones:
 Suma, 3 parámetros, devuelve la suma de los 3.
 Resta, 2 parámetros, devuelve la resta de los 2.
 Producto, 4 parámetros, devuelve el producto de los 4.
 Imprimir, 2 parámetros, texto y valor, devuelve la impresión de los valores pasados.
Usaremos Visual Studio Code, con la extensión de Python para hacer la práctica.
El equipo crea un Project en Githug y agrega 2 al menos 2 issue por cada tarea a realizar.
Crear una rama por cada miembro.
El primer integrante del grupo, creará el repositorio, creará un programa en Python con la
función suma, y el main y subirá al repo el código producido

@@ -1,7 +1,4 @@
# Mensaje de inicio

print("Hola, selecione la operacion que desea realizar\n 1 - Sumar\n 2 - Restar\n 3 - Multiplicar\n 4 - Dividir")
opción_elegida=input("Opcion elegida: ")
#--------------------------------Funciones--------------------------------------

# Funcion sumar 3 valores
@@ -33,16 +30,23 @@ def cociente_2_parametros():
    print("El cociente es:",(float(a)/float(b)))
#-----------------------Operaciones segun opcion elegida ----------------------------

if int(opción_elegida) == 1:
    suma_3_parametros()
if int(opción_elegida) == 2:
    resta_2_parametros()
if int(opción_elegida) == 3:
    producto_4_parametros()
if int(opción_elegida) == 4:
    cociente_2_parametros()
else:
    print("ingrese una opción correcta")

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
