from __future__ import annotations
import pygame
import math

class GameObject():
    def __init__(self, x:float, y:float, direction:float, speed:int, hitboxRadius:int, imagePath:str, imageSize:tuple[int,int]) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.hitboxRadius = hitboxRadius
        self.image = self.load_image(imagePath, imageSize)
        self.health:float = 0
        self.max_health:float = 0

    def update(self, dt:float) -> None:
        pass

    def render(self, screen:pygame.Surface) -> None:
        pygame.Surface.blit(screen, self.image, (self.x, self.y))
    
    def load_image(self, path:str, size:tuple[int,int]) -> pygame.Surface:
        return pygame.transform.scale(pygame.image.load(path), size)
    
    def move_toward(self, x:float, y:float, dt:float) -> None:
        self.direction = math.atan2((y - self.y), (x - self.x)) + math.pi/2
        self.x += math.sin(self.direction) * self.speed * dt
        self.y -= math.cos(self.direction) * self.speed * dt

    def get_distance_to_object(self, object:GameObject) -> float:
        return math.sqrt((object.y - self.y)**2 + (object.x - self.x)**2)
    
    def check_collisions(self, objects:list) -> GameObject | None:
        for object in objects:
            if self.get_distance_to_object(object) < self.hitboxRadius + object.hitboxRadius:
                if object != self:
                    return object
        return None