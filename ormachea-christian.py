from colorama import Fore, Back, Style
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
    cuadro_colorido("Hola que tal bienvenido/a a la calculadora binaria del grupo 3", Fore.GREEN)
    time.sleep(3)
    limpiar_pantalla()

def cuadro_colorido(texto, color):
    """
    Cuadro colorido que encierra la salida y la hace mas bella.
    """
    longitud = len(texto) + 4
    print(color + "+" + "-" * longitud + "+" + Style.RESET_ALL)
    print(color + "|  " + texto + "  |" + Style.RESET_ALL)
    print(color + "+" + "-" * longitud + "+" + Style.RESET_ALL)

def linea_final(texto, color):
    """
    Linea de final de la consola que hace mas bella la salida
    """
    longitud = len(texto) + 4
    print(color + "+" + "-" * longitud + "+" + Style.RESET_ALL)

def imprimir_resultado(op: str, bin1: str, bin2: str, resultado: str):
    """
    Funcion que imprime el resultado en binario en la consola.
    """
    texto_resultado = ("El resultado es")
    cuadro_colorido(texto_resultado, Fore.GREEN)
    print(Fore.MAGENTA + f"Operacion: {op}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Primer binario: {bin1}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Segundo binario: {bin2}" + Style.RESET_ALL)
    linea_final(texto_resultado, Fore.GREEN)
    

def test_automatico(op: str, bin1: str, bin2: str, resultado: str):
    """
    Test realizado para validar la correcta realizacion de las operaciones, este mismo lo que hace es convertir
    los numeros binarios implicados a decimal, luego compara el resultado de la operacion en decimal con la conversion
    a decimal del resultado que fue hecho previamente por la calculadora en binario.
    Al ser correcto el programa activara la bandera y retornara el booleano.
    """
    todo_correcto = False
    
    if (op == "Suma"):
        resultado_decimal = conversores.binario_a_decimal(int(bin1)) + conversores.binario_a_decimal(int(bin2))
    elif (op == "Resta"):
        resultado_decimal = conversores.binario_a_decimal(int(bin1)) - conversores.binario_a_decimal(int(bin2))
    elif (op) == "Multiplicacion":
        resultado_decimal = conversores.binario_a_decimal(int(bin1)) * conversores.binario_a_decimal(int(bin2))
    elif (op == "Division"):
        resultado_decimal = conversores.binario_a_decimal(int(bin1)) / conversores.binario_a_decimal(int(bin2))
    
    if (resultado_decimal == conversores.binario_a_decimal(resultado)):
        todo_correcto = True
    
    return todo_correcto

def operacion_a_texto(opcion: int):
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
        return "Error"

def menu_operacion(texto_operacion: str):
    while opcion != 5:
        cuadro_colorido(texto_operacion, Fore.GREEN)
        print(Fore.MAGENTA + "1. Suma.  " + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. Resta. " + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. Multiplicacion. " + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Division. " + Style.RESET_ALL)
        print(Fore.MAGENTA + "5. Salir. " + Style.RESET_ALL)
        linea_final(texto_operacion, Fore.GREEN)
        opcion = int(input())
        texto_operacion = operacion_a_texto(opcion)
        
        if (opcion == 1):
            bin1 = int(input(Fore.MAGENTA + "Ingrese el primer binario: " + Style.RESET_ALL))
            bin2 = int(input(Fore.MAGENTA + "Ingrese el segundo binario: " + Style.RESET_ALL))
            resultado = "11101"
            if test_automatico(texto_operacion, bin1, bin2, resultado):
                imprimir_resultado(texto_operacion, bin1, bin2, resultado)
            #else con el error a manejar
        elif (opcion == 2):
            bin1 = int(input(Fore.MAGENTA + "Ingrese el primer binario: " + Style.RESET_ALL))
            bin2 = int(input(Fore.MAGENTA + "Ingrese el segundo binario: " + Style.RESET_ALL))
            resultado = "111010"
            if test_automatico(texto_operacion, bin1, bin2, resultado):
                imprimir_resultado(texto_operacion, bin1, bin2, resultado)
                #else con el error a manejar
        elif (opcion == 3):
            bin1 = int(input(Fore.MAGENTA + "Ingrese el primer binario: " + Style.RESET_ALL))
            bin2 = int(input(Fore.MAGENTA + "Ingrese el segundo binario: " + Style.RESET_ALL))
            resultado = "111010"
            if test_automatico(texto_operacion, bin1, bin2, resultado):
                imprimir_resultado(texto_operacion, bin1, bin2, resultado)
                #else con el error a manejar
        elif (opcion == 3):
            bin1 = int(input(Fore.MAGENTA + "Ingrese el primer binario: " + Style.RESET_ALL))
            bin2 = int(input(Fore.MAGENTA + "Ingrese el segundo binario: " + Style.RESET_ALL))
            resultado = "111010"
            if test_automatico(texto_operacion, bin1, bin2, resultado):
                imprimir_resultado(texto_operacion, bin1, bin2, resultado)
                #else con el error a manejar
        elif (opcion == 4):
            bin1 = int(input(Fore.MAGENTA + "Ingrese el primer binario: " + Style.RESET_ALL))
            bin2 = int(input(Fore.MAGENTA + "Ingrese el segundo binario: " + Style.RESET_ALL))
            resultado = "111010"
            if test_automatico(texto_operacion, bin1, bin2, resultado):
                imprimir_resultado(texto_operacion, bin1, bin2, resultado)
                #else con el error a manejar


def main():
    """
    Funcion principal, donde ejecuto mi menu y testeo para poder mostrar el resultado asegurando
    un correcto funcionamiento de la calculadora testeando el resultado.
    """
    opcion = 0
    texto_operacion = "Que operacion necesita realizar?"
    mostrar_bienvenida()
    menu_operacion()


if __name__ == "__main__":
    main()