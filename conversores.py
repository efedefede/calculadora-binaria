def decimal_a_binario(decimal):
    """
    Convierte un número decimal entero a su representación binaria como string.
    
    Args:
        decimal (int): Número decimal entero positivo
        
    Returns:
        str: Cadena que representa el número en binario
        
    Example:
        >>> decimal_a_binario(10)
        '1010'
    """
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

def binario_a_decimal(binario):
    """
    Convierte un número binario (como string) a su equivalente decimal.
    
    Args:
        binario (str): Cadena que representa el número binario
        
    Returns:
        int: Número decimal equivalente
        
    Example:
        >>> binario_a_decimal('1010')
        10
    """

    decimal = 0
    longitud = len(binario)
    
    for i in range(longitud - 1, -1, -1):
        digito = binario[i] 
        potencia = longitud - i - 1  
        decimal += int(digito) * (2 ** potencia)
    
    return decimal

