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

    Args:
        None

    Returns:
        str: opcion seleccionada.
    """

    opcion = ""

    posicion_mouse = pygame.mouse.get_pos()

    coordenadas_boton_nivel =   pygame.Rect(139, 320, 215, 80)
    coordenadas_boton_jugar =   pygame.Rect(421, 320, 236, 80)
    coordenadas_boton_puntaje = pygame.Rect(133, 430, 215, 80)
    coordenadas_boton_salir =   pygame.Rect(450, 430, 215, 80)
    coordenadas_boton_musica =  pygame.Rect(700, 40, 40, 40)

    if coordenadas_boton_nivel.collidepoint(posicion_mouse):
        opcion = "nivel"
    elif coordenadas_boton_puntaje.collidepoint(posicion_mouse):
        opcion = "puntaje"
    elif coordenadas_boton_salir.collidepoint(posicion_mouse):
        opcion = "salir"
    elif coordenadas_boton_jugar.collidepoint(posicion_mouse):
        opcion = "juego"
    elif coordenadas_boton_musica.collidepoint(posicion_mouse):
        opcion = "musica"

    return opcion



def pantalla_nivel(pantalla, eventos: list) -> str:
    """
    Funcion que permite seleccionar el nivel de dificultad del juego.

    Args:
        pantalla (pygame.Surface): Superficie de Pygame donde se renderiza el contenido, obtenida con pygame.display.set_mode()
        eventos (list): Lista de eventos de Pygame obtenidos con pygame.event.get()

    Returns:
        str: opcion seleccionada.
    """

    retorno = "nivel"
    fuente_botones = pygame.font.SysFont("consolas", 20)

    coordenadas_boton_atras = pygame.Rect(10, 10, 100, 50)
    pygame.draw.rect(pantalla, (255, 221, 0), coordenadas_boton_atras)
    texto_atras = fuente_botones.render("Atras", True, (0, 0, 0)) 
    rect_texto_atras = texto_atras.get_rect(center=coordenadas_boton_atras.center)
    pantalla.blit(texto_atras, rect_texto_atras)

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            
            if coordenadas_boton_atras.collidepoint(posicion_mouse):
                retorno = "inicio"

    return retorno



def pantalla_juego(pantalla, eventos: list, dict_aplicacion: dict, dict_juego: dict, dict_jugador: dict) -> str:
    """
    Funcion donde se encuentra el juego, se renderiza el tablero, los botones y el puntaje.

    Args:
        pantalla (pygame.Surface): Superficie de Pygame donde se renderiza el contenido, obtenida con pygame.display.set_mode()
        eventos (list): Lista de eventos de Pygame obtenidos con pygame.event.get()
        dict_aplicacion (dict): Diccionario que contiene la configuracion de la aplicacion
        dict_juego (dict): Parametros del juego, como el tablero con las naves y las coordenadas de cada nave.
        dict_jugador (dict): Parametros del jugador, como coordenadas acertadas, no acertadas y puntaje

    Returns:
        str: opcion seleccionada.
    """
    
    retorno = "juego"

    sonido_disparo_acertado = mixer.Sound(dict_aplicacion["sonido_disparo_acertado_path"])
    sonido_disparo_no_acertado =  mixer.Sound(dict_aplicacion["sonido_disparo_no_acertado_path"])

    sonido_disparo_acertado.set_volume(0.2)
    sonido_disparo_no_acertado.set_volume(0.2)


    renderizar_tablero(pantalla)
    # renderizar_botones(pantalla)
    # renderizar_puntaje(pantalla)
    fuente_botones = pygame.font.SysFont("consolas", 20)

    coordenadas_boton_atras = pygame.Rect(10, 10, 100, 50)
    pygame.draw.rect(pantalla, (255, 221, 0), coordenadas_boton_atras)
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

            if (i, j) in dict_jugador["seleccion"]:
                if tablero[i][j] == 1:
                    pantalla.blit(dict_aplicacion["imagen_disparo_acertado"], (x, y))
                else:
                    pantalla.blit(dict_aplicacion["imagen_disparo_no_acertado"], (x, y))


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

                        for numero_de_casilla in range(len(dict_jugador["seleccion"])):
                            seleccion_usuario = dict_jugador["seleccion"][numero_de_casilla]
                            if seleccion_usuario[0] == i and seleccion_usuario[1] == j:
                                se_clickeo = True
                    
                        if se_clickeo == False:
                            dict_jugador["seleccion"].append((i,j))
                            if tablero[i][j] == 1:
                                sonido_disparo_acertado.play()
                                dict_jugador["disparos_acertados"].append([i,j])
                                dict_jugador["puntaje"] += 5
                                verificar_destruccion(dict_juego, dict_jugador)
                            else: 
                                sonido_disparo_no_acertado.play()
                                dict_jugador["disparos_no_acertados"].append((i,j))
                                dict_jugador["puntaje"] -= 1
    
    partida_finalizada = partida_terminada(dict_jugador)
    if partida_finalizada == True:
        guardar_puntaje(dict_aplicacion ,dict_jugador)
        retorno = "reiniciar"
    #print(dict_jugador["puntaje"])
    texto_surface = fuente_puntaje.render(f"PUNTAJE: {dict_jugador['puntaje']}", False, (255, 255, 255))
    pantalla.blit(texto_surface, (500, 10))
    return retorno



def pantalla_puntaje(pantalla, eventos: list, dict_aplicacion: dict) -> str:
    """
    Funcion que permite ver el historico de puntajes en el juego.

    Args:
        pantalla (pygame.Surface): Superficie de Pygame donde se renderiza el contenido, obtenida con pygame.display.set_mode()
        eventos (list): Lista de eventos de Pygame obtenidos con pygame.event.get()
        dict_aplicacion (dict): Diccionario que contiene la configuracion de la aplicacion

    Returns:
        str: opcion seleccionada.
    """

    retorno = "puntaje"
    pantalla.blit(dict_aplicacion["imagen_fondo_puntajes"], [0,0])
    puntaje_jugador_archivos = obtener_mayor_puntaje(dict_aplicacion)

    fuente_puntaje = pygame.font.SysFont("Consolas", 32)

    fuente_botones = pygame.font.SysFont("consolas", 20)

    coordenadas_boton_atras = pygame.Rect(10, 10, 100, 50)
    pygame.draw.rect(pantalla, (255, 221, 0), coordenadas_boton_atras)
    texto_atras = fuente_botones.render("Atras", True, (0, 0, 0)) 
    rect_texto_atras = texto_atras.get_rect(center=coordenadas_boton_atras.center)
    pantalla.blit(texto_atras, rect_texto_atras)

    if len(puntaje_jugador_archivos) >= 1:
        texto_surface_nombre1 = fuente_puntaje.render(f"{puntaje_jugador_archivos[0]["nombre"]}", False, (255, 255, 255))
        texto_surface_puntaje1 = fuente_puntaje.render(f"{puntaje_jugador_archivos[0]["puntaje"]}", False, (255, 255, 255))
        pantalla.blit(texto_surface_nombre1, (150, 240))
        pantalla.blit(texto_surface_puntaje1, (480, 240))

    if len(puntaje_jugador_archivos) >= 2:
        texto_surface_nombre2 = fuente_puntaje.render(f"{puntaje_jugador_archivos[1]["nombre"]}", False, (255, 255, 255))
        texto_surface_puntaje2 = fuente_puntaje.render(f"{puntaje_jugador_archivos[1]["puntaje"]}", False, (255, 255, 255))
        pantalla.blit(texto_surface_nombre2, (150, 365))
        pantalla.blit(texto_surface_puntaje2, (480, 365))

    if len(puntaje_jugador_archivos) >= 3:
        texto_surface_nombre3 = fuente_puntaje.render(f"{puntaje_jugador_archivos[2]["nombre"]}", False, (255, 255, 255))
        texto_surface_puntaje3 = fuente_puntaje.render(f"{puntaje_jugador_archivos[2]["puntaje"]}", False, (255, 255, 255))
        pantalla.blit(texto_surface_nombre3, (150, 490))
        pantalla.blit(texto_surface_puntaje3, (480, 490))

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            
            if coordenadas_boton_atras.collidepoint(posicion_mouse):
                retorno = "inicio"

    return retorno


def desactivar_activar_musica(eventos: list, dict_aplicacion: dict) -> str:
    """
    Activa o desactiva la musica de fondo al detectar un clic.

    Args:
        eventos (list): Lista de eventos de Pygame obtenidos con pygame.event.get().
        dict_aplicacion (dict): Diccionario que contiene la configuracion de la aplicacion, incluyendo el estado de la musica.

    Returns:
        str: opcion seleccionada.
    """

    retorno = "inicio"
    coordenadas_boton_activar = pygame.Rect(700, 40, 40, 40)

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            if coordenadas_boton_activar.collidepoint(posicion_mouse):
                if dict_aplicacion["musica_fondo_activa"] == True:
                    mixer.music.stop()
                    dict_aplicacion["musica_fondo_activa"] = False
                else:
                  mixer.music.play(loops=-1)
                  dict_aplicacion["musica_fondo_activa"] = True

    return retorno

# Renderizado de objetos.
def renderizar_tablero(pantalla) -> None:
    """
    Funcion donde se renderiza el tablero.

    Args:
        eventos (list): Lista de eventos de Pygame obtenidos con pygame.event.get()

    Returns:
        str: opcion seleccionada.
    """

    CANT_FILAS = 10
    CANT_COLUMNAS = 10
    ANCHO_IMAGEN_AGUA = 30
    ALTO_IMAGEN_AGUA = 30
    MARGEN_ROTULO_SUP = 40
    MARGEN_ROTULO_IZQ = 40
    COLOR_FONDO = (0, 0, 0)       # NEGRO
    COLOR_TEXTO = (255, 255, 255) # BLANCO
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

def ingresar_nombre_usuario(pantalla, eventos: list, dict_aplicacion: dict, dict_jugador: dict, nombre_usuario: str) -> None:
    """
    Funcion que permite ingresar nombre de usuario

    Args:
        pantalla (pygame.Surface): Superficie de Pygame donde se renderiza el contenido, obtenida con pygame.display.set_mode()
        eventos (list): Lista de eventos de Pygame obtenidos con pygame.event.get()
        dict_aplicacion (dict): Diccionario que contiene la configuracion de la aplicacion
        dict_jugador (dict): Parametros del jugador, como coordenadas acertadas, no acertadas y puntaje
        nombre_usuario (str): Nombre del jugador ingresado o por ingresar

    Returns:
        str: Nombre del jugador ingresado.
    """
    pantalla.blit(dict_aplicacion["imagen_fondo_ingresar_nombre"], [0,0])

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

def verificar_destruccion(dict_juego: dict, dict_jugador: dict) -> None:
    """
    Funcion donde verifica si hubo destruccion de la nave, sumando 10 puntos extras por cada elemento que compone la misma. 

    Args:
        dict_juego (dict): Parametros del juego, como el tablero con las naves y las coordenadas de cada nave.
        dict_jugador (dict): Parametros del jugador, como coordenadas acertadas, no acertadas y puntaje

    Returns:
        None
    """
     
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
        
def partida_terminada(dict_jugador: dict) -> bool:
    """
    Funcion que verifica si se termino la partida en base a que todas las naves esten destruidas.

    Args:
        dict_jugador (dict): Parametros del jugador, como coordenadas acertadas, no acertadas y puntaje.

    Returns:
        bool: True o False dependiendo si se termino o no la partida.
    """

    naves_destruidas = dict_jugador["naves_destruidas"]
    
    retorno = False

    if naves_destruidas == 10:
        retorno = True

    return retorno

def guardar_puntaje(dict_aplicacion: dict, dict_jugador: dict) -> None:
    """
    Guarda el puntaje del jugador en un archivo JSON.

    Args:
        dict_aplicacion (dict): Diccionario que contiene la configuracion de la aplicacion
        dict_jugador (dict): Parametros del jugador, como coordenadas acertadas, no acertadas y puntaje.

    Returns:
        None
    """
    nombre_usuario = dict_jugador["nombre_usuario"]
    puntaje = dict_jugador["puntaje"]
    
    ruta = dict_aplicacion["archivo_puntajes_path"]

    if not os.path.exists("Jugadores"):
        os.makedirs("Jugadores")

    if os.path.exists(ruta):
        with open(ruta, "r") as f:
            puntajes = json.load(f)
    else:
        puntajes = []

    puntajes.append({"nombre": nombre_usuario, "puntaje": puntaje})

    with open(ruta, "w") as f:
        json.dump(puntajes, f, indent=4)

def ordenamiento(datos: list) -> None:
    """
    Funcion que ordena de manera ASC una matriz pasada por parametros.

    Args:
        datos (list): Una matriz que contiene los datos a ordenar

    Returns:
        La matriz pasada por parametro ordenada.
    """

    for i in range(0, len(datos)-1, 1):
        for j in range(i + 1, len(datos), 1):
            if datos[i]["puntaje"] < datos[j]["puntaje"]:
                puntaje_auxiliar = datos[i]["puntaje"]
                datos[i]["puntaje"] = datos[j]["puntaje"]
                datos[j]["puntaje"] = puntaje_auxiliar

                nombre_auxiliar = datos[i]["nombre"]
                datos[i]["nombre"] = datos[j]["nombre"]
                datos[j]["nombre"] = nombre_auxiliar

def obtener_mayor_puntaje(dict_aplicacion: dict) -> list:
    """
    Obtiene los tres mayores puntajes almacenados en el archivo JSON.

    Args:
        dict_aplicacion (dict): Diccionario que contiene la configuracion de la aplicacion

    Returns:
        list: Lista con los datos de los jugadores con mayor puntaje (hasta un maximo de tres).
    """
    ruta = dict_aplicacion["archivo_puntajes_path"]
    mayores_puntajes = []

    if os.path.exists(ruta):
        with open(ruta, "r") as archivo:
            puntaje_jugadores_archivo = json.load(archivo)
            #ordenamos los datos de mayor puntaje
            ordenamiento(puntaje_jugadores_archivo)
            rango = len(puntaje_jugadores_archivo)

            if rango > 3:
                rango = 3
                
            for i in range(rango):
                mayores_puntajes.append(puntaje_jugadores_archivo[i])

    return mayores_puntajes