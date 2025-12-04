from GameObject import GameObject
import pygame
import math

class Player(GameObject):
    def __init__(self, x:float, y:float) -> None:
       super().__init__(x, y, 0, 125, 30, "Assets/Evil Snowman.png", (100,100))
       self.health:float = 100
       self.invincibility_frames:float = 0

    def take_damage(self, value:float, dt:float):
        if self.invincibility_frames <= 0:
            self.health -= value
            self.invincibility_frames:float = 10

    def render(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "cornsilk1", (self.x, self.y), self.hitboxRadius)