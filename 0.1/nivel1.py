import pygame
import ladron
import moneda
import random
pygame.init()

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
    segundosint=0
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
        
        if game_over==False:
            segundosint= pygame.time.get_ticks()/1000 #toma el tiempo que se esta ejecutando el juego
            segundos=str(segundosint)#los combierte de numero a string
            transcurre=fuente1.render(segundos,0,pygame.Color('orange'))#pone el tiempo en un texto
        else:
            transcurre=fuente1.render(segundos,0,pygame.Color('orange'))
        
        screen.blit(transcurre,(600,5))
        screen.blit(contador,(450,5))  
        pygame.display.update()
        
        
    pygame.quit ()
    
Nivel()