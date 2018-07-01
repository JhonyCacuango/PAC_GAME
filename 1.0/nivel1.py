import pygame
import ladron
pygame.init()

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
    
Nivel()