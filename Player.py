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
       self.hitboxRadius = 30
       self.speed = 125
       self.invincibility_frames:float = 0
       self.max_invincibility_frames:float = 25
       self.dash_cooldown:float = 0
       self.dash_max_cooldown:float = 2
       self.max_dash_length:float = 0.5
       self.dash_length:float = self.max_dash_length
       self.healthbar = Healthbar(50, 10, self)
       self.dashing:bool = False
       
    def take_damage(self, value:float):
        if self.invincibility_frames <= 0:
            self.health -= value
            self.invincibility_frames:float = self.max_invincibility_frames

    def render(self, screen:pygame.Surface):
        if self.dashing:
            pygame.draw.circle(screen, "cornsilk1", (self.x, self.y), self.dash_size)
        else:
            pygame.draw.circle(screen, "cornsilk1", (self.x, self.y), self.size)

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