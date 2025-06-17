import pygame

fondo_imagen = pygame.image.load("proyecto_segundo_parcial/Imagenes/imagen_fondo_pantallas.jpg")

seleccion = set() #{}


def pantalla_nivel(pantalla):
    pantalla.blit(fondo_imagen, [0,0])
    pygame.draw.rect(pantalla, 'pink', [100,100,300,300])

def pantalla_juego(pantalla,eventos, tablero):

    fondo_agua = pygame.image.load("proyecto_segundo_parcial/Imagenes/agua_2.png")
    imagen_reescalada = pygame.transform.scale(fondo_agua, (40, 40))
    contador = 0

    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            x = 170 + j * 45
            y = 80 + i * 45
            pantalla.blit(imagen_reescalada, [x,y])

            if (i, j) in seleccion:
                if tablero[i][j] == 1:
                    pygame.draw.rect(pantalla, 'pink', [x, y, 40, 40])
                else:
                    pygame.draw.rect(pantalla, 'blue', [x, y, 40, 40])

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    x = 170 + j * 45
                    y = 80 + i * 45
                    rect2 = pygame.Rect(x, y, 40, 40)
                    
                    if rect2.collidepoint(posicion_mouse):
                        print(f"Clic en casilla fila {i} columna {j}")
                        print(tablero)
                        seleccion.add((i, j))
                            

def pantalla_puntaje(pantalla):
    fondo_imagen = pygame.image.load("proyecto_segundo_parcial/Imagenes/pantalla_puntajes.jpg")
    pantalla.blit(fondo_imagen, [0,0])

def seleccionar_botones(pantalla, eventos,tablero):
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
        pantalla_juego(pantalla,eventos,tablero)
    elif coordenadas_puntaje.collidepoint(posicion_mouse):
        estado_pantalla = "puntaje"
    elif coordenadas_salir.collidepoint(posicion_mouse):
        estado_pantalla = "salir"

    return estado_pantalla