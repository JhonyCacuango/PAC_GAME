# -*- coding: utf-8 -*-

import pygame
import ladron
import moneda
import random


pygame.init()

#creamos un cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)#definimos el  rectangulo
    def update(self):# mover el rectangulo invisible segue el mouse
        self.left,self.top=pygame.mouse.get_pos()# mover el rectangulo invisible segue el mouse


# Definimos algunas variables que usaremos en nuestro código
#clase boton para crear la animacion 
class Boton(pygame.sprite.Sprite):
    
    def __init__(self,imagen1,imagen2,x=0,y=0):#recibe estos parametros 
        self.imagen_normal=imagen1 # define los parametros recibidos  crea la primera imagen del boton
        self.imagen_seleccion=imagen2# crea la segunda imagen del boton 
        self.imagen_actual=self.imagen_normal # crea una tercera imagen la que essta normalmente
        self.rect=self.imagen_actual.get_rect()# define las dimenciones del rectangulo del boton 
        self.rect.left=x #posicion en x del rectangulo
        self.rect.top=y

    def update(self,pantalla,cursor):# actualizacion de la imagen  recibe la posicion del cursor
        if cursor.colliderect(self.rect):# si la posicion del cursor coliciona con  la del rectangulo de l boton 
            self.imagen_actual=self.imagen_seleccion # carga la segunda imagen 
            
        else:
            self.imagen_actual=self.imagen_normal# carga la imagen normal 

        pantalla.blit(self.imagen_actual,self.rect)#dibuja en pantalla el boton 
    
  # definir  funcion nivel   
def Nivel():
    ancho_ventana = 740
    alto_ventana = 480
    screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("SAMMLER")
    nivel1=pygame.image.load("nivel.jpg")
    x=20
    y=20
    player = ladron.Ladron((ancho_ventana/2, alto_ventana/2))
    coin = moneda.Moneda(x,y)
    cantidad=0
    fuente1=pygame.font.SysFont("Arial",20,True,False)#crea la fuente
    
    clock = pygame.time.Clock()
    game_over = False

    while game_over == False:
        tiempo=pygame.time.get_ticks()/1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if player.rect.colliderect(coin.rect):
                
                x=random.randrange(10,600)
                y=random.randrange(10,400)
                coin = moneda.Moneda(x,y)
                cantidad+=1
            
        clock.tick(20)
        screen.blit(nivel1,(0,0))
        
        
        player.handle_event(event)
        screen.blit(player.image, player.rect)
        coin.dibujar(screen)  
        coin.animacion(tiempo)  
        total=str(cantidad)
        contador=fuente1.render("MONEDAS "+ str(total),0,pygame.Color('orange'))
        screen.blit(contador,(450,5))  
        pygame.display.update()
        
    pygame.quit ()
#funcion principal 
def main():
    
    pygame.mixer.init()
    ancho_ventana = 740
    alto_ventana = 480
    screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("SAMMLER")# pone nombre a la ventana
    
    fondo=pygame.image.load("fondoini.png")
    
    # carga el archivo de audio
    pygame.mixer.music.load('musica.mp3')# cargar  un archivo de audio
    pygame.mixer.music.play(-1, 0.0)# reproduce el archivo de audio
    
    i1=pygame.image.load("welcome.png")
    i2=pygame.image.load("samm.png")
    clock = pygame.time.Clock()
    # cargar las imagenes de los botones la normal y la del momento de pasar el boton 
    salir=pygame.image.load("salir.png")
    salir2=pygame.image.load("saliro.png")
    
    jugarini=pygame.image.load("jugar.png")
    jugar=pygame.image.load("jugaro.png")
    
    scoreini=pygame.image.load("score.png")
    score=pygame.image.load("scoreo.png")
    # crear los botones y pasarles como parametro las imagenes de los dos estados 
    boton1=Boton(salir,salir2,100,100)
    boton2=Boton(jugarini,jugar,100,200)
    boton3=Boton(scoreini,score,100,300)
    # crea el cursor 
    cursor1=Cursor()
    
   
    game_over = False

    while game_over == False:

        for event in pygame.event.get():
            # si el evento es clic del mouse
            if event.type==pygame.MOUSEBUTTONDOWN:
                #si el mouse esta sobre el boton 
                if cursor1.colliderect(boton1.rect):#boton salir
                    game_over=True
                if cursor1.colliderect(boton2.rect):# boton jugar 
                    pygame.mixer.music.stop()# para el audio
                    Nivel()#carga la funcion nivel
                    
            
            if event.type == pygame.QUIT:
                game_over = True

    #player.handle_event(event)
    
        
        clock.tick(20)
        #sonido1.play()
        screen.blit(fondo,(0,0)) #carga el fondo en pantalla 
        screen.blit(i1,(250,100))
        screen.blit(i2,(290,200))
        cursor1.update()# actualiza la posicion del cursor 
        boton1.update(screen,cursor1)# coloca el boton en pantalla 
        boton2.update(screen, cursor1)# coloca el boton en pantalla
        boton3.update(screen, cursor1)

        pygame.display.update()
        
    pygame.quit ()
main()

