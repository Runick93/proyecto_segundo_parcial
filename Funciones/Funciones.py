from Utils import *


def inicializar_tablero() -> dict:
    matriz_tablero = inicializar_matriz(10, 10)
    diccionario_juego = cargar_naves(matriz_tablero)

    return diccionario_juego

def comenzar_juego():
    diccionario_juego = inicializar_tablero()
    print(diccionario_juego["submarino_1"])
    #Capturar la posicion de la cuadricula donde el usuario hace click -> pygame.mouse.get_pos() -> devuelve tupla
    #buscar la cordenada en la matriz y verificar si hay un 0 y 1 -> para ver si le pego a algo



if __name__ == "__main__":
    print(inicializar_tablero())