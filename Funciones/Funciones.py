from Funciones.Utils import *


def inicializar_juego() -> dict:
    matriz_tablero = inicializar_matriz(10, 10)
    dict_juego = inicializar_naves(matriz_tablero)
    imprimir_tablero(dict_juego["tablero"]) #For debug.
    return dict_juego

def inicializar_jugador() -> dict:
    dict_jugador = {
        "disparos_acertados": [],
        "disparos_no_acertados": [],
        "puntaje": "0000"
    }
    return dict_jugador

# def comenzar_juego():
#     diccionario_juego = inicializar_tablero()
    #print(diccionario_juego["submarino_1"])
    #Capturar la posicion de la cuadricula donde el usuario hace click -> pygame.mouse.get_pos() -> devuelve tupla
    #buscar la cordenada en la matriz y verificar si hay un 0 y 1 -> para ver si le pego a algo



# if __name__ == "__main__":
#     print(inicializar_tablero())