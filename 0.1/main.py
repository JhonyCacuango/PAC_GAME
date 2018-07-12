# -*- coding: utf-8 -*-

import pygame
import ladron
import moneda
import random
from pygame.locals import *


pygame.init()

#clase para policia

class Policia(pygame.sprite.Sprite):                          #hereda metodos de clase pygame.sprite.Sprite que nos permite usarlos para el manejo de sprites
    def __init__(self, x, y):                                  #inicializa la clase y recibe parametros para posicion en ancho y alto
        pygame.sprite.Sprite.__init__(self)                   #invoca metodo init de la clase heredada
        self.image = load_image("policia.png", True)          #cargar imagen y el verdadero de transparencia
        self.rect = self.image.get_rect()                     #la función self.image.get_rect() obtiene un rectangulo con las dimensiones y posición de la imagen 
        self.rect.centerx = x                          #situa en centro del ancho de la ventana
        self.rect.centery = y                                 #situa en centro del alto de la ventana
        self.speed = [0.3, -0.3]                              #velocidad de movimiento con respecto a los ejes

    def actualizar(self, time):                   #define el método y parametros del tiempo transcurrido
        Ancho = 1280 
        Alto = 720
        self.rect.centerx += self.speed[0] * time             #fisica e=v*t pos en X (velocidad en el tiempo) y (tiempo transcurrido)
        self.rect.centery += self.speed[1] * time             #fisica e=v*t pos en Y
        if self.rect.left <= 0 or self.rect.right >= Ancho:   #parte izquierda del objeto a moverse no sea menor a 0 con respecto al rectangulo de la ventana externa
            self.speed[0] = -self.speed[0]                    #y parte derecha no mayor a ancho para evitar que el objeto se salga de pantalla en el eje X
            self.rect.centerx += self.speed[0] * time         
        if self.rect.top <= 0 or self.rect.bottom >= Alto:
            self.speed[1] = -self.speed[1]                    #lo mismo pero con el eje Y
            self.rect.centery += self.speed[1] * time
#cargar imagenes
def load_image(fondo1, transparent=False):            #recibe parametros: 1)nombre/ruta 2)Si tiene parte transparente
        try: image = pygame.image.load(fondo1)        #asignacion de imagen a una variable
        except pygame.error. message:                       #maneja errores por si no existe imagen
                raise SystemExit. message
        image = image.convert()                             #convierte la imagen al tipo interno de pygame
        if transparent:                                     #condicion por si la imagen tiene transparencia
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image                                        #retorna imagen

    
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
    
    ancho_ventana = 1280
    alto_ventana = 720
    screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("SAMMLER")
    nivel1=pygame.image.load("nivel.jpg")
    x=30
    y=30
    player = ladron.Ladron((0, 0))
    coin = moneda.Moneda(x,y)
    
    
    cantidad=-1
    fuente1=pygame.font.SysFont("Arial",20,True,False)#crea la fuente

    policia = Policia((random.randrange(100, 1280, 5)),(random.randrange(100, 720, 5)))      #crear policia y colocar los parametros de posicion
    policia1 = Policia((random.randrange(100, 1280, 5)),(random.randrange(100, 720, 5))) 
    policia2 = Policia((random.randrange(100, 1280, 5)),(random.randrange(100, 720, 5)))
    policia3 = Policia((random.randrange(100, 1280, 5)),(random.randrange(100, 720, 5)))
    policia4 = Policia((random.randrange(100, 1280, 5)),(random.randrange(100, 720, 5)))
    policia5 = Policia((random.randrange(100, 1280, 5)),(random.randrange(100, 720, 5)))
    
    clock = pygame.time.Clock()
    game_over = False
    
    while game_over == False:
        
        
        tiempo=pygame.time.get_ticks()/1000
        time = clock.tick(60)                               #(fotogramas por seg)framerate de 60 para que funcione de las misma manera en todo ordenador
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if player.rect.colliderect(coin.rect):
                pygame.mixer.music.load('sonidomoneda.mp3')
                pygame.mixer.music.play()
                x=random.randrange(10,1250)
                y=random.randrange(10,700)
                coin = moneda.Moneda(x,y)
                cantidad+=1
            
                
            if player.rect.colliderect(policia.rect):
                print("Final del juego")
                #game_over = True
            if player.rect.colliderect(policia1.rect):
                print("Final del juego")
                #game_over = True
            if player.rect.colliderect(policia2.rect):
                print("Final del juego")
                #game_over = True
            if player.rect.colliderect(policia3.rect):
                print("Final del juego")
                #game_over = True
            if player.rect.colliderect(policia4.rect):
                print("Final del juego")
                #game_over = True
            if player.rect.colliderect(policia5.rect):
                print("Final del juego")
                #game_over = True

                
        policia.actualizar(time)                 #actualizaciones de el policia con respecto al tiempo transcurrido
        policia1.actualizar(time)
        policia2.actualizar(time)
        policia3.actualizar(time)
        policia4.actualizar(time)
        policia5.actualizar(time)
        
        
        screen.blit(nivel1,(0,0))

        
        screen.blit(policia.image, policia.rect)            #ubicar la imagen policia en ventana y pasar el rect para que se vaya moviendo y no sea estatico como en el fondo que se pasa coordenadas
        screen.blit(policia1.image, policia1.rect)
        screen.blit(policia2.image, policia2.rect)
        screen.blit(policia3.image, policia3.rect)
        screen.blit(policia4.image, policia4.rect)
        screen.blit(policia5.image, policia5.rect)
        
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
    
        
        clock.tick(10)
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

