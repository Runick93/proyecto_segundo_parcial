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
        "puntaje": 0000,
        "selection": []
    }
    return dict_jugador