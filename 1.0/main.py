# -*- coding: utf-8 -*-

import pygame
import ladron
import nivel1


pygame.init()

#creamos un cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)#es un rectangulo
    def update(self):# mover el rectangulo invisible segun el mouse
        self.left,self.top=pygame.mouse.get_pos()


# Definimos algunas variables que usaremos en nuestro código
class Boton(pygame.sprite.Sprite):
    
    def __init__(self,imagen1,imagen2,x=0,y=0):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left=x
        self.rect.top=y

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
            
        else:
            self.imagen_actual=self.imagen_normal

        pantalla.blit(self.imagen_actual,self.rect)
    
    
def Nivel():
    ancho_ventana = 740
    alto_ventana = 480
    screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("SAMMLER")
    nivel1=pygame.image.load("nivel.jpg")
    
    player = ladron.Ladron((ancho_ventana/2, alto_ventana/2))
    
    clock = pygame.time.Clock()
    game_over = False

    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
        clock.tick(20)
        screen.blit(nivel1,(0,0))
        player.handle_event(event)
        screen.blit(player.image, player.rect)
        pygame.display.update()
        
    pygame.quit ()

def main():
    
    pygame.mixer.init()
    ancho_ventana = 740
    alto_ventana = 480
    screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("SAMMLER")# pone nombre a la ventana
    
    fondo=pygame.image.load("fondoini.png")
    
    #sonido1=pygame.mixer.Sound('sonidofondo.wav')# carga el archivo de audio
    
    
    pygame.mixer.music.load('musica.mp3')# cargar y reproduce un archivo de audio
    pygame.mixer.music.play(-1, 0.0)
    
    i1=pygame.image.load("welcome.png")
    i2=pygame.image.load("samm.png")
    clock = pygame.time.Clock()
    
    salir=pygame.image.load("salir.png")
    salir2=pygame.image.load("saliro.png")
    
    jugarini=pygame.image.load("jugar.png")
    jugar=pygame.image.load("jugaro.png")
    
    scoreini=pygame.image.load("score.png")
    score=pygame.image.load("scoreo.png")
    
    boton1=Boton(salir,salir2,100,100)
    boton2=Boton(jugarini,jugar,100,200)
    boton3=Boton(scoreini,score,100,300)
    
    cursor1=Cursor()
    
   
    game_over = False

    while game_over == False:

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    game_over=True
                if cursor1.colliderect(boton2.rect):
                    pygame.mixer.music.stop()
                    Nivel()
                    
            
            if event.type == pygame.QUIT:
                game_over = True

    #player.handle_event(event)
    
        
        clock.tick(20)
        #sonido1.play()
        screen.blit(fondo,(0,0))
        screen.blit(i1,(250,100))
        screen.blit(i2,(290,200))
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen, cursor1)
        boton3.update(screen, cursor1)
        #screen.fill(pygame.Color('gray'))
    #screen.blit(player.image, player.rect)#pasa la imagn y el rectangulo

        pygame.display.update()
        
    pygame.quit ()
main()

