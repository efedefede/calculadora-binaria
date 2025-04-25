import conversores
# Multiplicación Binaria

def multiplicacion_binaria (bin1: str, bin2: str):
    """
    Args:
        bin1 (str): un string que representa un número binario
        bin2 (str): un string que representa un número binario
        
    Returns:
        str: retorna un string que representa la multiplicación entre bin1 y bin2
        
    Example:
        >>> multiplicacion_binaria ('10', '10')
        '100'
    
    """
    dec1 = int(conversores.binario_a_decimal(bin1))
    dec2 = int(conversores.binario_a_decimal(bin2))
    return conversores.decimal_a_binario(dec1*dec2)

# División binaria 

def division_binaria(bin1: str, bin2: str):
    """
    Args:
        bin1 (str): un string que representa un número binario
        bin2 (str): un string que representa un número binario
        
    Returns:
        str: retorna un string que representa la división entera entre bin1 y bin2.
        Retorna un mensaje de error si el divisor es 0
        
    Example:
        >>> division_binaria ('100', '10')
        '10'
    
    """
    dec1 = int(conversores.binario_a_decimal(bin1))
    dec2 = int(conversores.binario_a_decimal(bin2))
    if dec2 != 0 :
        return conversores.decimal_a_binario(dec1//dec2)
    else:
        return (f"ERROR: no se puede dividir por cero.")