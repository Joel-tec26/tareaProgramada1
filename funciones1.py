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


        
# mostrar tokens

def mostrarTokens(ptokens):
    """
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
    """
    posicionActual = 0
    for pareja in plistaDeTokens:
        if pareja[0] == palabraBuscada:
            return posicionActual
        posicionActual += 1
    return False




def procesarActualizacionDeTokens(pcadenaNueva, pseparador, plistaTokens):
    """
    """
    confirmacion= input("¿Desea continuar en el proceso? \nDigite [1] para continuar o [2] para cancelar el proceso: ")
    if confirmacion == "1":
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
    else:
        print ("Proceso cancelado")
        return plistaTokens


# guardar tokens en archivo

def procesarGuardadoTokens(pTokensm, pArchivo, pSeparador):
    """
    """
    archivoObjeto = open(f"{pArchivo}.txt", "a", encoding="utf-8")
    for i in pTokensm:
        archivoObjeto.write(f"{i[0]}{pSeparador}{i[1]}\n")
    archivoObjeto.close()

#traducir codigo

def TraduccionPalabra2(pPalabra, pListaTokens):
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
                resultado = TraduccionPalabra2(fragmento, pListaTokens)
                lineaTraducida += resultado
                conteoPalabrasLinea += 1
            else:
                lineaTraducida += fragmento
    return lineaTraducida, conteoPalabrasLinea


#generar reporte CSV



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


# submenú bitacora

def inservarEnBitacora(pdescripcion):
    fecha=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    bitacora=open("bitacora.txt","a", encoding="utf-8")
    bitacora.write(f"({fecha},{pdescripcion})\n")
    bitacora.close()
    return

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