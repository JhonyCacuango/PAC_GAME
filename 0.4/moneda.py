import pygame

pygame.init()
class Moneda(pygame.sprite.Sprite):
    def __init__(self, posx,posy):
        
        self.imagen1=pygame.image.load("monedaa.png")

        
        self.ImagenMoneda = self.imagen1
        self.rect=self.ImagenMoneda.get_rect()
        
        self.rect.top=posy
        self.rect.left=posx
        
    def dibujar(self,superficie):
        superficie.blit(self.ImagenMoneda,self.rect)
        
      
            
