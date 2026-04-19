# Python
def contar_personajes(tablero):
    return sum(1 for fila in tablero
               for celda in fila
               if celda is not None)
