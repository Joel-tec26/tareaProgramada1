#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 21/04/2026 8:20am
# Ultíma modificación: 30/04/2026 
# Versión: 3.14

# importaciones de metodos
import re
from datetime import datetime


# definicion de funciones 

# funciones opción 1 del menú 

def procesarArchivo1(pruta, pseparador):
    """
    Funcionalidad:
    Lee un archivo de texto, extrae tokens separados por un símbolo específico
    y almacena únicamente los tokens válidos y no repetidos.
    Entradas:
    -pruta(str): ruta o nombre del archivo que contiene los tokens
    -pseparador(str): símbolo utilizado para separar los tokens
    Salidas:
    -listaTokens(list): lista de tuplas con tokens válidos encontrados
    -mensaje(str): mensajes mostrados en pantalla sobre líneas inválidas o sin separador
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
 
# mostrar tokens

def mostrarTokens(ptokens):
    """
    Funcionalidad:
    Muestra en pantalla la lista de tokens y sus traducciones.
    Entradas:
    -ptokens(list): lista de tokens almacenados
    Salidas:
    -resultado(bool): True si existen tokens para mostrar, False si la lista está vacía
    -mensaje(str): impresión en pantalla de los tokens y traducciones
    """
    if ptokens==[]:
        return False
    print("Token\t\tTraduccion\n")
    for i in ptokens:
        print(f"{i[0]}"+" "*(20-len(i[1]))+f"{i[1]}")
    return True

# agregar o actualizar tokens

def buscarToken(palabraBuscada, plistaDeTokens):
    """
    Funcionalidad:
    Busca un token específico dentro de la lista de tokens.
    Entradas:
    -palabraBuscada(str): token que se desea localizar
    -plistaDeTokens(list): lista de tokens donde se realizará la búsqueda
    Salidas:
    -posicionActual(int): posición donde se encuentra el token
    -resultado(-1): si el token no existe en la lista
    """
    posicionActual = 0
    for pareja in plistaDeTokens:
        if pareja[0] == palabraBuscada:
            return posicionActual
        posicionActual += 1
    return -1

def procesarActualizacionDeTokens(pcadenaNueva, pseparador, plistaTokens):
    """
    Funcionalidad:
    Agrega nuevos tokens o actualiza tokens existentes en la lista principal.
    Entradas:
    -pcadenaNueva(str): cadena con los nuevos tokens ingresados por el usuario
    -pseparador(str): símbolo separador utilizado entre token y traducción
    -plistaTokens(list): lista actual de tokens
    -confirmacion(str): confirmación ingresada por el usuario para continuar o cancelar
    Salidas:
    -plistaTokens(list): lista de tokens actualizada
    -mensaje(str): mensajes mostrados en pantalla sobre actualizaciones, inserciones o cancelación
    """
    confirmacion= input("¿Desea continuar en el proceso? \nDigite [1] para continuar o [2] para cancelar el proceso: ")
    if confirmacion == "1":
        bloques = pcadenaNueva.split()
        for bloque in bloques:
            partes = bloque.split(pseparador)
            llave = partes[0].strip()
            valor = partes[1].strip()
            indice = buscarToken(llave, plistaTokens)
            if indice != -1:
                print(f"El token existente: {llave}, ahora es: {valor}")
                plistaTokens[indice] = (llave, valor, 0)
            else:
                print(f"Se a añadido nuevo token: ({llave}, {valor})")
                plistaTokens.append((llave, valor, 0))
        return plistaTokens
    else:
        inservarEnBitacora("El usuario cancelo el proceso de actualización de tokens")
        print ("Proceso cancelado")
        return plistaTokens


# guardar tokens en archivo

def procesarGuardadoTokens(pTokensm, pArchivo, pSeparador):
    """
    Funcionalidad:
    Guarda los tokens en un archivo de texto utilizando un separador definido.
    Entradas:
    -pTokensm(list): lista de tokens que se desea guardar
    -pArchivo(str): nombre del archivo destino
    -pSeparador(str): símbolo separador entre token y traducción
    Salidas:
    -archivo(txt): archivo de texto generado con los tokens almacenados
    """
    archivoObjeto = open(f"{pArchivo}.txt", "a", encoding="utf-8")
    for i in pTokensm:
        archivoObjeto.write(f"{i[0]}{pSeparador}{i[1]}\n")
    archivoObjeto.close()

#traducir codigo

def TraduccionPalabra2(pPalabra, pListaTokens):
    """
    Funcionalidad:
    Traduce una palabra utilizando la lista de tokens y actualiza
    la cantidad de reemplazos realizados.
    Entradas:
    -pPalabra(str): palabra que se desea traducir
    -pListaTokens(list): lista de tokens disponibles para traducción
    Salidas:
    -traduccion(str): palabra traducida o palabra original si no existe traducción
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
    Funcionalidad:
    Procesa una línea de texto, traduce las palabras utilizando
    los tokens disponibles y cuenta las palabras procesadas.
    Entradas:
    -pLinea(str): línea de texto que se desea procesar
    -pListaTokens(list): lista de tokens utilizados para la traducción
    Salidas:
    -lineaTraducida(str): línea traducida
    -conteoPalabrasLinea(int): cantidad de palabras procesadas en la línea
    """
    partes = re.split(r'([^a-zA-Z0-9áéíóúÁÉÍÓÚ])', pLinea)
    lineaTraducida = ""
    conteoPalabrasLinea = 0
    for fragmento in partes:
        if fragmento: 
            if fragmento.isalnum():
                resultado = TraduccionPalabra2(fragmento, pListaTokens)
                lineaTraducida += resultado
                conteoPalabrasLinea += 1
            else:
                lineaTraducida += fragmento
    return lineaTraducida, conteoPalabrasLinea


#generar reporte CSV

def generarReporteCSV(pcambios):
    """
    Funcionalidad:
    Genera un archivo CSV con el registro de palabras reemplazadas
    y la cantidad de veces que fueron traducidas.
    Entradas:
    -pcambios(list): lista de tokens con información de reemplazos
    Salidas:
    -archivo(csv): archivo CSV generado con el reporte
    -resultado(bool): True si el proceso finaliza correctamente
    """
    archivo = open("reporte.csv","a", encoding="utf-8")
    for i in pcambios:
        if i[2]>0:
            archivo.write(f"Palabra original: {i[0]}\t|\tToken de cambio: {i[1]}\t|\tCantidad de reeplazos: {i[2]}\n")
    archivo.close()
    return True

#generar reporte HTML

def calcularEstadisticas(pListaTokens, pTotalPalabras):
    """
    Funcionalidad:
    Calcula estadísticas relacionadas con el proceso de traducción.
    Entradas:
    -pListaTokens(list): lista de tokens con cantidades de reemplazo
    -pTotalPalabras(int): cantidad total de palabras procesadas
    Salidas:
    -totalReemplazos(int): cantidad total de reemplazos realizados
    -porcentaje(float): porcentaje de palabras reemplazadas
    """
    totalReemplazos = 0
    for tupla in pListaTokens:
        totalReemplazos += tupla[2] 
    if pTotalPalabras > 0:
        porcentaje = (totalReemplazos / pTotalPalabras) * 100
    else:
        porcentaje = 0
    return totalReemplazos, porcentaje

def CuerpoHTML(pTituloPestanna, pFechaHora, pEstadisticas, pListaTokens, ptiempoTraduccion):
    """
    Funcionalidad:
    Construye el contenido HTML de un reporte de traducción.
    Entradas:
    -pTituloPestanna(str): título del reporte HTML
    -pFechaHora(str): fecha y hora de generación del reporte
    -pEstadisticas(tupla): estadísticas del proceso de traducción
    -pListaTokens(list): lista de tokens con información de reemplazos
    -ptiempoTraduccion(float): tiempo total de traducción
    Salidas:
    -html(str): contenido HTML completo del reporte
    """
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


# submenú bitacora

def inservarEnBitacora(pdescripcion):
    """
    Funcionalidad:
    Registra una acción o evento dentro del archivo de bitácora del sistema.
    Entradas:
    -pdescripcion(str): descripción del evento que se desea registrar
    Salidas:
    -archivo(txt): actualización del archivo bitacora.txt con el nuevo registro
    """
    fecha=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    bitacora=open("bitacora.txt","a", encoding="utf-8")
    bitacora.write(f"({fecha},{pdescripcion})\n")
    bitacora.close()
    return

def filtrarPorDia(pfecha):
    """
    Funcionalidad:
    Busca y muestra registros de la bitácora correspondientes
    a una fecha específica.
    Entradas:
    -pfecha(str): fecha que se desea buscar en la bitácora
    Salidas:
    -resultado(bool): True si se encontraron registros, False en caso contrario
    -mensaje(str): registros encontrados mostrados en pantalla
    """
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

def filtrarPorPalabraClave1(ppalabra):
    """
    Funcionalidad:
    Busca y muestra registros de la bitácora que contengan
    una palabra clave específica.
    Entradas:
    -ppalabra(str): palabra clave que se desea buscar
    Salidas:
    -resultado(bool): True si se encontraron coincidencias, False en caso contrario
    -mensaje(str): registros encontrados mostrados en pantalla
    """
    import os
    encontrar = False
    if not os.path.exists("bitacora.txt"):
        return False
    bitacora = open("bitacora.txt", "r", encoding="utf-8")
    for i in bitacora:
        linea = i.strip()
        if not linea or "," not in linea:
            continue 
        partes = linea.split(",")
        if len(partes) >= 2:
            texto = partes[1]
            for palabra in texto.split():
                palabraLimpia = re.sub(r'[^a-zA-Zá-úä-üÁ-ÚÄ-Ü0-9]', '', palabra)
                if palabraLimpia == ppalabra:
                    print(linea) 
                    encontrar = True
    bitacora.close()
    return encontrar