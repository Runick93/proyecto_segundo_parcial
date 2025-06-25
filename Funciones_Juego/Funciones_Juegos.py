import pygame
from Funciones.Funciones import *

import pygame.mixer as mixer
import json
import os

mixer.init()



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

    elif coordenadas_boton_puntaje.collidepoint(posicion_mouse):
        opcion = "puntaje"
    elif coordenadas_boton_salir.collidepoint(posicion_mouse):
        opcion = "salir"
    elif coordenadas_boton_jugar.collidepoint(posicion_mouse):
        opcion = "juego"

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

    imagen_cruz_roja = pygame.image.load("Imagenes/cruz_roja.png")
    imagen_cruz_roja_reescalada = pygame.transform.scale(imagen_cruz_roja, (30, 30))

    imagen_cruz_negra = pygame.image.load("Imagenes/cruz_negra.png")
    imagen_cruz_negra_reescalada = pygame.transform.scale(imagen_cruz_negra, (30, 30))

    sonido_disparo_acertado = mixer.Sound("Sonidos/sonido_acertado.wav")
    sonido_disparo_fallido = mixer.Sound("Sonidos/sonido_no_acertado.wav")

    sonido_disparo_acertado.set_volume(0.2)
    sonido_disparo_fallido.set_volume(0.2)


    renderizar_tablero(pantalla)
    # renderizar_botones(pantalla)
    # renderizar_puntaje(pantalla)
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

    
    tablero = dict_juego["tablero"]

    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            x = 250 + j * 32
            y = 150 + i * 32
            rect = pygame.Rect(x, y, 30, 30)

            if (i, j) in dict_jugador["selection"]:
                if tablero[i][j] == 1:
                    pantalla.blit(imagen_cruz_roja_reescalada, (x, y))
                else:

                    pantalla.blit(imagen_cruz_negra_reescalada, (x, y))


    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            
            if coordenadas_boton_atras.collidepoint(posicion_mouse):
                retorno = "inicio"
            
            if coordenadas_boton_reiniciar.collidepoint(posicion_mouse):
                retorno = "reiniciar"
            
            for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    x = 250 + j * 32
                    y = 150 + i * 32
                    rect = pygame.Rect(x, y, 30, 30)

                    if rect.collidepoint(posicion_mouse):
                        print(f"clic en la casilla fila {i} columna {j}")
                        se_clickeo = False

                        for numero_de_casilla in range(len(dict_jugador["selection"])):
                            seleccion_usuario = dict_jugador["selection"][numero_de_casilla]
                            if seleccion_usuario[0] == i and seleccion_usuario[1] == j:
                                se_clickeo = True
                    
                        if se_clickeo == False:
                            dict_jugador["selection"].append((i,j))
                            if tablero[i][j] == 1:
                                sonido_disparo_acertado.play()
                                dict_jugador["disparos_acertados"].append([i,j])
                                dict_jugador["puntaje"] += 5
                                verificar_destruccion(dict_juego, dict_jugador)
                            else: 
                                sonido_disparo_fallido.play()
                                dict_jugador["disparos_no_acertados"].append((i,j))
                                dict_jugador["puntaje"] -= 1
    
    partida_finalizada = partida_terminada(dict_jugador)
    if partida_finalizada == True:
        guardar_puntaje(dict_jugador)
        retorno = "reiniciar"
    #print(dict_jugador["puntaje"])
    texto_surface = fuente_puntaje.render(f"PUNTAJE: {dict_jugador['puntaje']}", False, (255, 255, 255))
    pantalla.blit(texto_surface, (500, 10))
    return retorno



def pantalla_puntaje(pantalla, diccionario_juego:dict, diccionario_jugador:dict):
    """
    Funcion que permite ver el historico de puntajes en el juego.
    """
    fondo_imagen = pygame.image.load("Imagenes/pantalla_puntajes.jpg")
    pantalla.blit(fondo_imagen, [0,0])
    #buscar_barco(diccionario_juego, diccionario_jugador)



# Renderizado de objetos.

def renderizar_tablero(pantalla):
    """
    Funcion donde se renderiza el tablero.
    """
    CANT_FILAS = 10
    CANT_COLUMNAS = 10
    ANCHO_IMAGEN_AGUA = 30
    ALTO_IMAGEN_AGUA = 30
    MARGEN_ROTULO_SUP = 40
    MARGEN_ROTULO_IZQ = 40
    COLOR_CONTORNO = (0, 0, 0)    # NEGRO
    COLOR_FONDO = (0, 0, 0)       # NEGRO
    COLOR_TEXTO = (255, 255, 255) # BLANCO
    GROSOR_CONTORNO = 2
    IMAGEN_AGUA = "Imagenes/agua_tablero.png"

    ANCHO_PANTALLA, ALTO_PANTALLA = pantalla.get_size()

    # Calcular tamaño del tablero
    ANCHO_GRILLA = CANT_FILAS * ANCHO_IMAGEN_AGUA
    ALTO_GRILLA = CANT_COLUMNAS * ALTO_IMAGEN_AGUA

    # Calcular offsets para centrar la grilla
    offset_x = (ANCHO_PANTALLA - ANCHO_GRILLA) // 2
    offset_y = (ALTO_PANTALLA - ALTO_GRILLA) // 2

    fuente = pygame.font.SysFont("Consolas", 20)

    # Cargar y escalar imagen
    imagen = pygame.image.load(IMAGEN_AGUA)
    imagen_reescalada = pygame.transform.scale(imagen, (ANCHO_IMAGEN_AGUA, ALTO_IMAGEN_AGUA))

    # Contorno
    #contorno = pygame.Surface((ANCHO_IMAGEN_AGUA, ALTO_IMAGEN_AGUA), pygame.SRCALPHA)
    #pygame.draw.rect(contorno, COLOR_CONTORNO, pygame.Rect(0, 0, ANCHO_IMAGEN_AGUA, ALTO_IMAGEN_AGUA), width=GROSOR_CONTORNO)

    pantalla.fill(COLOR_FONDO)

    # Rótulo superior (numeros)
    for j in range(CANT_FILAS):
        texto = fuente.render(str(j + 1), False, COLOR_TEXTO)
        x = offset_x + j * 32 + 32 // 2 - texto.get_width() // 2
        y = offset_y - MARGEN_ROTULO_SUP // 2 - texto.get_height() // 2
        pantalla.blit(texto, (x, y))

    # Rótulo lateral (letras)
    for i in range(CANT_COLUMNAS):
        letra = chr(ord('A') + i)
        texto = fuente.render(letra, False, COLOR_TEXTO)
        x = offset_x - MARGEN_ROTULO_IZQ // 2 - texto.get_width() // 2
        y = offset_y + i * 32 + 32 // 2 - texto.get_height() // 2
        pantalla.blit(texto, (x, y))

    # Dibujar casillas
    for i in range(CANT_COLUMNAS):
        for j in range(CANT_FILAS):
            x = offset_x + j * 32
            y = offset_y + i * 32
            pantalla.blit(imagen_reescalada, (x, y))
            #pantalla.blit(contorno, (x, y))     




# def buscar_barco(diccionario_juego:dict, diccionario_jugador:dict) -> bool: 
#     submarinos = diccionario_juego["submarinos"]
#     destructores = diccionario_juego["destructores"]
#     cruceros = diccionario_juego["cruceros"]
#     acorazados = diccionario_juego["acorazados"]   

#     disparos_acertados = diccionario_jugador["disparos_acertados"]
#     disparos_no_acertados = diccionario_jugador["disparos_no_acertados"]



#     print("en proceso")


def ingresar_nombre_usuario(pantalla, eventos, dict_jugador: dict, nombre_usuario) -> None:
    """
    Funcion que permite ingresar nombre de usuario
    """
    pantalla_nombre_usuario = pygame.image.load("Imagenes/pantalla_ingresar_nombre.png")
    pantalla_nombre_usuario_reescalada = pygame.transform.scale(pantalla_nombre_usuario, (800, 600))
    pantalla.blit(pantalla_nombre_usuario_reescalada, [0,0])

    if len(nombre_usuario) > 6:
        nombre_usuario = nombre_usuario[0:6]
    
    fuente = pygame.font.SysFont("consolas", 65)
    rect = pygame.Rect(270, 270, 300, 65)
    
    boton_continuar = pygame.Rect(235, 395, 325, 100)

    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                nombre_usuario = nombre_usuario[0:-1]
            else:
                nombre_usuario += evento.unicode
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            if boton_continuar.collidepoint(posicion_mouse) and len(nombre_usuario) > 0:
                dict_jugador["nombre_insertado"] = True
    dict_jugador["nombre_usuario"] = nombre_usuario

    texto_superficie = fuente.render(nombre_usuario, True, (255,255,255))

    pantalla.blit(texto_superficie, rect)

    return nombre_usuario

def verificar_destruccion(dict_juego, dict_jugador):
    tipos_nave = ["submarinos", "destructores", "cruceros", "acorazados"]
    disparos = dict_jugador["disparos_acertados"]

    for tipo in tipos_nave:
        naves = dict_juego[tipo]
        naves_a_eliminar = []

        for nave in naves:
            fue_destruida = True

            for parte in nave:
                fue_acertada = False
                
                for disparo in disparos:
                    if disparo[0] == parte[0] and disparo[1] == parte[1]:
                        fue_acertada = True
                        break

                if fue_acertada == False:
                    fue_destruida = False
                    break

            if fue_destruida == True:
                dict_jugador["puntaje"] += 10 * len(nave)
                print("nave destruida", tipo, nave)
                naves_a_eliminar.append(nave)
                dict_jugador["naves_destruidas"] += 1

        for nave in naves_a_eliminar:
            naves.remove(nave)
        
def partida_terminada(dict_jugador):
    naves_destruidas = dict_jugador["naves_destruidas"]
    
    retorno = False

    if naves_destruidas == 10:
        retorno = True

    return retorno

def guardar_puntaje(dict_jugador):
    nombre_usuario = dict_jugador["nombre_usuario"]
    puntaje = dict_jugador["puntaje"]
    
    ruta = "Jugadores/puntajes_jugadores.json"

    if os.path.exists(ruta):
        with open(ruta, "r") as f:
            puntajes = json.load(f)
    else:
        puntajes = []

    puntajes.append({"nombre": nombre_usuario, "puntaje": puntaje})

    with open(ruta, "w") as f:
        json.dump(puntajes, f, indent=4)