from datetime import datetime
import re

def adminMostrarTokens(ptokens):
    print ("="*30)
    print ("Opción 2")
    print ("="*30)
    if mostrarTokens(ptokens):
        inservarEnbitacora("Ejecución exitosa de la opcion 2: mostrar tokens")
        input("\nPrecione ENTER para continuar")
        return
    print("No hay tokens guardados")
    inservarEnbitacora("Error al mostrar tokens en archivo(opcion 4): no habian tokens")
    input("Precione ENTER para continuar")
    return
    

def mostrarTokens(ptokens):
    if ptokens==[]:
        return False
    print("Token\t\tTraduccion\n")
    for i in ptokens:
        print(f"{i[0]}"+" "*(20-len(i[1]))+f"{i[1]}")
    return True

def validarGuardarTokensEnArchivo(ptokens):
    print ("="*30)
    print ("Opción 4")
    print ("="*30)
    inservarEnbitacora("Seleccion de la opcion 2")
    if ptokens==[]:
        inservarEnbitacora("Error al guardar tokens en archivo(opcion 4): no habian tokens")
        print("No hay tokens")
        input("Precione ENTER para continuar")
        return
    archivo = input("Ingrese el nombre del archivo que desee para guardar tokens")
    if archivo=="":
        inservarEnbitacora("Error al guardar tokens en archivo(opcion 4): el usuario no ingresó un nombre para el archivo")
        print("Debe escribir un nombre para el archivo")
        input("Precione ENTER para continuar")
        return
    separador = input("Escriba la forma en la que quiere que los tokens se separe ej(\"=\",\"-\")")
    if separador == "":
        inservarEnbitacora("Error al guardar tokens en archivo(opcion 4): el usuario no ingresó un nombre para el archivo")
        print("Debe escribir una forma de separación")
        input("Precione ENTER para continuar")
        return
    if re.match("[a-zA-Zá-úÁ-Úä-üÄ-Ü0-9]",separador):
        inservarEnbitacora("Error al guardar tokens en archivo(opcion 4): el usuario ingresó en el separador una letra o numero")
        print("El separador debe ser únicamente un simbolo")
        input("Precione ENTER para continuar")
        return
    guardarTokensEnArchivo(ptokens,archivo, separador)
    print("Tokens guardados con éxito")
    inservarEnbitacora("ejecución exitosa de la opcion 4: guardar tokens en archivo")
    input("precione ENTER para continuar")
    return

def guardarTokensEnArchivo(ptokensm, parchivo, pseparador):
    archivo=open(f"{parchivo}.txt","a")
    for i in ptokensm:
        archivo.write(f"{i[0]}{pseparador}{i[1]}\n")
    archivo.close()
    return

def adminGenerarReporteCSV(pcambios):
    print ("="*30)
    print ("Opción 6")
    print ("="*30)
    print("Generando Reporte CSV")
    if pcambios==[]:
        print("Todavía no hay actualizaciones")
        inservarEnbitacora("Error al realizar el reporte csv: no hay actualizaciones aún")
        return
    generarReporteCSV(pcambios)
    inservarEnbitacora("Ejecucion exitosa de la opcion 6: generar reporte csv")
    return

def generarReporteCSV(pcambios):
    archivo = open("reporte.csv","w")
    for i in pcambios:
        archivo.write(f"Palabra original: {i[0]}\t|\tToken de cambio: {i[1]}\t|\tCantidad de reeplazos: {i[2]}\n")
    archivo.close()
    return

def submenubitacora():
    while True:
        print("\t Submenú de Bitácora del Sistema")
        print("\nEscoga una de las opciones:")
        print("[1]:\tAcciones por día escogído")
        print("[2]:\tAcciones con algunas palabras clave")
        print("[3]:\tSalir del submenú")
        opcion=input("\nSeleccione: ")
        if opcion=="1":
            inservarEnbitacora("selección de la opcion del submenú de bitacora del sistema 1: Acciones por día escogido")
            validarFiltrarPorDia()
        elif opcion=="2":
            inservarEnbitacora("selección de la opcion del submenú de bitacora del sistema 2: Acciones con algunas palabras clave")
            validarFiltrarPorPalabraClave()
        elif opcion=="3":
            inservarEnbitacora("selección de la opcion del submenú de bitacora del sistema 3: Salir del submenú")
            break
        else:
            print("Opcion invalida, vuelva a intentar")
            inservarEnbitacora("Error en selección de la opcion del submenú: el usuario ingresó una opcion invalida")
            input("Precione ENTER para continuar")
    return

def inservarEnbitacora(pdescripcion):
    fecha=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    bitacora=open("bitacora.txt","a")
    bitacora.write(f"({fecha},{pdescripcion})\n")
    bitacora.close()
    return


def validarFiltrarPorDia():
    print ("="*30)
    print ("Sub Opción 1")
    print ("="*30)
    print("Ingrese la fecha que desea buscar. Formato:AAAA-MM-DD")
    fecha=input()
    if fecha=="":
        print("Debe ingresar una fecha")
        inservarEnbitacora("Error al filtrar cada registro de la bitácora: no ingresó un nada")
        input("Presione ENTER para continuar")
        return
    if not re.match("^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$",fecha):
        print("Formato de fecha incorrecto")
        inservarEnbitacora("Error al filtrar cada registro de la bitácora: el usuario ingresó una fecha con formato incorrecto")
        input("Precione ENTER para continuar")
        return
    if not filtrarPorDia(fecha):
        print("No se encontró ningún registro con esa fecha")
        input("Presione ENTER para continuar")
        inservarEnbitacora("Error al filtrar cada registro de la bitácora: no se encontró ningún registro con esa fecha")
    
def filtrarPorDia(pfecha):
    bitacora=open("bitacora.txt","r")
    encontrar=False
    for i in bitacora.readlines():
        fechaTiempo=i[1:11]
        print(fechaTiempo)
        if fechaTiempo==pfecha:
            print(i)
            encontrar=True
    bitacora.close()
    return encontrar

def validarFiltrarPorPalabraClave():
    print ("="*30)
    print ("Sub Opción 2")
    print ("="*30)
    print("ingrese la palabra que desea buscar")
    palabra=input()
    if palabra=="":
        print("Debe ingresar una palabra")
        inservarEnbitacora("Error al filtrar cada registro de la bitácora: no ingresó un nada")
    if not filtrarPorPalabraClave(palabra):
        print("No se encontró nongún registro con esa palabra clave")
        input("Presione ENTER para continuar")
        inservarEnbitacora("Error al filtrar cada registro de la bitácora: no se encontró la palabra que puso el usuario")
        return
    inservarEnbitacora("Ejecución exitosa de la subopción 2: Acciones con algunas palabras clave")
    return

def filtrarPorPalabraClave(ppalabra):
    encontrar=False
    bitacora=open("bitacora.txt","r")
    for i in bitacora.readlines():
        texto = i.split(",")[1]
        for palabra in texto.split():
            if re.sub(r'[^a-zA-Zá-úä-üÁ-ÚÄ-Ü0-9\s]', '', palabra) == ppalabra:
                print(i)
                encontrar=True
    bitacora.close()
    return encontrar

# PRUEBAS. IGNORAR

# def testeoOpcion6(werewe, eustakio):
#     wea = input("pepe")
#     wea2 = input("fuhrer")
#     archivo = open("socrates.txt","r")
#     lineass=archivo.readlines()
#     archivo.close()
#     archivo = open("socrates.txt","w")
#     for i in lineass:
#         mielda=i.split("-")
#         print(wea2)
#         primer=mielda[0]
#         oliginal = mielda[1]
#         if primer==wea:
#             archivo.write(f"{wea}-{wea2}\n")
#             d=False
#             l=0
#             for o in eustakio:
#                 print(o[0])
#                 if o[0]==wea:
#                     dd=o[2]
#                     ayo = (wea,wea2,dd+1)
#                     d=True
#                     eustakio[l]=ayo
#                 l+=1
#             if not d:
#                 eustakio.append((wea,wea2,1))
#         else:
#             archivo.write(i)
#     archivo.close()
#     for i in range(len(werewe)):
#         coso=werewe[i]
#         if coso[0] == wea:
#              werewe[i]=(wea,wea2)
#     return werewe, eustakio

# pruebaTokens=[("pepe","fuhrer"),("fibonacci","xi jinping")]
# cambios = []

# pruebaTokens, cambios = testeoOpcion6(pruebaTokens, cambios)
# pruebaTokens, cambios = testeoOpcion6(pruebaTokens, cambios)


# print(pruebaTokens, cambios)
submenubitacora()
# adminGenerarReporteCSV(cambios)