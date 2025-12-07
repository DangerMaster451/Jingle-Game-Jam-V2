from GameObject import GameObject
from Healthbar import Healthbar
import pygame

class Player(GameObject):
    def __init__(self, x:float, y:float) -> None:
       super().__init__()
       self.x = x
       self.y = y
       self.health:float = 100
       self.max_health:float = 100
       self.size = 30
       self.dash_size = 20
       self.hitboxRadius = 25
       self.speed = 125
       self.invincibility_frames:float = 0
       self.max_invincibility_frames:float = 25
       self.animation_frames:float = 0
       self.max_animation_frames: float = 0.8
       self.dash_cooldown:float = 0
       self.dash_max_cooldown:float = 1
       self.max_dash_length:float = 0.5
       self.dash_length:float = self.max_dash_length
       self.healthbar = Healthbar(75, 25, 135, self)
       self.dashing:bool = False

       self.frames = [self.load_image("Assets/Girl.png", (32*2,48*2)), self.load_image("Assets/Girl 2.png", (32*2, 48*2))]
       self.current_frame = 0
       self.image = self.frames[self.current_frame]
       
    def take_damage(self, value:float):
        if self.invincibility_frames <= 0:
            self.health -= value
            self.invincibility_frames:float = self.max_invincibility_frames

    def render(self, screen:pygame.Surface):
        imageSize = self.image.get_size()
        pygame.Surface.blit(screen, self.image, (self.x - imageSize[0]/2, self.y - imageSize[1]/2))
            
    def dash(self, x:float, y:float, mouseDown:bool, sound:pygame.mixer.Sound, dt:float):
        if self.dash_cooldown <= 0:
            self.dash_length = self.max_dash_length

        if self.dash_length == self.max_dash_length and mouseDown:
            self.dashing = True
            sound.play()
            self.invincibility_frames = 7
            self.dash_cooldown = self.dash_max_cooldown
            self.dash_length = self.max_dash_length

        if self.dash_length > 0 and mouseDown:
            self.move_toward(x, y, self.speed*4, dt)

        self.dash_length -= 2 * dt