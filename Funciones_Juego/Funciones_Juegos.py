import pygame

def pantalla_nivel(pantalla):
    pygame.draw.rect(pantalla, 'pink', [100,100,300,300])

def pantalla_juego(pantalla):
    pygame.draw.rect(pantalla, 'white', [100,100,300,300])

def pantalla_puntaje(pantalla):
    fondo_imagen = pygame.image.load("proyecto_segundo_parcial/Imagenes/pantalla_puntajes.jpg")
    pantalla.blit(fondo_imagen, [0,0])

def seleccionar_botones(pantalla):
    posicion_mouse = pygame.mouse.get_pos()

    coordenadas_nivel = pygame.Rect(139, 320, 215, 80)
    coordenadas_jugar = pygame.Rect(421, 320, 236, 80)
    coordenadas_puntaje = pygame.Rect(133, 430, 215, 80)
    coordenadas_salir = pygame.Rect(450, 430, 215, 80)

    estado_pantalla = ""

    if coordenadas_nivel.collidepoint(posicion_mouse):
        estado_pantalla = "nivel"
    elif coordenadas_jugar.collidepoint(posicion_mouse):
        estado_pantalla = "juego"
        pantalla.fill((0,0,0))
        pantalla_juego(pantalla)
    elif coordenadas_puntaje.collidepoint(posicion_mouse):
        estado_pantalla = "puntaje"
    elif coordenadas_salir.collidepoint(posicion_mouse):
        estado_pantalla = "salir"

    return estado_pantalla