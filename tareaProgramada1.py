#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 21/04/2026 8:20am
# Ultíma modificación: 6/05/2026 6:18
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
    Funcionalidad:
    Valida si un carácter corresponde a un símbolo especial y no a letras,
    números o espacios.
    Entradas:
    -pcaracter(str): carácter que se desea validar
    Salidas:
    -resultado(bool): True si el carácter es un símbolo especial, False en caso contrario
    """
    patron = r'^[^\d\s\w]$'
    return bool(re.match(patron, pcaracter))

def validarExistencia(pruta):
    """
    Funcionalidad:
    Verifica si un archivo existe en la ruta especificada.
    Entradas:
    -pruta(str): ruta o nombre del archivo que se desea verificar
    Salidas:
    -resultado(bool): True si el archivo existe, False en caso contrario
    -mensaje(str): mensaje de error mostrado en pantalla si el archivo no existe
    """
    if os.path.exists(pruta):
        return True
    else:
        print(f"No se encontró el archivo {pruta} en los archivos.")
        return False

def validarFormato(pbloque, pseparador):
    """
    Funcionalidad:
    Verifica que un bloque de texto contenga un separador válido
    y que las partes resultantes no estén vacías.
    Entradas:
    -pbloque(str): bloque de texto que se desea validar
    -pseparador(str): carácter separador esperado en el bloque
    Salidas:
    -resultado(bool): True si el formato es válido, False en caso contrario
    -mensaje(str): mensaje de error o cadena vacía según el resultado de la validación
    """
    if pseparador not in pbloque:
        return False, f"Al bloque: {pbloque} le falta el separador: {pseparador}."
    partes = pbloque.split(pseparador)
    if len(partes) != 2 or partes[0].strip() == "" or partes[1].strip() == "":
        return False, f"El bloque: {pbloque} tiene un formato incompleto o incorrecto."
    return True, ""

def validarListaTokens(pTokens):
    """
    Funcionalidad:
    Verifica si una lista de tokens contiene elementos.
    Entradas:
    -pTokens(list): lista de tokens a evaluar
    Salidas:
    -resultado(bool): True si la lista contiene elementos, False si está vacía
    """
    return pTokens != []

def validarNombreArchivo(pArchivo):
    """
    Funcionalidad:
    Verifica que el nombre de un archivo no esté vacío.
    Entradas:
    -pArchivo(str): nombre del archivo a validar
    Salidas:
    -resultado(bool): True si el nombre contiene información, False si está vacío
    """
    return pArchivo != ""

def validarSeparadorAux(pSeparador):
    """
    Funcionalidad:
    Verifica que un separador no esté vacío y que no sea una letra o número.
    Entradas:
    -pSeparador(str): carácter separador que se desea validar
    Salidas:
    -resultado(bool): True si el separador es válido, False en caso contrario
    """
    if pSeparador == "":
        return False
    if re.match(r"[a-zA-Zá-úÁ-Úä-üÄ-Ü0-9]", pSeparador):
        return False
    return True 



# Función 1: cargar tokens
def solicitarCargaTokens():
    """
    Funcionalidad:
    Solicita al usuario la ruta de un archivo y el símbolo separador
    que será utilizado para cargar tokens.
    Entradas:
    -pruta(str): nombre o ruta del archivo ingresado por el usuario
    -pseparador(str): símbolo separador ingresado por el usuario
    Salidas:
    -pruta(str): nombre o ruta válida del archivo
    -pseparador(str): símbolo separador válido
    -mensaje(str): mensajes mostrados en pantalla sobre validación del separador
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
    Funcionalidad:
    Administra el proceso de carga de tokens desde un archivo,
    validando la existencia del archivo y procesando su contenido.
    Entradas:
    -ruta(str): ruta del archivo ingresada por el usuario
    -separador(str): símbolo separador ingresado por el usuario
    -opcion(str): opción ingresada por el usuario para reintentar o cancelar
    Salidas:
    -tokens(list): lista de tokens cargados desde el archivo
    -mensaje(str): mensajes mostrados en pantalla sobre el estado de la carga
    """
    while True:
        ruta, separador = solicitarCargaTokens()
        if validarExistencia(ruta):
            try:
                tokens = procesarArchivo1(ruta, separador)
                print(f"\tCarga completada: {len(tokens)} tokens encontrados")
                input("Presione ENTER para continuar: ")
                return tokens
            except Exception :
                print(" Caracteristica inesperada encontrada al leer el archivo")
        opcion = input("\n¿Desea intentar de nuevo con otra ruta? \nDigite (1) para continuar \nDigite (2) para salir: ")
        if opcion != "1":
            print("Operación cancelada.")
            input("Presione ENTER para continuar: ")
            return []

# Función 2: Mostrar tokens
def administradoropcion2(ptokens):
    """
    Funcionalidad:
    Muestra los tokens almacenados y registra el resultado en la bitácora.
    Entradas:
    -ptokens(list): lista de tokens almacenados
    Salidas:
    -mensaje(str): mensajes mostrados en pantalla indicando si existen tokens o no
    """
    print ("="*30)
    print ("Opción 2")
    print ("="*30)
    if mostrarTokens(ptokens):
        inservarEnBitacora("Ejecución exitosa de la opcion 2: mostrar tokens")
        input("\nPresione ENTER para continuar: ")
        return
    print("No hay tokens guardados")
    inservarEnBitacora("Error al mostrar tokens en archivo(opcion 4): no habian tokens")
    input("Presione ENTER para continuar: ")
    return
    
# Función 3: Agregar y modificar tokens

def solicitarNuevosTokensSeguros():
    """
    Funcionalidad:
    Solicita al usuario nuevos tokens y valida que el formato
    y el separador utilizado sean correctos.
    Entradas:
    -separadorElegido(str): símbolo separador ingresado por el usuario
    -nuevaCadena(str): cadena de tokens ingresada por el usuario
    Salidas:
    -nuevaCadena(str): cadena válida de tokens
    -separadorElegido(str): símbolo separador válido
    -mensaje(str): mensajes mostrados en pantalla sobre errores o validaciones
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
    Funcionalidad:
    Administra el proceso de agregar y actualizar tokens en la lista principal.
    Entradas:
    -plistaTokens(list): lista actual de tokens almacenados
    -nuevaCadena(str): nueva cadena de tokens ingresada por el usuario
    -separadorUsado(str): símbolo separador utilizado por el usuario
    Salidas:
    -plistaTokens(list): lista de tokens actualizada
    -mensaje(str): mensajes mostrados en pantalla indicando el resultado del proceso
    """
    resultadoSolicitud = solicitarNuevosTokensSeguros()
    if resultadoSolicitud is not None:
        nuevaCadena, separadorUsado = resultadoSolicitud
        plistaTokens = procesarActualizacionDeTokens(nuevaCadena, separadorUsado, plistaTokens)
        print("\nProceso finalizado con éxito.")
        input("Presione ENTER para continuar: ")
    return plistaTokens

# Función 4: Guardar tokens en archivo

def administradorOpcion4(pTokens):
    """
    Funcionalidad:
    Administra el proceso de guardar tokens en un archivo,
    validando la existencia de tokens, el nombre del archivo
    y el separador elegido por el usuario.
    Entradas:
    -pTokens(list): lista de tokens que se desea guardar
    -archivo(str): nombre del archivo ingresado por el usuario
    -separador(str): símbolo separador ingresado por el usuario
    Salidas:
    -mensaje(str): mensajes mostrados en pantalla indicando errores o éxito del guardado
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
    Funcionalidad:
    Administra el proceso de traducción de un archivo utilizando
    la lista de tokens almacenados.
    Entradas:
    -pListaTokens(list): lista de tokens utilizados para la traducción
    -nombreOrigen(str): nombre del archivo origen ingresado por el usuario
    -nombreDestino(str): nombre del archivo destino ingresado por el usuario
    Salidas:
    -totalPalabras(int): cantidad total de palabras detectadas y procesadas
    -segundosTotales(float): tiempo total de traducción en segundos
    -mensaje(str): mensajes mostrados en pantalla sobre el resultado del proceso
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
def administradoropcion6(ptokens):
    """
    Funcionalidad:
    Genera un reporte CSV utilizando la lista de tokens almacenados.
    Entradas:
    -ptokens(list): lista de tokens que serán incluidos en el reporte
    Salidas:
    -mensaje(str): mensajes mostrados en pantalla indicando errores o éxito en la generación del reporte
    """
    print ("="*30)
    print ("Opción 6")
    print ("="*30)
    print("Generando Reporte CSV")
    if ptokens==[]:
        print("Todavía no hay tokens")
        inservarEnBitacora("Error al realizar el reporte csv: no hay actualizaciones aún")
        input("Presione ENTER para continuar ")
        return
    generarReporteCSV(ptokens)
    inservarEnBitacora("Ejecucion exitosa de la opcion 6: generar reporte csv")
    print("el reporte CSV se generó exitosamente")
    input("Presione ENTER para continuar ")
    return

# Función 7: Generar HTML
def administradorOpcion7(pListaTokens, pTotalPalabras, ptiempoTraduccion):
    """
    Funcionalidad:
    Genera un reporte HTML con estadísticas de traducción y datos
    de los tokens procesados.
    Entradas:
    -pListaTokens(list): lista de tokens utilizados en la traducción
    -pTotalPalabras(int): cantidad total de palabras procesadas
    -ptiempoTraduccion(float): tiempo total de traducción
    -tituloUsuario(str): título del reporte ingresado por el usuario
    Salidas:
    -mensaje(str): mensajes mostrados en pantalla indicando éxito o 
    error en la creación del reporte HTML 
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
    Funcionalidad:
    Muestra y administra el submenú de bitácora del sistema,
    permitiendo filtrar registros por fecha o palabra clave.
    Entradas:
    -opcion(str): opción seleccionada por el usuario en el submenú
    Salidas:
    -mensaje(str): mensajes mostrados en pantalla sobre navegación, errores o resultados del submenú
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
            filtrarPorDia()
        elif opcion=="2":
            inservarEnBitacora("selección de la opcion del submenú de bitacora del sistema 2: Acciones con algunas palabras clave")
            filtrarPorPalabraClaveaux()
        elif opcion=="3":
            inservarEnBitacora("selección de la opcion del submenú de bitacora del sistema 3: Salir del submenú")
            break
        else:
            print("Opcion invalida, vuelva a intentar")
            inservarEnBitacora("Error en selección de la opcion del submenú: el usuario ingresó una opcion invalida")
            input("Presione ENTER para continuar")
    return

def filtrarPorDia():
    """
    Funcionalidad:
    Solicita una fecha al usuario y filtra los registros
    de la bitácora correspondientes a ese día.
    Entradas:
    -fecha(str): fecha ingresada por el usuario en formato AAAA-MM-DD
    Salidas:
    -mensaje(str): mensajes mostrados en pantalla indicando errores, ausencia de registros o éxito del filtrado
    """
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

def filtrarPorPalabraClaveaux():
    """
    Funcionalidad:
    Solicita una palabra clave al usuario y filtra los registros
    de la bitácora que contengan dicha palabra.
    Entradas:
    -palabra(str): palabra clave ingresada por el usuario
    Salidas:
    -mensaje(str): mensajes mostrados en pantalla indicando errores, ausencia de coincidencias o éxito del filtrado
    """
    print ("="*30)
    print ("Sub Opción 2")
    print ("="*30)
    print("ingrese la palabra que desea buscar")
    palabra=input()
    if palabra=="":
        print("Debe ingresar una palabra")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no ingresó un nada")
    if not filtrarPorPalabraClave1(palabra):
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
        administradoropcion2(listaTokens)
    elif opcion=="3":
        listaTokens = administradorOpcion3(listaTokens)
    elif opcion=="4":
        administradorOpcion4(listaTokens)
    elif opcion=="5":
        cantidadPalabras, tiempoTraduccion = administradorOpcion5(listaTokens)
    elif opcion=="6":
        administradoropcion6(listaTokens)
    elif opcion=="7":
        cantidadPalabras = administradorOpcion7(listaTokens, cantidadPalabras, tiempoTraduccion)
    elif opcion=="8":
        submenubitacora()
    elif opcion=="9":
        break
    else:
        print("\nopción inválida")
        input("Presione ENTER para continuar ")
