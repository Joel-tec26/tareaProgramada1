from datetime import datetime
import re

def mostrarTokens(ptokens):
    print("Token\tTraduccion")
    for i in ptokens:
        print(f"{i[0]}\t{i[1]}")
    return

def guardarTokensEnArchivoAux(ptokens):
    inservarEnbitacora("seleccion de la opcion 2")
    if ptokens==[]:
        inservarEnbitacora("Error al guardar tokens en archivo(opcion 4): no habian tokens")
        print("no hay tokens")
        input("precione ENTER para continuar")
        return
    archivo = input("ingrese el nombre del archivo que desee para guardar tokens")
    if archivo=="":
        inservarEnbitacora("Error al guardar tokens en archivo(opcion 4): el usuario no ingresó un nombre para el archivo")
        print("Debe escribir un nombre para el archivo")
        input("precione ENTER para continuar")
        return
    separador = input("escriba la forma en la que quiere que los tokens se separe ej(\"=\",\"-\")")
    if separador == "":
        inservarEnbitacora("Error al guardar tokens en archivo(opcion 4): el usuario no ingresó un nombre para el archivo")
        print("Debe escribir una forma de separación")
        input("precione ENTER para continuar")
        return
    guardarTokensEnArchivo(ptokens, archivo, separador)
    print("Tokens guardados con exito")
    inservarEnbitacora("ejecución de la opcion 4: guardar tokens en archivo exitosa")
    input("precione ENTER para continuar")
    return

def guardarTokensEnArchivo(ptokensm, parchivo, pseparador):
    archivo=open(f"{parchivo}.txt","a")
    for i in ptokensm:
        archivo.write(f"{i[0]}{pseparador}{i[1]}\n")
    archivo.close()
    return

def generarReporteCSV():
    return

def submenubitacora():
    while True:
        print("\t Submenú de Bitácora del Sistema")
        print("\nescoga una de las opciones:")
        print("[1]:\tAcciones por día escogído")
        print("[2]:\tAcciones con algunas palabras clave")
        print("[3]:\tSalir del submenú")
        opcion=input("\nSeleccione: ")
        if opcion=="1":
            filtrarPorDiaAux()
            inservarEnbitacora("selección de la opcion del submenú de bitacora del sistema 1: Acciones por día escogido")
        elif opcion=="2":
            filtrarPorPalabraClaveAux()
            inservarEnbitacora("selección de la opcion del submenú de bitacora del sistema 2: Acciones con algunas palabras clave")
        elif opcion=="3":
            inservarEnbitacora("selección de la opcion del submenú de bitacora del sistema 3: Salir del submenú")
            break
        else:
            print("Opcion invalida, vuelva a intentar")
            input("precione ENTER para continuar")
    return

def inservarEnbitacora(pdescripcion):
    fecha=datetime.now().strftime("%y-%m-%d_%H:%M:%S")
    bitacora=open("bitacora.txt","a")
    bitacora.write(f"({fecha},{pdescripcion})\n")
    bitacora.close()
    return


def filtrarPorDiaAux():
    print("ingrese la fecha que desea buscar. Formato:AAAA-MM-DD")
    fecha=input()
    if not re.match(fecha, "^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"):
        print("Formato de fecha incorrecto")
        inservarEnbitacora("Error al filtrar cada registro de la bitácora: el usuario ingresó una fecha con formato incorrecto")
        input("precione ENTER para continuar")
        return
    if not filtrarPorDia(fecha):
        print("no se encontró ningún registro con esa fecha")
    
def filtrarPorDia(pfecha):
    bitacora=open("bitacora.txt","r")
    encontrar=False
    for i in bitacora.read():
        fechaTiempo=i[0]
        if fechaTiempo[2:12]==pfecha:
            print(i)
            encontrar=True
    bitacora.close()
    return encontrar

def filtrarPorPalabraClaveAux():
    print("ingrese la palabra que desea buscar")
    palabra=input()
    if not filtrarPorPalabraClave(palabra):
        print("no se encontró nongún registro con esa palabra clave")
    return

def filtrarPorPalabraClave(ppalabra):
    encontrar=False
    bitacora=open("bitacora.txt","r")

    for i in bitacora.readlines():
        texto = i.split(",")[1]
        for palabra in texto.split():
            if re.sub(r'[^a-zA-Z0-9\s]', '', palabra) == ppalabra:
                print(i)
                encontrar=True
    bitacora.close()
    return encontrar

guardarTokensEnArchivoAux([("socrates","algo"),("wea","algoams")])