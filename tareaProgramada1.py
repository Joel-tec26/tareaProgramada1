#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 21/04/2026 8:20am
# Ultíma modificación: 3/05/2026 
# Versión: 3.14

#Importación de librerias 
from funciones1 import *
import os
from datetime import datetime

# Variables globales
listaTokens = []
cantidadPalabras = 0 
tiempoTraduccion = 0

#Definición de funciones 

# DE validar
def validardivision (pcaracter):
    """

    """
    patron = r'^[^\d\s\w]$'
    return bool(re.match(patron, pcaracter))

def validarExistencia(pruta):
    """
    
    """
    if os.path.exists(pruta):
        return True
    else:
        print(f"No se encontró el archivo {pruta} en los archivos.")
        return False

def validarFormato(pbloque, pseparador):
    """
    """
    if pseparador not in pbloque:
        return False, f"Al bloque: {pbloque} le falta el separador: {pseparador}."
    partes = pbloque.split(pseparador)
    if len(partes) != 2 or partes[0].strip() == "" or partes[1].strip() == "":
        return False, f"El bloque: {pbloque} tiene un formato incompleto o incorrecto."
    return True, ""

def validarListaTokens(pTokens):
    """
    """
    return pTokens != []

def validarNombreArchivo(pArchivo):
    """
    """
    return pArchivo != ""

def validarSeparadorAux(pSeparador):
    """
    """
    if pSeparador == "":
        return False
    if re.match("[a-zA-Zá-úÁ-Úä-üÄ-Ü0-9]", pSeparador):
        return False
    return True 



# Función 1: cargar tokens
def solicitarCargaTokens():
    """
    
    """
    print ("="*30)
    print ("Opción 1")
    print ("="*30)
    print("\n--- Configuración de Carga de tokens ---")
    pruta = input("\nPor favor, ingrese el nombre del archivo de tokens: ")
    while True:
        pseparador = input("Ingrese el símbolo que separa las palabras (solo 1 símbolo): ")
        if validardivision(pseparador):
            print("Separador aceptado")
            return pruta, pseparador
        else:
            print("El separador debe ser exactamente un símbolo (ni letras, ni números, ni espacios).")

def administradorOpcion1():
    """
    """
    while True:
        ruta, separador = solicitarCargaTokens()
        if validarExistencia(ruta):
            try:
                tokens = procesarArchivo1(ruta, separador)
                print(f"\tCarga completada: {len(tokens)} tokens encontrados")
                input("pulse ENTER para continuar: ")
                return tokens
            except Exception :
                print(" Caracteristica inesperada encontrada al leer el archivo")
        opcion = input("\n¿Desea intentar de nuevo con otra ruta? \nDigite (1) para continuar \nDigite (2) para salir: ")
        if opcion != "1":
            print("Operación cancelada.")
            input("pulse ENTER para continuar: ")
            return []

# Función 2: Mostrar tokens
def adminMostrarTokens(ptokens):
    """
    """
    print ("="*30)
    print ("Opción 2")
    print ("="*30)
    if mostrarTokens(ptokens):
        inservarEnBitacora("Ejecución exitosa de la opcion 2: mostrar tokens")
        input("\nPrecione ENTER para continuar: ")
        return
    print("No hay tokens guardados")
    inservarEnBitacora("Error al mostrar tokens en archivo(opcion 4): no habian tokens")
    input("Precione ENTER para continuar: ")
    return
    
# Función 3: Agregar y modificar tokens

def solicitarNuevosTokensSeguros():
    """
    """
    while True:
        print ("="*30)
        print ("Opción 3")
        print ("="*30)
        print("\n--- Registro de Tokens Personalizado ---")
        separadorElegido = input("Digite el separador que vaya a usar: ").strip()
        while not validardivision(separadorElegido):
            print("Formato incorrecto. \nEl separador debe ser exactamente un símbolo (ni letras, ni números, ni espacios. ")
            separadorElegido = input("Digite el separador que vaya a usar: ").strip()
        print(f"\nIngrese los tokens usando el separador ecogido: {separadorElegido}  \n(ejemplo: if{separadorElegido}si)")
        nuevaCadena = input(" Ingrese la cadena de tokens que desea añadir: ").strip()
        bloques = nuevaCadena.split()
        todoCorrecto = True
        for linea in bloques:
            esValido, mensaje = validarFormato(linea, separadorElegido)
            if not esValido:
                print(mensaje)
                todoCorrecto = False
                break
        if todoCorrecto:
            return nuevaCadena, separadorElegido

def administradorOpcion3(plistaTokens):
    """
    """
    resultadoSolicitud = solicitarNuevosTokensSeguros()
    if resultadoSolicitud is not None:
        nuevaCadena, separadorUsado = resultadoSolicitud
        plistaTokens = procesarActualizacionDeTokens(nuevaCadena, separadorUsado, plistaTokens)
        print("\nProceso finalizado con éxito.")
        input("pulse ENTER para continuar: ")
    return plistaTokens

# Función 4: Guardar tokens en archivo

def administradorOpcion4(pTokens):
    """
    """
    print("=" * 30)
    print("Opción 4")
    print("=" * 30)
    inservarEnBitacora("\n--- Guardado de Tokens ---")
    if not validarListaTokens(pTokens):
        inservarEnBitacora("Error al guardar tokens en archivo(opcion 4): no habian tokens")
        print("No hay tokens")
        input("Presione ENTER para continuar ")
        return
    archivo = input("Ingrese el nombre del archivo que desee para guardar tokens: ")
    if not validarNombreArchivo(archivo):
        inservarEnBitacora("Error al guardar tokens en archivo(opcion 4): el usuario no ingresó un nombre")
        print("Debe escribir un nombre para el archivo")
        input("Presione ENTER para continuar ")
        return
    separador = input("Escriba la forma en la que quiere que los tokens se separe ej(\"=\",\"-\"): ")
    if not validarSeparadorAux(separador):
        inservarEnBitacora("Error al guardar tokens en archivo(opcion 4): separador vacío o inválido")
        print("El separador debe ser únicamente un símbolo y no puede estar vacío")
        input("Presione ENTER para continuar ")
        return
    procesarGuardadoTokens(pTokens, archivo, separador)
    print("Tokens guardados con éxito")
    inservarEnBitacora("ejecución exitosa de la opcion 4: guardar tokens en archivo")
    input("Presione ENTER para continuar ")

# Función 5: Traducir codigo

def administradorOpcion5(pListaTokens):
    """
    """
    print ("="*30)
    print ("Opción 5")
    print ("="*30)
    print("\n---Traducción de codigo ---")
    nombreOrigen = input("Digite el nombre del archivo a traducir: ")
    for i in range(len(pListaTokens)):
        pListaTokens[i] = (pListaTokens[i][0], pListaTokens[i][1], 0)
    totalPalabras=0
    if os.path.exists(nombreOrigen):
        nombreDestino = input("Digite el nombre del nuevo archivo: ")
        try:
            inicio = datetime.now()
            archivoLectura = open(nombreOrigen, "r", encoding="utf-8")
            archivoEscritura = open(nombreDestino, "w", encoding="utf-8")

            for linea in archivoLectura:
                nuevaLinea, conteo = procesarContenidoLinea(linea, pListaTokens)
                archivoEscritura.write(nuevaLinea)
                totalPalabras += conteo
            archivoLectura.close()
            archivoEscritura.close()
            fin = datetime.now()
            duracion = fin - inicio
            segundosTotales = duracion.total_seconds()
            print(f"\nArchivo: {nombreDestino}, creado.")
            print(f"Palabras totales detectadas: {totalPalabras}")
            return totalPalabras, segundosTotales
        except Exception as e:
            print(f"Error al procesar: {e}")
            return 0, 0 
    else:
        print("El archivo de origen no existe.")
        return 0, 0

# Función 6: Generar CSV
def adminGenerarReporteCSV(ptokens):
    print ("="*30)
    print ("Opción 6")
    print ("="*30)
    print("Generando Reporte CSV")
    if ptokens==[]:
        print("Todavía no hay tokens")
        inservarEnBitacora("Error al realizar el reporte csv: no hay actualizaciones aún")
        input("precione ENTER para continuar ")
        return
    generarReporteCSV(ptokens)
    inservarEnBitacora("Ejecucion exitosa de la opcion 6: generar reporte csv")
    print("el reporte CSV se generó exitosamente")
    input("precione ENTER para continuar ")
    return

# Función 7: Generar HTML
def administradorOpcion7(pListaTokens, pTotalPalabras, ptiempoTraduccion):
    """
    """
    print ("="*30)
    print ("Opción 7")
    print ("="*30)
    print("\n--- Generar Reporte HTML ---")
    tituloUsuario = input("\nIngrese el título del reporte: ")
    ahora = datetime.now()
    fechaH2 = ahora.strftime("%d/%m/%y-%H:%M:%S")
    fechaArch = ahora.strftime("%d-%m-%y_%H-%M-%S")    
    nombreArchivo = "reporteHTML_" + fechaArch + ".html"
    estadisticas = calcularEstadisticas(pListaTokens, pTotalPalabras)
    contenidoFinal = CuerpoHTML(tituloUsuario, fechaH2, estadisticas, pListaTokens, ptiempoTraduccion)
    try:
        archivoFinal = open(nombreArchivo, "w", encoding="utf-8")
        archivoFinal.write(contenidoFinal)
        archivoFinal.close()
        print("\nReporte generado con éxito: " + nombreArchivo)
    except Exception as e:
        print(" Ocurrió un error al crear el reporte: " + str(e) + " intente nuevamente")

# Función 8: Submenú bitacora del sistema
def submenubitacora():
    """
    """
    while True:
        print("\t Submenú de Bitácora del Sistema")
        print("\nEscoga una de las opciones:")
        print("[1]:\tAcciones por día escogído")
        print("[2]:\tAcciones por palabra clave")
        print("[3]:\tSalir del submenú")
        opcion=input("\nSeleccione: ")
        if opcion=="1":
            inservarEnBitacora("selección de la opcion del submenú de bitacora del sistema 1: Acciones por día escogido")
            validarFiltrarPorDia()
        elif opcion=="2":
            inservarEnBitacora("selección de la opcion del submenú de bitacora del sistema 2: Acciones con algunas palabras clave")
            validarFiltrarPorPalabraClave()
        elif opcion=="3":
            inservarEnBitacora("selección de la opcion del submenú de bitacora del sistema 3: Salir del submenú")
            break
        else:
            print("Opcion invalida, vuelva a intentar")
            inservarEnBitacora("Error en selección de la opcion del submenú: el usuario ingresó una opcion invalida")
            input("Precione ENTER para continuar")
    return

def validarFiltrarPorDia():
    print ("="*30)
    print ("Sub Opción 1")
    print ("="*30)
    print("Ingrese la fecha que desea buscar. Formato:AAAA-MM-DD")
    fecha=input()
    if fecha=="":
        print("Debe ingresar una fecha")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no ingresó un nada")
        input("Presione ENTER para continuar ")
        return
    if not re.match(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$",fecha):
        print("Formato de fecha incorrecto")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: el usuario ingresó una fecha con formato incorrecto")
        input("Precione ENTER para continuar ")
        return
    if not filtrarPorDia(fecha):
        print("No se encontró ningún registro con esa fecha")
        input("Presione ENTER para continuar ")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no se encontró ningún registro con esa fecha")
    inservarEnBitacora("Ejecución exitosa de la subopción 1: filtrar por día")
    input("Presione ENTER para continuar ")

def validarFiltrarPorPalabraClave():
    print ("="*30)
    print ("Sub Opción 2")
    print ("="*30)
    print("ingrese la palabra que desea buscar")
    palabra=input()
    if palabra=="":
        print("Debe ingresar una palabra")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no ingresó un nada")
    if not filtrarPorPalabraClave(palabra):
        print("No se encontró ningún registro con esa palabra clave")
        input("Presione ENTER para continuar ")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no se encontró la palabra que puso el usuario")
        return
    inservarEnBitacora("Ejecución exitosa de la subopción 2: filtrar por palabra clave")
    input("Presione ENTER para continuar ")
    return

#Programa Principal
while True:
    print("\n\t\tTraductor de Codigo")
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
        administradorOpcion4(listaTokens)
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