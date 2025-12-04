from GameObject import GameObject

import math
import pygame

class Projectile(GameObject):
    def __init__(self, x:float, y:float, direction:float, damage:float, speed:int, hitboxRaidus:int, imagePath:str, imageSize:tuple[int,int]) -> None:
        self.damage = damage
        super().__init__(x, y, direction, speed, hitboxRaidus, imagePath, imageSize)

class Snowball(Projectile):
    def __init__(self, x:float, y:float, direction:float) -> None:
        super().__init__(x, y, direction, 30, 300, 15, "Assets/Snowball.png", (30,30))

    def update(self, dt:float) -> None:
        self.x += math.sin(self.direction) * self.speed * dt
        self.y -= math.cos(self.direction) * self.speed * dt

    def render(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "cyan", (self.x, self.y), 15)