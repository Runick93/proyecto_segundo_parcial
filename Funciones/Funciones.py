from Utils import *


def inicializar_tablero() -> list:
    tablero = inicializar_matriz(10, 10)
    #imprimir_tablero(tablero)
    print("")
    tablero = cargar_naves(tablero)
    imprimir_tablero(tablero)


if __name__ == "__main__":
    print(inicializar_tablero())