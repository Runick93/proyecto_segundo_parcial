import pygame
from Funciones.Funciones import *

# Pantallas.
def pantalla_inicio() -> str:
    """
    Funcion de la pantalla de inicio que permite seleccionar un boton para elegir a que opcion se desea ir.

    Returns:
        str: opcion seleccionada.
    """

    opcion = ""

    posicion_mouse = pygame.mouse.get_pos()

    coordenadas_boton_nivel =   pygame.Rect(139, 320, 215, 80)
    coordenadas_boton_jugar =   pygame.Rect(421, 320, 236, 80)
    coordenadas_boton_puntaje = pygame.Rect(133, 430, 215, 80)
    coordenadas_boton_salir =   pygame.Rect(450, 430, 215, 80)    

    if coordenadas_boton_nivel.collidepoint(posicion_mouse):
        opcion = "nivel"
    elif coordenadas_boton_jugar.collidepoint(posicion_mouse):
        opcion = "juego"
    elif coordenadas_boton_puntaje.collidepoint(posicion_mouse):
        opcion = "puntaje"
    elif coordenadas_boton_salir.collidepoint(posicion_mouse):
        opcion = "salir"

    return opcion



def pantalla_nivel(pantalla):
    """
    Funcion que permite seleccionar el nivel de dificultad del juego.

    Returns:
        str: opcion seleccionada.
    """
    pygame.draw.rect(pantalla, 'pink', [100, 100, 300, 300])



def pantalla_juego(pantalla, eventos, dict_juego, dict_jugador) -> str:
    """
    Funcion donde se encuentra el juego, se renderiza el tablero, los botones y el puntaje.

    Args:
        pantalla: 
        eventos: 
        dict_juego: Parametros del juego, como el tablero con las naves y las coordenadas de cada nave.
        dict_jugador: Parametros del jugador, como coordenadas acertadas, no acertadas y puntaje
    """
    retorno = "juego"

    renderizar_tablero(pantalla)

    fuente_botones = pygame.font.SysFont("consolas", 20)

    coordenadas_boton_atras = pygame.Rect(10, 10, 100, 50)
    pygame.draw.rect(pantalla, 'yellow', coordenadas_boton_atras)
    texto_atras = fuente_botones.render("Atras", True, (0, 0, 0)) 
    rect_texto_atras = texto_atras.get_rect(center=coordenadas_boton_atras.center)
    pantalla.blit(texto_atras, rect_texto_atras)
    
    coordenadas_boton_reiniciar = pygame.Rect(130, 10, 100, 50)
    pygame.draw.rect(pantalla, 'pink', coordenadas_boton_reiniciar)
    texto_reiniciar = fuente_botones.render("Reiniciar", True, (0, 0, 0))
    rect_texto_reiniciar = texto_reiniciar.get_rect(center=coordenadas_boton_reiniciar.center)
    pantalla.blit(texto_reiniciar, rect_texto_reiniciar)

    fuente_puntaje = pygame.font.SysFont("Consolas", 32)
    texto_surface = fuente_puntaje.render(f"PUNTAJE: {dict_jugador['puntaje']}", False, (255, 255, 255))
    pantalla.blit(texto_surface, (500, 10))
    
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
    """
    Funcion que permite ver el historico de puntajes en el juego.
    """
    fondo_imagen = pygame.image.load("Imagenes/pantalla_puntajes.jpg")
    pantalla.blit(fondo_imagen, [0,0])


# Renderizado de objetos.

def renderizar_tablero(pantalla):
    """
    Funcion donde se renderiza el tablero.
    """
    CANT_X = 10
    CANT_Y = 10
    ANCHO_IMAGEN_AGUA = 30
    ALTO_IMAGEN_AGUA = 30
    MARGEN_ROTULO_SUP = 40
    MARGEN_ROTULO_IZQ = 40
    COLOR_CONTORNO = (0, 0, 0)    # NEGRO
    COLOR_FONDO = (0, 0, 0)       # NEGRO
    COLOR_TEXTO = (255, 255, 255) # BLANCO
    GROSOR_CONTORNO = 2
    IMAGEN_AGUA = "imagenes/agua_tablero.png"

    ANCHO_PANTALLA, ALTO_PANTALLA = pantalla.get_size()

    # Calcular tamaño del tablero
    ANCHO_GRILLA = CANT_X * ANCHO_IMAGEN_AGUA
    ALTO_GRILLA = CANT_Y * ALTO_IMAGEN_AGUA

    # Calcular offsets para centrar la grilla
    offset_x = (ANCHO_PANTALLA - ANCHO_GRILLA) // 2
    offset_y = (ALTO_PANTALLA - ALTO_GRILLA) // 2

    fuente = pygame.font.SysFont("Consolas", 20)

    # Cargar y escalar imagen
    imagen = pygame.image.load(IMAGEN_AGUA)
    imagen_reescalada = pygame.transform.scale(imagen, (ANCHO_IMAGEN_AGUA, ALTO_IMAGEN_AGUA))

    # Contorno
    contorno = pygame.Surface((ANCHO_IMAGEN_AGUA, ALTO_IMAGEN_AGUA), pygame.SRCALPHA)
    pygame.draw.rect(contorno, COLOR_CONTORNO, pygame.Rect(0, 0, ANCHO_IMAGEN_AGUA, ALTO_IMAGEN_AGUA), width=GROSOR_CONTORNO)

    pantalla.fill(COLOR_FONDO)

    # Rótulo superior (numeros)
    for j in range(CANT_X):
        texto = fuente.render(str(j + 1), False, COLOR_TEXTO)
        x = offset_x + j * ANCHO_IMAGEN_AGUA + ANCHO_IMAGEN_AGUA // 2 - texto.get_width() // 2
        y = offset_y - MARGEN_ROTULO_SUP // 2 - texto.get_height() // 2
        pantalla.blit(texto, (x, y))

    # Rótulo lateral (letrsa)
    for i in range(CANT_Y):
        letra = chr(ord('A') + i)
        texto = fuente.render(letra, False, COLOR_TEXTO)
        x = offset_x - MARGEN_ROTULO_IZQ // 2 - texto.get_width() // 2
        y = offset_y + i * ALTO_IMAGEN_AGUA + ALTO_IMAGEN_AGUA // 2 - texto.get_height() // 2
        pantalla.blit(texto, (x, y))

    # Dibujar casillas
    for i in range(CANT_Y):
        for j in range(CANT_X):
            x = offset_x + j * ANCHO_IMAGEN_AGUA
            y = offset_y + i * ALTO_IMAGEN_AGUA
            pantalla.blit(imagen_reescalada, (x, y))
            pantalla.blit(contorno, (x, y))     


def buscar_barco(tablero:list, coordenadas:list) -> bool:    
    retorno = False

    fila = coordenadas[0]
    col = coordenadas[1]
    if tablero[fila][col] == 1:
        retorno = True

    return retorno