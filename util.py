def calcular_media(lista):
    """Calcula a média de uma lista de números."""
    if not lista:  
        return 0
    return sum(lista) / len(lista)
