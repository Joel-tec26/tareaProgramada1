#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 26/04/2026 8:20am
# Ultíma modificación: 
# Versión: 3.14

# importaciones de metodos
import re
import os

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
            print("El separador debe ser exactamente un símbolo (ni letras, ni números, ni espacios.")
        


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
                    pareja = (token1, token2)
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
            plistaTokens[indice] = (llave, valor)
        else:
            print(f"Se a añadido nuevo token: ({llave}, {valor})")
            plistaTokens.append((llave, valor))
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


# Programa principal de pruebas

listaGlobal = []
while True:
    print("\n Menu tester")
    print("1. cargar")
    print("2. Agregar/Actualizar")
    print("3. Ver Lista")
    print("4. Salir")
    op = input("Seleccione: ")
    if op == "1":
        listaGlobal = administradorOpcion1()
    elif op == "2":
        listaGlobal = administradorOpcion2(listaGlobal)
    elif op=="3":
        print(f"\nLista actual: {listaGlobal}")
    elif op == "4":
        break
