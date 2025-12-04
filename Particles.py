from __future__ import annotations
import pygame
import random

class Particle():
    def __init__(self, x:float, y:float, color:tuple[int,int,int], size:int, lifetime:int) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.lifetime = lifetime

    def render(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        self.lifetime -= 1

class Blood(Particle):
    def __init__(self, x:float, y:float, lifetime:int) -> None:
        if random.randint(0, 10) == 10:
            color = (random.randint(220,255), random.randint(220,255), random.randint(220,255))
        else:  
            color = (random.randint(100,255), 0, 0)
        super().__init__(x, y, color, 5, lifetime)

class IceBlood(Particle):
    def __init__(self, x:float, y:float, lifetime:int) -> None:
        if random.randint(1, 4) == 1:
            color = (15, 244, 252)
        else:  
            brightness = random.randint(210,255)
            color = (brightness, brightness, brightness)
        super().__init__(x, y, color, 5, lifetime)