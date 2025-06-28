from Funciones.Utils import *
import pygame


def inicializar_juego() -> dict:
    """
    Inicializa el juego creando el tablero y ubicando las naves.

    Args:
        None

    Returns:
        dict: Diccionario que contiene el estado inicial del juego, incluyendo el tablero con las naves posicionadas.
    """

    matriz_tablero = inicializar_matriz(10, 10)
    dict_juego = inicializar_naves(matriz_tablero)
    imprimir_tablero(dict_juego["tablero"]) #Para debug.
    return dict_juego

def inicializar_jugador() -> dict:
    """
    Crea e inicializa un diccionario con la informacion del jugador.

    Args:
        None

    Returns:
        dict: Diccionario con los datos iniciales del jugador, incluyendo nombre, disparos, naves destruidas, puntaje y seleccion actual.
    """

    dict_jugador = {
        "nombre_usuario": "",
        "nombre_insertado": False,
        "disparos_acertados": [],
        "disparos_no_acertados": [],
        "naves_destruidas": 0,
        "puntaje": 0000,
        "selection": []
    }
    return dict_jugador

def inicializar_aplicacion() -> dict:
    """
    Inicializa los recursos visuales y de configuracion de la aplicacion.

    Args:
        None

    Returns:
        dict: Diccionario con la configuracion inicial de la aplicacion, incluyendo imagenes, iconos, musica de fondo y pantallas.
    """

    dict_aplicacion = {
        "musica_fondo": True,
        "imagen_fondo": pygame.image.load("Imagenes/imagen_menu.jpg"),
        "imagen_musica_activa": pygame.transform.scale(pygame.image.load("Imagenes/musica_activa.png"), (40, 40)),
        "imagen_musica_inactiva": pygame.transform.scale(pygame.image.load("Imagenes/musica_inactiva.png"), (40, 40)),
        "agua_tablero": pygame.transform.scale(pygame.image.load("Imagenes/agua_tablero.png"), (40, 40)),
        "cruz_negra": pygame.transform.scale(pygame.image.load("Imagenes/cruz_negra.png"), (30, 30)),
        "cruz_negra": pygame.transform.scale(pygame.image.load("Imagenes/cruz_negra.png"), (30, 30)),
        "icono_juego": pygame.image.load("Imagenes/icono_juego.jpg"),
        "pantalla_ingresar_nombre": pygame.transform.scale(pygame.image.load("Imagenes/pantalla_ingresar_nombre.png"), (800, 600)),
        "pantalla_puntaje": pygame.transform.scale(pygame.image.load("Imagenes/pantalla_puntajes.jpg"), (800, 600)),
    }
    return dict_aplicacion