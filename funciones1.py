#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 21/04/2026 8:20am
# Ultíma modificación: 30/04/2026 
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
    print("\n--- Configuración de Carga de tokens ---")
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
        
# mostrar tokens

def adminMostrarTokens(ptokens):
    print ("="*30)
    print ("Opción 2")
    print ("="*30)
    if mostrarTokens(ptokens):
        inservarEnBitacora("Ejecución exitosa de la opcion 2: mostrar tokens")
        input("\nPrecione ENTER para continuar")
        return
    print("No hay tokens guardados")
    inservarEnBitacora("Error al mostrar tokens en archivo(opcion 4): no habian tokens")
    input("Precione ENTER para continuar")
    return
    
def mostrarTokens(ptokens):
    if ptokens==[]:
        return False
    print("Token\t\tTraduccion\n")
    for i in ptokens:
        print(f"{i[0]}"+" "*(20-len(i[1]))+f"{i[1]}")
    return True

# agregar o actualizar tokens

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

# guardar tokens en archivo

def validarGuardarTokensEnArchivo(ptokens):
    print ("="*30)
    print ("Opción 4")
    print ("="*30)
    inservarEnBitacora("Seleccion de la opcion 4")
    while True:
        if ptokens==[]:
            inservarEnBitacora("Error al guardar tokens en archivo(opcion 4): no habian tokens")
            print("No hay tokens")
            input("Precione ENTER para continuar")
            return
        archivo = input("Ingrese el nombre del archivo que desee para guardar tokens: ")
        if archivo=="":
            inservarEnBitacora("Error al guardar tokens en archivo(opcion 4): el usuario no ingresó un nombre para el archivo")
            print("Debe escribir un nombre para el archivo")
            input("Precione ENTER para continuar")
            return
        separador = input("Escriba la forma en la que quiere que los tokens se separe ej(\"=\",\"-\"): ")
        if separador == "":
            inservarEnBitacora("Error al guardar tokens en archivo(opcion 4): el usuario no ingresó un nombre para el archivo")
            print("Debe escribir una forma de separación")
            input("Precione ENTER para continuar")
            return
        if re.match("[a-zA-Zá-úÁ-Úä-üÄ-Ü0-9]",separador):
            inservarEnBitacora("Error al guardar tokens en archivo(opcion 4): el usuario ingresó en el separador una letra o numero")
            print("El separador debe ser únicamente un simbolo")
            input("Precione ENTER para continuar")
            return
        break
    guardarTokensEnArchivo(ptokens,archivo, separador)
    print("Tokens guardados con éxito")
    inservarEnBitacora("ejecución exitosa de la opcion 4: guardar tokens en archivo")
    input("precione ENTER para continuar")
    return

def guardarTokensEnArchivo(ptokensm, parchivo, pseparador):
    archivo=open(f"{parchivo}.txt","a", encoding="utf-8")
    for i in ptokensm:
        archivo.write(f"{i[0]}{pseparador}{i[1]}\n")
    archivo.close()
    return

#traducir codigo

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
    
#generar reporte CSV

def adminGenerarReporteCSV(ptokens):
    print ("="*30)
    print ("Opción 6")
    print ("="*30)
    print("Generando Reporte CSV")
    if ptokens==[]:
        print("Todavía no hay tokens")
        inservarEnBitacora("Error al realizar el reporte csv: no hay actualizaciones aún")
        input("precione ENTER para continuar")
        return
    generarReporteCSV(ptokens)
    inservarEnBitacora("Ejecucion exitosa de la opcion 6: generar reporte csv")
    print("el reporte CSV se generó exitosamente")
    input("precione ENTER para continuar")
    return

def generarReporteCSV(pcambios):
    archivo = open("reporte.csv","a", encoding="utf-8")
    for i in pcambios:
        if i[2]>0:
            archivo.write(f"Palabra original: {i[0]}\t|\tToken de cambio: {i[1]}\t|\tCantidad de reeplazos: {i[2]}\n")
    archivo.close()
    return True

#generar reporte HTML

def calcularEstadisticas(pListaTokens, pTotalPalabras):
    totalReemplazos = 0
    for tupla in pListaTokens:
        totalReemplazos += tupla[2] 
    if pTotalPalabras > 0:
        porcentaje = (totalReemplazos / pTotalPalabras) * 100
    else:
        porcentaje = 0
    return totalReemplazos, porcentaje

def CuerpoHTML(pTituloPestanna, pFechaHora, pEstadisticas, pListaTokens, ptiempoTraduccion):
    totalR, porcR = pEstadisticas
    html = "<html>\n<head>\n  <title>" + pTituloPestanna + "</title>\n</head>\n<body>\n"
    html += '  <h1 align="center">Reporte de Traducción</h1>\n'
    html += '  <h2 align="center">Fecha y hora de generación: ' + pFechaHora + '</h2>\n'
    html += '  <p align="center">\n'
    html += '    <b>Estadísticas del proceso:</b><br>\n'
    html += '    Cantidad total de reemplazos: ' + str(totalR) + '<br>\n'
    html += '    Porcentaje de palabras reemplazadas: ' + str(round(porcR, 2)) + '%<br>\n'
    html += '    Duración de la traducción: ' + str(round(ptiempoTraduccion, 4)) + ' segundos\n' 
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

def administradorOpcion7(pListaTokens, pTotalPalabras, ptiempoTraduccion):
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

# submenú bitacora

def submenubitacora():
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

def inservarEnBitacora(pdescripcion):
    fecha=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    bitacora=open("bitacora.txt","a", encoding="utf-8")
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
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no ingresó un nada")
        input("Presione ENTER para continuar")
        return
    if not re.match("^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$",fecha):
        print("Formato de fecha incorrecto")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: el usuario ingresó una fecha con formato incorrecto")
        input("Precione ENTER para continuar")
        return
    if not filtrarPorDia(fecha):
        print("No se encontró ningún registro con esa fecha")
        input("Presione ENTER para continuar")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no se encontró ningún registro con esa fecha")
    inservarEnBitacora("Ejecución exitosa de la subopción 1: filtrar por día")
    input("Presione ENTER para continuar")
    
def filtrarPorDia(pfecha):
    bitacora=open("bitacora.txt","r", encoding="utf-8")
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
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no ingresó un nada")
    if not filtrarPorPalabraClave(palabra):
        print("No se encontró nongún registro con esa palabra clave")
        input("Presione ENTER para continuar")
        inservarEnBitacora("Error al filtrar cada registro de la bitácora: no se encontró la palabra que puso el usuario")
        return
    inservarEnBitacora("Ejecución exitosa de la subopción 2: filtrar por palabra clave")
    input("Presione ENTER para continuar")
    return

def filtrarPorPalabraClave(ppalabra):
    encontrar=False
    bitacora=open("bitacora.txt","r", encoding="utf-8")
    for i in bitacora.readlines():
        texto = i.split(",")[1]
        for palabra in texto.split():
            if re.sub(r'[^a-zA-Zá-úä-üÁ-ÚÄ-Ü0-9\s]', '', palabra) == ppalabra:
                print(i)
                encontrar=True
    bitacora.close()
    return encontrar