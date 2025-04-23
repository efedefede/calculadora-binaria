from .conversores import *

#           Suma binaria

def suma_binaria(bin1: str, bin2: str):
    """
    Args:
        bin1 (str): un string que representa un número binario
        bin2 (str): un string que representa un número binario

    Returns:
        str: retorna un string que representa la suma entre bin1 y bin2

    Example:
        >>> suma_binaria('10', '11')
        '101'
    """
    dec1 = int(binario_a_decimal(bin1))
    dec2 = int(binario_a_decimal(bin2))
    return decimal_a_binario(dec1 + dec2)

#           Resta binaria

def resta_binaria(bin1: str, bin2: str):
    """
    Args:
        bin1 (str): un string que representa un número binario
        bin2 (str): un string que representa un número binario

    Returns:
        str: retorna un string que representa la resta entre bin1 y bin2.
        Retorna un mensaje de error si el resultado es negativo.

    Example:
        >>> resta_binaria('100', '11')
        '1'
    """
    dec1 = int(binario_a_decimal(bin1))
    dec2 = int(binario_a_decimal(bin2))
    if dec1 >= dec2:
        return decimal_a_binario(dec1 - dec2)
    else:
        return "ERROR: la resta da un número negativo."