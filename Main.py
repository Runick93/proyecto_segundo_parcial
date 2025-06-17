import pygame
import pygame.mixer as mixer
from Funciones_Juego.Funciones_Juegos import *
from Funciones.Funciones import inicializar_tablero


pygame.init()
mixer.init()

pantalla = pygame.display.set_mode((800,600))
fondo_imagen = pygame.image.load("proyecto_segundo_parcial/Imagenes/imagen_menu.jpg")

pygame.display.set_caption("Batalla Naval")
imagen = pygame.image.load("proyecto_segundo_parcial/Imagenes/icono_juego.jpg")
pygame.display.set_icon(imagen)

#mixer.music.load("proyecto_segundo_parcial/Sonidos/musica_fondo.mp3")
#mixer.music.set_volume(0.4)
#mixer.music.play(loops=-1)

menu_inicio = "inicio"  
tablero = inicializar_tablero()
matriz_tablero = tablero["tablero"]


while True:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if menu_inicio == "inicio":
                menu_inicio = seleccionar_botones(pantalla, eventos, matriz_tablero)
            
            posicion_mouse = pygame.mouse.get_pos()
            coordenadas_menu = pygame.Rect(20,15,95,55)

            if coordenadas_menu.collidepoint(posicion_mouse):
                menu_inicio = "inicio"

    if menu_inicio == "inicio":
        pantalla.blit(fondo_imagen, [0,0])
    elif menu_inicio == "nivel":
        pantalla.fill((0,0,0))
        menu_inicio = pantalla_nivel(pantalla)
    elif menu_inicio == "juego":
        pantalla.fill((0,0,0))
        pantalla_juego(pantalla, eventos,matriz_tablero)
    elif menu_inicio == "puntaje":
        pantalla.fill((0,0,0))
        menu_inicio = pantalla_puntaje(pantalla)
    elif menu_inicio == "salir":
        pygame.quit()
        quit()

    pygame.display.flip()