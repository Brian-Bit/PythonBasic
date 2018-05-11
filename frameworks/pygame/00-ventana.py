#Import del paquete
import pygame
import sys

#Inicializamos pygame
pygame.init()

#Establecemos el tamaño de la ventana.
ventana = pygame.display.set_mode((700,400))
#podemos ponerle titulo a nuestra ventana, entre otras cosas,
#icono, que sea redimensionable...
pygame.display.set_caption("Titulo de ventana")

#Bucle de "Juego"
while True:
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa

    pygame.display.flip()               #Genera la ventana
