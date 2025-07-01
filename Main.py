import pygame
import pygame.mixer as mixer
from Funciones_Juego.Funciones_Juegos import * 

dict_juego = inicializar_juego()
dict_jugador = inicializar_jugador()
dict_aplicacion = inicializar_aplicacion()

pygame.init()
mixer.init()

pantalla = pygame.display.set_mode((800,600))

pygame.display.set_caption("Batalla Naval")
imagen = pygame.image.load("Imagenes/icono_juego.jpg")
pygame.display.set_icon(imagen)

mixer.music.load(dict_aplicacion["musica_fondo_path"])
mixer.music.set_volume(0.1)
mixer.music.play(loops=-1)

menu_inicio = "inicio"
nombre_usuario = dict_jugador["nombre_usuario"]


while True:
    eventos = pygame.event.get()
    for evento in eventos:
        # Evento quit. Por si se decide cerrar la ventana
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Evento mouse clic.
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if menu_inicio == "inicio":
                menu_inicio = pantalla_inicio()

    match menu_inicio:
        case "inicio":
            pantalla.blit(dict_aplicacion["imagen_fondo"], [0, 0])
            if dict_aplicacion["musica_fondo_activa"]:
                pantalla.blit(dict_aplicacion["imagen_musica_activa"], [700, 40])
            else:
                pantalla.blit(dict_aplicacion["imagen_musica_inactiva"], [700, 40])

        case "musica":
            menu_inicio = desactivar_activar_musica(eventos, dict_aplicacion)

        case "nivel":
            pantalla.fill((0, 0, 0))
            menu_inicio = pantalla_nivel(pantalla, eventos)

        case "juego":
            if not dict_jugador["nombre_insertado"]:
                nombre_usuario = ingresar_nombre_usuario(pantalla, eventos, dict_aplicacion, dict_jugador, nombre_usuario)
            else:
                menu_inicio = pantalla_juego(pantalla, eventos, dict_aplicacion, dict_juego, dict_jugador)

        case "puntaje":
            menu_inicio = pantalla_puntaje(pantalla, eventos, dict_aplicacion)

        case "salir":
            pygame.quit()
            quit()

        case "reiniciar":
            dict_juego = inicializar_juego()
            dict_jugador = inicializar_jugador()
            nombre_usuario = ""
            menu_inicio = "juego"


    pygame.display.flip()