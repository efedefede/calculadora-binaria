import colorama
import validacion
import suma_resta
from div_multi import *
import os
import time
import conversores

def limpiar_pantalla():
    """
    Limpia la consola, utiliza un if para verificar el sistema operativo actual y utiliza el comando correspondiente
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_bienvenida():
    """
    Muestra el mensaje de bienvenida
    """
    limpiar_pantalla()
    cuadro_colorido("Hola que tal bienvenido/a a la validadora de calculo binario del grupo 3", colorama.Fore.GREEN)
    time.sleep(3)
    limpiar_pantalla()

def cuadro_colorido(texto, color):
    """
    Cuadro colorido que encierra la salida y la hace mas bella.
    """
    longitud = len(texto) + 4
    print(color + "+" + "-" * longitud + "+" + colorama.Style.RESET_ALL)
    print(color + "|  " + texto + "  |" + colorama.Style.RESET_ALL)
    print(color + "+" + "-" * longitud + "+" + colorama.Style.RESET_ALL)

def linea_final(texto, color):
    """
    Linea de final de la consola que hace mas bella la salida
    """
    longitud = len(texto) + 4
    print(color + "+" + "-" * longitud + "+" + colorama.Style.RESET_ALL)

def imprimir_resultado(op: str, bin1: str, bin2: str, resultado: str):
    """
    Funcion que imprime el resultado en binario en la consola.
    """
    texto_resultado = ("El resultado es")
    cuadro_colorido(texto_resultado, colorama.Fore.GREEN)
    print(colorama.Fore.MAGENTA + f"Operacion: {op}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + f"Primer binario: {bin1}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + f"Segundo binario: {bin2}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + f"Resultado: {resultado}" + colorama.Style.RESET_ALL)
    linea_final(texto_resultado, colorama.Fore.GREEN)
    

def test_automatico(op: str, bin1: str, bin2: str, resultado: str):
    """
    Test realizado para validar la correcta realizacion de las operaciones, este mismo lo que hace es convertir
    los numeros binarios implicados a decimal, luego compara el resultado de la operacion en decimal con la conversion
    a decimal del resultado que fue hecho previamente por la calculadora en binario.
    Al ser correcto el programa activara la bandera y retornara el booleano.
    """
    todo_correcto = False
    
    if (op == "Suma"):
        resultado_decimal = conversores.binario_a_decimal(bin1) + conversores.binario_a_decimal(bin2)
    elif (op == "Resta"):
        resultado_decimal = conversores.binario_a_decimal(bin1) - conversores.binario_a_decimal(bin2)
    elif (op) == "Multiplicacion":
        resultado_decimal = conversores.binario_a_decimal(bin1) * conversores.binario_a_decimal(bin2)
    elif (op == "Division"):
        resultado_decimal = conversores.binario_a_decimal(bin1) / conversores.binario_a_decimal(bin2)
    
    if (resultado_decimal == conversores.binario_a_decimal(resultado)):
        todo_correcto = True
    
    return todo_correcto

def operacion_a_texto(opcion):
    """
    Funcion que realiza una conversion del numero que tiene que ingresar el usuario a formato texto 
    para representar la operacion como una palabra para su posterior validacion.
    """
    if (opcion == 1):
        return "Suma"
    elif (opcion == 2):
        return "Resta"
    elif (opcion == 3):
        return "Multiplicacion"
    elif (opcion == 4):
        return "Division"
    else:
        return "Error. Usted ingresó una opción no válida."

def menu_operacion(texto_operacion: str):
    opcion = 1
    opciones_validas = {1,2,3,4,5}  #Posibles opciones válidas de menú
        
    while opcion != 5:
        cuadro_colorido(texto_operacion, colorama.Fore.GREEN)
        print(colorama.Fore.MAGENTA + "1. Suma.  " + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + "2. Resta. " + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + "3. Multiplicacion. " + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + "4. Division. " + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + "5. Salir. " + colorama.Style.RESET_ALL)
        linea_final(texto_operacion, colorama.Fore.GREEN)
        #Consulto la opción deseada
        opcion = int(input())
        #Devuelvo la opción como un string
        texto_operacion = operacion_a_texto(opcion)
        
        #Si la opción ingresada está dentro de las posibles 
        if opcion in opciones_validas:
                
                #Solicito los binarios a operar y valido que sean correctos
                bin1 = input(colorama.Fore.MAGENTA + "Ingrese el primer binario: " + colorama.Style.RESET_ALL)
                while not validacion.es_binario(bin1):
                    bin1 = input("Ingrese otro numero: \n")
                bin2 = input(colorama.Fore.MAGENTA + "Ingrese el segundo binario: " + colorama.Style.RESET_ALL)
                while not validacion.es_binario(bin2):
                    bin2 = input("Ingrese otro numero: \n")
            
                if (opcion == 1): # 1 -> suma
                    resultado = suma_resta.suma_binaria(bin1, bin2)
                    if test_automatico(texto_operacion, bin1, bin2, resultado):
                        imprimir_resultado(texto_operacion, bin1, bin2, resultado)
                        break
                
                elif (opcion == 2): # 2 -> resta
                    resultado = suma_resta.resta_binaria(bin1,bin2)
                    if test_automatico(texto_operacion, bin1, bin2, resultado):
                        imprimir_resultado(texto_operacion, bin1, bin2, resultado)
                
                elif (opcion == 3): # 3 -> Multiplicación
                    resultado = multiplicacion_binaria(bin1,bin2)
                    if test_automatico(texto_operacion, bin1, bin2, resultado):
                        imprimir_resultado(texto_operacion, bin1, bin2, resultado)
                
                elif (opcion == 4): # 4 -> Division
                    resultado = division_binaria(bin1,bin2)
                    if test_automatico(texto_operacion, bin1, bin2, resultado):
                        imprimir_resultado(texto_operacion, bin1, bin2, resultado)
