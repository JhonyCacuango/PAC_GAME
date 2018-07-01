import pygame

pygame.init()
sonido1=pygame.mixer.Sound("pasos.wav")
# clase base para los sprites
class Ladron(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.sheet=pygame.image.load("ladron.png")#cargamos el personaje
        self.sheet.set_clip(pygame.Rect(0,0,52,76))#definimos un rectangulo con las dimenciones del personaje
        self.image = self.sheet.subsurface(self.sheet.get_clip())#lo definimos como imagen
        self.rect=self.image.get_rect()
        self.rect.topleft = pos#optener la posicion inicial del personaje
        self.frame = 0 #el frame inicial
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        self.up_states = { 0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76) }
        self.down_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
#optener el frame en el que se encuentra
    def get_frame(self, frame_set):
        self.frame+=1
        if self.frame>(len(frame_set)-1):
            self.frame=0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect)is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
# definir los movimientos en las diferentes direcciones 
    def update(self,direc):
        if direc=='left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direc == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direc == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direc == 'down':
            self.clip(self.down_states)
            self.rect.y += 5
#definir las pocisiones iniciales de cada estado del personaje
        if direc == 'stand_left':
            self.clip(self.left_states[0])
        if direc == 'stand_right':
            self.clip(self.right_states[0])
        if direc == 'stand_up':
            self.clip(self.up_states[0])
        if direc == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

#definir los movimiento del personaje
    #salida
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
    # evento de tipo presionar tecla
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
                sonido1.play()
            if event.key == pygame.K_RIGHT:
                self.update('right')
                sonido1.play()
            if event.key == pygame.K_UP:
                self.update('up')
                sonido1.play()
            if event.key == pygame.K_DOWN:
                self.update('down')
                sonido1.play()
    # evento de tipo soltar tecla
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
                sonido1.stop()
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
                sonido1.stop()
            if event.key == pygame.K_UP:
                self.update('stand_up')
                sonido1.stop()
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
                sonido1.stop()
