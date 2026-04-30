#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 26/04/2026 8:20am
# Ultíma modificación: 
# Versión: 3.14

# importaciones de metodos
import re
import os
from datetime import datetime

# definicion de funciones 
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

# funciones opción 1 del menú 
def solicitarCargaTokens():
    """
    
    """
    print ("="*30)
    print ("Opción 1")
    print ("="*30)
    print("\n--- Configuración de Carga de Diccionario ---")
    pruta = input("\nPor favor, ingrese el nombre del archivo de tokens: ")
    while True:
        pseparador = input("Ingrese el símbolo que separa las palabras (solo 1 símbolo): ")
        if validardivision(pseparador):
            print("Separador aceptado")
            return pruta, pseparador
        else:
            print("El separador debe ser exactamente un símbolo (ni letras, ni números, ni espacios).")

def procesarArchivo1(pruta, pseparador):
    """

    """
    listaTokens = []
    vistos = set()
    archivo = open(pruta, "r", encoding="utf-8")
    numLinea = 1
    linea = archivo.readline()
    while linea != "":
        lineaLimpia = linea.strip()
        if lineaLimpia != "":
            if pseparador in lineaLimpia:
                partes = lineaLimpia.split(pseparador)
                if len(partes) == 2:
                    token1 = partes[0].strip()
                    token2 = partes[1].strip()
                    pareja = (token1, token2, 0)
                    if pareja not in vistos:
                        listaTokens.append(pareja)
                        vistos.add(pareja)
                else:
                    print(f"Línea {numLinea} inválida: {lineaLimpia}")
            else:
                print(f"Línea {numLinea} sin separador: {lineaLimpia}")
        linea = archivo.readline()
        numLinea += 1
    archivo.close()
    return listaTokens

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

# Funciones de la opción dos
def buscarToken(palabraBuscada, plistaDeTokens):
    """
    """
    posicionActual = 0
    for pareja in plistaDeTokens:
        if pareja[0] == palabraBuscada:
            return posicionActual
        posicionActual += 1
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

def solicitarNuevosTokensSeguros():
    """
    """
    while True:
        print ("="*30)
        print ("Opción 2")
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

def procesarActualizacionDeTokens(pcadenaNueva, pseparador, plistaTokens):
    """
    """
    bloques = pcadenaNueva.split()
    for bloque in bloques:
        partes = bloque.split(pseparador)
        llave = partes[0].strip()
        valor = partes[1].strip()
        indice = buscarToken(llave, plistaTokens)
        
        if indice != False:
            print(f"El token existente: {llave}, ahora es: {valor}")
            plistaTokens[indice] = (llave, valor, 0)
        else:
            print(f"Se a añadido nuevo token: ({llave}, {valor})")
            plistaTokens.append((llave, valor, 0))
    return plistaTokens

def administradorOpcion2(plistaTokens):
    """
    """
    resultadoSolicitud = solicitarNuevosTokensSeguros()
    if resultadoSolicitud is not None:
        nuevaCadena, separadorUsado = resultadoSolicitud
        plistaTokens = procesarActualizacionDeTokens(nuevaCadena, separadorUsado, plistaTokens)
        print("\nProceso finalizado con éxito.")
        input("pulse ENTER para continuar: ")
    return plistaTokens

# traduccion:
def validarTraduccionPalabra(pPalabra, pListaTokens):
    """
    """
    if pPalabra.isdigit():
        return pPalabra
    for i in range(len(pListaTokens)):
        if pListaTokens[i][0] == pPalabra:
            original = pListaTokens[i][0]
            traduccion = pListaTokens[i][1]
            conteoActual = pListaTokens[i][2]
            pListaTokens[i] = (original, traduccion, conteoActual + 1)
            return traduccion
    return pPalabra

def procesarContenidoLinea(pLinea, pListaTokens):
    """
    """
    partes = re.split(r'([^a-zA-Z0-9áéíóúÁÉÍÓÚ])', pLinea)
    lineaTraducida = ""
    conteoPalabrasLinea = 0
    for fragmento in partes:
        if fragmento: 
            if fragmento.isalnum():
                resultado = validarTraduccionPalabra(fragmento, pListaTokens)
                lineaTraducida += resultado
                conteoPalabrasLinea += 1
            else:
                lineaTraducida += fragmento
    return lineaTraducida, conteoPalabrasLinea

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
            archivoLectura = open(nombreOrigen, "r", encoding="utf-8")
            archivoEscritura = open(nombreDestino, "w", encoding="utf-8")

            for linea in archivoLectura:
                nuevaLinea, conteo = procesarContenidoLinea(linea, pListaTokens)
                archivoEscritura.write(nuevaLinea)
                totalPalabras += conteo
            archivoLectura.close()
            archivoEscritura.close()
            print(f"\nArchivo: {nombreDestino}, creado.")
            print(f"Palabras totales detectadas: {totalPalabras}")
            return totalPalabras
        except Exception as e:
            print(f"Error al procesar: {e}")
            return 0
    else:
        print("El archivo de origen no existe.")
        return 0

# reporte HTML
def calcularEstadisticas(pListaTokens, pTotalPalabras):
    totalReemplazos = 0
    for tupla in pListaTokens:
        totalReemplazos += tupla[2] 
    if pTotalPalabras > 0:
        porcentaje = (totalReemplazos / pTotalPalabras) * 100
    else:
        porcentaje = 0
    return totalReemplazos, porcentaje

def CuerpoHTML(pTituloPestanna, pFechaHora, pEstadisticas, pListaTokens):
    totalR, porcR = pEstadisticas
    html = "<html>\n<head>\n  <title>" + pTituloPestanna + "</title>\n</head>\n<body>\n"
    html += '  <h1 align="center">Reporte de Traducción</h1>\n'
    html += '  <h2 align="center">Fecha y hora de generación: ' + pFechaHora + '</h2>\n'
    html += '  <p align="center">\n'
    html += '    <b>Estadísticas del proceso:</b><br>\n'
    html += '    Cantidad total de reemplazos: ' + str(totalR) + '<br>\n'
    html += '    Porcentaje de palabras reemplazadas: ' + str(round(porcR, 2)) + '%\n'
    html += '  </p>\n'
    html += '  <table border="1" align="center" width="80%">\n'
    html += '    <tr bgcolor="#CCCCCC">\n      <th>Palabra Original</th>\n      <th>Reemplazo</th>\n      <th>Cantidad</th>\n    </tr>\n'
    contador = 0
    for tupla in pListaTokens:
        if tupla[2] > 0:
            colorFila = "#F2F2F2" if contador % 2 == 0 else "#FFFFFF"
            html += '    <tr bgcolor="' + colorFila + '">\n'
            html += '      <td align="center">' + str(tupla[0]) + '</td>\n'
            html += '      <td align="center">' + str(tupla[1]) + '</td>\n'
            html += '      <td align="center">' + str(tupla[2]) + '</td>\n'
            html += '    </tr>\n'
            contador += 1
    html += "  </table>\n</body>\n</html>"
    return html

def administradorOpcion7(pListaTokens, pTotalPalabras):
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
    contenidoFinal = CuerpoHTML(tituloUsuario, fechaH2, estadisticas, pListaTokens)
    try:
        archivoFinal = open(nombreArchivo, "w", encoding="utf-8")
        archivoFinal.write(contenidoFinal)
        archivoFinal.close()
        print("\nReporte generado con éxito: " + nombreArchivo)
    except Exception as e:
        print(" Ocurrió un error al crear el reporte: " + str(e) + " intente nuevamente")

listaGlobal = []
palabras = 0 

while True:
    print("\n Menu tester")
    print("1. cargar")
    print("2. Agregar/Actualizar")
    print("3. Ver Lista")
    print("4. Salir")
    print("5. traducir codigo")
    print("6. HTML")
    op = input("Seleccione: ")
    
    if op == "1":
        listaGlobal = administradorOpcion1()
    elif op == "2":
        listaGlobal = administradorOpcion2(listaGlobal)
    elif op == "3":
        print(f"\nLista actual: {listaGlobal}")
    elif op == "4":
        break
    elif op == "5":
        palabras = administradorOpcion5(listaGlobal)
    elif op == "6":
        palabras = administradorOpcion7(listaGlobal, palabras)