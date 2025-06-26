import pygame
import pygame.mixer as mixer
from Funciones_Juego.Funciones_Juegos import * 

pygame.init()
mixer.init()

pantalla = pygame.display.set_mode((800,600))

pygame.display.set_caption("Batalla Naval")
imagen = pygame.image.load("Imagenes/icono_juego.jpg")
pygame.display.set_icon(imagen)

mixer.music.load("Sonidos/musica_fondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(loops=-1)

dict_juego = inicializar_juego()
dict_jugador = inicializar_jugador()
dict_aplicacion = inicializar_aplicacion()


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


    if menu_inicio == "inicio":
        pantalla.blit(dict_aplicacion["imagen_fondo"], [0,0])
        if dict_aplicacion["musica_fondo"] == True:
            pantalla.blit(dict_aplicacion["imagen_musica_activa"], [700,40])
        else:
            pantalla.blit(dict_aplicacion["imagen_musica_inactiva"], [700,40])
    elif menu_inicio == "musica":
        menu_inicio = desactivar_activar_musica(eventos, dict_aplicacion)
    elif menu_inicio == "nivel":
        pantalla.fill((0,0,0))
        menu_inicio = pantalla_nivel(pantalla, eventos)
    elif menu_inicio == "juego": 
        if dict_jugador["nombre_insertado"] == False:
            nombre_usuario = ingresar_nombre_usuario(pantalla, eventos, dict_jugador, nombre_usuario)
        else:
            menu_inicio = pantalla_juego(pantalla, eventos, dict_juego, dict_jugador)
    elif menu_inicio == "puntaje":
        menu_inicio = pantalla_puntaje(pantalla, eventos)
    elif menu_inicio == "salir":
        pygame.quit()
        quit()
    elif menu_inicio == "reiniciar":
        dict_juego = inicializar_juego()
        dict_jugador = inicializar_jugador()
        nombre_usuario = ""
        menu_inicio = "juego"

    pygame.display.flip()