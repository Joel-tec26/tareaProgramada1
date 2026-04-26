#Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 24/04/2026 9:30pm
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
                return tokens 
            except Exception :
                print(" Caracteristica inesperada encontrada al leer el archivo")
        opcion = input("\n¿Desea intentar de nuevo con otra ruta? \nDigite (1) para continuar \nDigite (2) para salir: ")
        if opcion != "1":
            print("Operación cancelada.")
            return []


# Programa principal de pruebas

lista = administradorOpcion1()
