from GameObject import GameObject
from Healthbar import Healthbar
import pygame

class Player(GameObject):
    def __init__(self, x:float, y:float) -> None:
       super().__init__(x, y, 0, 125, 30, "Assets/Evil Snowman.png", (100,100))
       self.health:float = 100
       self.max_health:float = 100
       self.invincibility_frames:float = 0
       self.dash_cooldown:float = 0
       self.dash_max_cooldown:float = 2
       self.max_dash_length:float = 0.5
       self.dash_length:float = self.max_dash_length
       self.healthbar = Healthbar(50, 10, self)

    def take_damage(self, value:float):
        if self.invincibility_frames <= 0:
            self.health -= value
            self.invincibility_frames:float = 10

    def render(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "cornsilk1", (self.x, self.y), self.hitboxRadius)

    def dash(self, x:float, y:float, dt:float):
        if self.dash_cooldown <= 0:
            self.dash_length = self.max_dash_length

        if self.dash_length == self.max_dash_length:
            self.invincibility_frames = 10
            self.dash_cooldown = self.dash_max_cooldown
            self.dash_length = self.max_dash_length
        elif self.dash_length > 0:
            self.move_toward(x, y, self.speed*4, dt)

        self.dash_length -= 2 * dt