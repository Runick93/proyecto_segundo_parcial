import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas:int, valor_inicial: any = 0) -> list:
    """
    Funcion que permite inicializar una matriz con las respectivas filas y columnas indicadas por parametro

    Args:
        cantidad_filas (int): La cantidad de filas que tendra la matriz
        cantidad_columnas (int): La cantidad de columnas que tendra la matriz
        valor_inicial (any, optional): description. Defaults to 0. El valos con el cual se inicializara la matriz

    Returns:
        list: Una matriz con las columnas, filas y inicializada con los valores recibidos por parametro
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
    return matriz

def cargar_naves(tablero:list) -> list:
    for i in range(40):        
        
        rnd_fila = random.randint(0, len(tablero) - 1)
        rnd_col =  random.randint(0, len(tablero) - 1)  
    
        while tablero[rnd_fila][rnd_col] == 1: 
            print(f"Se superpusieron submarinos. Fila: {rnd_fila}, Col: {rnd_col}")
            rnd_fila = random.randint(0, len(tablero) - 1)
            rnd_col =  random.randint(0, len(tablero) - 1)        
            

        tablero[rnd_fila][rnd_col] = 1

    return tablero



#imprimir matriz
def imprimir_tablero(matriz_notas:list):
    """
    Imprime tablero
    
    Args:
        matriz_notas: Son las notas de las materias de los alumnos.
    Returns:
        None.
    """
    for i in range(len(matriz_notas)):        
        for j in range(len(matriz_notas[i])):
            print(matriz_notas[i][j], end=" | ")
        print("")