from GameObject import GameObject

import math
import pygame

class Projectile(GameObject):
    def __init__(self, x:float, y:float, direction:float, damage:float, speed:int, hitboxRaidus:int, imagePath:str, imageSize:tuple[int,int]) -> None:
        super().__init__()
        self.damage = damage
        self.x = x
        self.y = y
        self.direction = direction
        self.damage = damage
        self.speed = speed
        self.hitboxRadius = hitboxRaidus
        self.imagePath = imagePath
        self.imageSize = imageSize        

class Snowball(Projectile):
    def __init__(self, x:float, y:float, direction:float) -> None:
        self.image = self.load_image("Assets/Snowball.png", (50,50))
        super().__init__(x, y, direction, 30, 750, 15, "Assets/Snowball.png", (30,30))

    def update(self, dt:float) -> None:
        self.x += math.sin(self.direction) * self.speed * dt
        self.y -= math.cos(self.direction) * self.speed * dt

    #def render(self, screen:pygame.Surface):
    #    pygame.draw.circle(screen, "cyan", (self.x, self.y), 15)