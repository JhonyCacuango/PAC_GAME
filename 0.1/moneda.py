import pygame

pygame.init()
class Moneda(pygame.sprite.Sprite):
    def __init__(self, posx,posy):
        
        self.imagen1=pygame.image.load("monedaa.png")
        self.imagen2=pygame.image.load("monedab.png")
        self.imagen3=pygame.image.load("monedac.png")
        self.imagen4=pygame.image.load("monedad.png")
        self.imagen5=pygame.image.load("monedae.png")
        
        self.listaImagenes = [self.imagen1, self.imagen2,self.imagen3,self.imagen4,self.imagen5]
        self.posImagen=0
        self.ImagenMoneda = self.listaImagenes[self.posImagen]
        self.rect=self.ImagenMoneda.get_rect()
        
        self.tiempocambio=1
        self.rect.top=posy
        self.rect.left=posx
        
    def dibujar(self,superficie):
        self.ImagenMoneda=self.listaImagenes[self.posImagen]
        superficie.blit(self.ImagenMoneda,self.rect)
        
    def animacion(self,tiempo):
        if self.tiempocambio==tiempo:
            self.posImagen+= 1
            self.tiempocambio+= 1
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen=0
        
