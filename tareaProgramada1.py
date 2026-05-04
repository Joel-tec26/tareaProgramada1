#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 21/04/2026 8:20am
# Ultíma modificación: 30/04/2026 
# Versión: 3.14

from funciones1 import *

listaTokens = []
cantidadPalabras = 0 
tiempoTraduccion = 0

while True:
    print("\t\tTraductor de Codigo")
    print("-"*60)
    print("1. Cargar tokens")
    print("2. Mostrar tokens")
    print("3. Agregar/Modificar tokens")
    print("4. Guardar tokens")
    print("5. Traducir codigo")
    print("6. Generar CSV")
    print("7. Generar HTML")
    print("8. Submenú bitacora del sistema")
    print("9. Salir")
    opcion = input("Seleccione la opcion deseada: ")

    if opcion=="1":
        listaTokens = administradorOpcion1()
    elif opcion=="2":
        adminMostrarTokens(listaTokens)
    elif opcion=="3":
        listaTokens = administradorOpcion3(listaTokens)
    elif opcion=="4":
        validarGuardarTokensEnArchivo(listaTokens)
    elif opcion=="5":
        cantidadPalabras, tiempoTraduccion = administradorOpcion5(listaTokens)
    elif opcion=="6":
        adminGenerarReporteCSV(listaTokens)
    elif opcion=="7":
        cantidadPalabras = administradorOpcion7(listaTokens, cantidadPalabras, tiempoTraduccion)
    elif opcion=="8":
        submenubitacora()
    elif opcion=="9":
        break
    else:
        print("opción inválida")