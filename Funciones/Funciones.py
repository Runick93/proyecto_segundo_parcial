from Funciones.Utils import *
import pygame


def inicializar_juego() -> dict:
    matriz_tablero = inicializar_matriz(10, 10)
    dict_juego = inicializar_naves(matriz_tablero)
    imprimir_tablero(dict_juego["tablero"]) #For debug.
    return dict_juego

def inicializar_jugador() -> dict:
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
    dict_aplicacion = {
        "musica_fondo": True,
        "imagen_fondo": pygame.image.load("Imagenes/imagen_menu.jpg"),
        "imagen_musica_activa": pygame.transform.scale(pygame.image.load("Imagenes/musica_activa.png"), (40, 40)),
        "imagen_musica_inactiva": pygame.transform.scale(pygame.image.load("Imagenes/musica_inactiva.png"), (40, 40)),
        "agua_tablero": pygame.transform.scale(pygame.image.load("Imagenes/agua_tablero.png"), (40, 40)),
        "cruz_negra": pygame.transform.scale(pygame.image.load("Imagenes/cruz_negra.png"), (30, 30)),
        "cruz_negra": pygame.transform.scale(pygame.image.load("Imagenes/cruz_negra.png"), (30, 30)),
        "icono_juego": pygame.image.load("Imagenes/icono_juego.png"),
        "pantalla_ingresar_nombre": pygame.transform.scale(pygame.image.load("Imagenes/pantalla_ingresar_nombre.jpg"), (800, 600)),
        "pantalla_puntaje": pygame.transform.scale(pygame.image.load("Imagenes/pantalla_puntajes.jpg"), (800, 600)),
    }
    return dict_aplicacion