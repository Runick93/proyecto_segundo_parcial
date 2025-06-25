import pygame
import pygame.mixer as mixer
from Funciones_Juego.Funciones_Juegos import * 

pygame.init()
mixer.init()

pantalla = pygame.display.set_mode((800,600))
fondo_imagen = pygame.image.load("Imagenes/imagen_menu.jpg")

pygame.display.set_caption("Batalla Naval")
imagen = pygame.image.load("Imagenes/icono_juego.jpg")
pygame.display.set_icon(imagen)

# mixer.music.load("Sonidos/musica_fondo.mp3")
# mixer.music.set_volume(0.4)
# mixer.music.play(loops=-1)

dict_juego = inicializar_juego()
dict_jugador = inicializar_jugador()


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
        pantalla.blit(fondo_imagen, [0,0])
    elif menu_inicio == "nivel":
        pantalla.fill((0,0,0))
        menu_inicio = pantalla_nivel(pantalla)
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