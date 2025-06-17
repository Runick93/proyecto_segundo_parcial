import pygame
from Funciones.Funciones import *

#cruz_roja_imagen = pygame.image.load("Imagenes/cruz_roja.jpg")
#cruz_negra_imagen = pygame.image.load("Imagenes/cruz_negra.jpg")

def seleccionar_botones_inicio() -> str:
    estado_pantalla = ""

    posicion_mouse = pygame.mouse.get_pos()

    coordenadas_boton_nivel = pygame.Rect(139, 320, 215, 80)
    coordenadas_boton_jugar = pygame.Rect(421, 320, 236, 80)
    coordenadas_boton_puntaje = pygame.Rect(133, 430, 215, 80)
    coordenadas_boton_salir = pygame.Rect(450, 430, 215, 80)    

    if coordenadas_boton_nivel.collidepoint(posicion_mouse):
        estado_pantalla = "nivel"
    elif coordenadas_boton_jugar.collidepoint(posicion_mouse):
        estado_pantalla = "juego"
    elif coordenadas_boton_puntaje.collidepoint(posicion_mouse):
        estado_pantalla = "puntaje"
    elif coordenadas_boton_salir.collidepoint(posicion_mouse):
        estado_pantalla = "salir"

    return estado_pantalla

def pantalla_nivel(pantalla):
    pygame.draw.rect(pantalla, 'pink', [100, 100, 300, 300])

def pantalla_juego(pantalla, eventos, dict_juego, dict_jugador) -> str:
    retorno = "juego"

    renderizar_tablero(pantalla)

    coordenadas_boton_atras = pygame.Rect(0, 0, 50, 50)
    pygame.draw.rect(pantalla, 'yellow', [0, 0, 50, 50])

    coordenadas_boton_reiniciar = pygame.Rect(60, 0, 50, 50)
    pygame.draw.rect(pantalla, 'pink', [60, 0, 50, 50])
    
    coordenadas_casillas = pygame.Rect(250, 150, 30 * 10, 30 * 10)
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            
            if coordenadas_boton_atras.collidepoint(posicion_mouse):
                retorno = "inicio"
            
            if coordenadas_boton_reiniciar.collidepoint(posicion_mouse):
                retorno = "reiniciar"
            
            if coordenadas_casillas.collidepoint(posicion_mouse):
                mouse_x, mouse_y = posicion_mouse

                # Coordenadas relativas dentro del tablero
                rel_x = mouse_x - coordenadas_casillas.x
                rel_y = mouse_y - coordenadas_casillas.y

                # Para buscar en la matriz                
                fila = rel_y // 30
                columna = rel_x // 30
                posicion_matriz = (fila, columna)

                # pra dibujar las cruces en la pantalla
                posicion_tablero = (coordenadas_casillas.x, coordenadas_casillas.y)

                hay_barco = buscar_barco(dict_juego["tablero"],[fila, columna])
                if hay_barco:
                    dict_jugador["disparos_acertados"].append(posicion_matriz)
                    print("Acerto al barco")
                else:
                    dict_jugador["disparos_no_acertados"].append(posicion_matriz)
                    print("No acerto al barco")
        
                # Aca funcion para dibujar las cruces

                # Debug
                print("Aciertos:", dict_jugador["disparos_acertados"])
                print("No Aciertos:", dict_jugador["disparos_no_acertados"])

    return retorno

def pantalla_puntaje(pantalla):
    fondo_imagen = pygame.image.load("Imagenes/pantalla_puntajes.jpg")
    pantalla.blit(fondo_imagen, [0,0])



def renderizar_tablero(pantalla):
    # Constantes
    CANT_X = 10
    CANT_Y = 10
    ANCHO_IMAGEN = 30
    ALTO_IMAGEN = 30
    MARGEN_ROTULO_SUP = 40
    MARGEN_ROTULO_IZQ = 40
    COLOR_CONTORNO = (0, 0, 0)
    COLOR_FONDO = (30, 30, 30)
    COLOR_TEXTO = (255, 255, 255)
    GROSOR_CONTORNO = 2
    AGUA_IMAGEN = "imagenes/agua_tablero.png"

    # Obtener tamaño ventana
    ANCHO_PANTALLA, ALTO_PANTALLA = pantalla.get_size()

    # Calcular tamaño total del tablero
    GRILLA_ANCHO = CANT_X * ANCHO_IMAGEN
    GRILLA_ALTO = CANT_Y * ALTO_IMAGEN

    # Calcular offsets para centrar la grilla
    offset_x = (ANCHO_PANTALLA - GRILLA_ANCHO) // 2
    offset_y = (ALTO_PANTALLA - GRILLA_ALTO) // 2

    # Fuente
    fuente = pygame.font.SysFont("Arial", 20)

    # Cargar y escalar imagen
    imagen = pygame.image.load(AGUA_IMAGEN).convert_alpha()
    imagen_reescalada = pygame.transform.scale(imagen, (ANCHO_IMAGEN, ALTO_IMAGEN))

    # Contorno
    contorno = pygame.Surface((ANCHO_IMAGEN, ALTO_IMAGEN), pygame.SRCALPHA)
    pygame.draw.rect(contorno, COLOR_CONTORNO, pygame.Rect(0, 0, ANCHO_IMAGEN, ALTO_IMAGEN), width=GROSOR_CONTORNO)

    pantalla.fill(COLOR_FONDO)

    # Rótulo superior (numeros)
    for j in range(CANT_X):
        texto = fuente.render(str(j + 1), True, COLOR_TEXTO)
        x = offset_x + j * ANCHO_IMAGEN + ANCHO_IMAGEN // 2 - texto.get_width() // 2
        y = offset_y - MARGEN_ROTULO_SUP // 2 - texto.get_height() // 2
        pantalla.blit(texto, (x, y))

    # Rótulo lateral (letrsa)
    for i in range(CANT_Y):
        letra = chr(ord('A') + i)
        texto = fuente.render(letra, True, COLOR_TEXTO)
        x = offset_x - MARGEN_ROTULO_IZQ // 2 - texto.get_width() // 2
        y = offset_y + i * ALTO_IMAGEN + ALTO_IMAGEN // 2 - texto.get_height() // 2
        pantalla.blit(texto, (x, y))

    # Dibujar casillas
    for i in range(CANT_Y):
        for j in range(CANT_X):
            x = offset_x + j * ANCHO_IMAGEN
            y = offset_y + i * ALTO_IMAGEN
            pantalla.blit(imagen_reescalada, (x, y))
            pantalla.blit(contorno, (x, y))     


def buscar_barco(tablero:list, coordenadas:list) -> bool:    
    retorno = False

    fila = coordenadas[0]
    col = coordenadas[1]
    if tablero[fila][col] == 1:
        retorno = True

    return retorno