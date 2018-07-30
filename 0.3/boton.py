import pygame

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
