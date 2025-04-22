### Funcion para validar si el numero es binario ###

def es_binario(cadena):
    
    # Se convierte el numero dado en una cadena
    
    cadena = str(cadena)
    
    # Ahora que lo convertimos en cadena nos permite recorrerla caracter por caracter en un ciclo for

    for caracter in cadena:
        # En este if se analiza si algun caracter no esta comprendido en la tupla  
        if caracter not in ("0","1"):
            return False
        # Si se encuentra uno solo que no sea 0 o 1, nos devuelve falso como resultado
    
    return True
    # Nos devuelve verdadero si todos los valores del caracter fueron 0 o 1


### TEST ###
cadena = input("ingrese un numero binario: ")

if es_binario(cadena):
    print("Es un numero binario")
else:
    print("Es un numero binario")