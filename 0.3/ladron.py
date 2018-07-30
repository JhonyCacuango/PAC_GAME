import pygame

pygame.init()
sonido1=pygame.mixer.Sound("pasos.wav")# crea el archivo de audio 
sonido1.set_volume(0.05)
# clase base para los sprites
class Ladron(pygame.sprite.Sprite):
    
    def __init__(self, pos,jugador):# parametros iniciales de la clase
        self.sheet=pygame.image.load(jugador)#cargamos el personaje
        self.sheet.set_clip(pygame.Rect(0,0,52,76))#definimos un rectangulo con las dimenciones del personaje
        self.image = self.sheet.subsurface(self.sheet.get_clip())#lo definimos como imagen
        self.rect=self.image.get_rect()
        self.rect.topleft = pos#optener la posicion inicial del personaje
        self.frame = 0 #el frame inicial
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }# los diferentre sestados de derecha
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }# los estados de izquierda
        self.up_states = { 0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76) }
        self.down_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
        
#optener el frame en el que se encuentra
    def get_frame(self, frame_set):
        self.frame+=1#avanza al siguiente frame
        if self.frame>(len(frame_set)-1):# si esta el el ultimo frame 
            self.frame=0# regresa al inicial 
        return frame_set[self.frame]# devuelve el frame en el que se encuentra 
# definir el rectangulo de la imagen 
    def clip(self, clipped_rect):
        if type(clipped_rect)is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
# definir los movimientos en las diferentes direcciones 
    def update(self,direc):
        
        downapretada,upapretada,leftapretada,rightapretada=False,False,False,False
        wapretada,aapretada,sapretada,dapretada=False,False,False,False
        
        Ancho = 800
        Alto = 600
        if self.rect.left >= 0:
            if direc=='left':
                self.clip(self.left_states)
                leftapretada=True
                self.rect.x -= 8
        if self.rect.right <= Ancho: 
            if direc == 'right':
                self.clip(self.right_states)
                rightapretada=True
                self.rect.x += 8
        if self.rect.top >= 0:
            if direc == 'up':
                self.clip(self.up_states)
                upapretada=True
                self.rect.y -= 8
        if self.rect.bottom <= Alto: 
            if direc == 'down':
                self.clip(self.down_states)
                downapretada=True
                self.rect.y += 8
#definir las pocisiones iniciales de cada estado del personaje
        if direc == 'stand_left':
            leftapretada=False
            if leftapretada:
                self.rect.x -= 8
            else:
                self.clip(self.left_states[0])
            
        if direc == 'stand_right':
            rightapretada=False
            if rightapretada:
                self.rect.x += 8
            else:
                self.clip(self.right_states[0])
            
        if direc == 'stand_up':
            upapretada=False
            if upapretada:
                self.rect.y -= 8
            else:
                self.clip(self.up_states[0])
            
        if direc == 'stand_down':
            downapretada=False
            if downapretada:
                self.rect.y += 8
            else:
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
     #evento de tipo soltar tecla
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
    def handle_event2(self, event):
        if event.type == pygame.QUIT:
            game_over = True
    # evento de tipo presionar tecla
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                self.update('left')
                sonido1.play()
            if event.key == pygame.K_d:
                self.update('right')
                sonido1.play()
            if event.key == pygame.K_w:
                self.update('up')
                sonido1.play()
            if event.key == pygame.K_s:
                self.update('down')
                sonido1.play()
     #evento de tipo soltar tecla
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                self.update('stand_left')
                sonido1.stop()
            if event.key == pygame.K_d:
                self.update('stand_right')
                sonido1.stop()
            if event.key == pygame.K_w:
                self.update('stand_up')
                sonido1.stop()
            if event.key == pygame.K_s:
                self.update('stand_down')
                sonido1.stop()