from __future__ import annotations
import pygame
import math

class GameObject():
    def __init__(self) -> None:
        self.x:float
        self.y:float
        self.hitboxRadius:float
        self.image:pygame.Surface
        self.speed:float

    def update(self, dt:float) -> None:
        pass

    def render(self, screen:pygame.Surface) -> None:
        
        imageSize = self.image.get_size()
        pygame.Surface.blit(screen, self.image, (self.x - imageSize[0]/2, self.y - imageSize[1]/2))
        #pygame.draw.circle(screen, "red", (self.x, self.y), self.hitboxRadius)
        
    
    def load_image(self, path:str, size:tuple[int,int]) -> pygame.Surface:
        return pygame.transform.scale(pygame.image.load(path), size)
    
    def move_toward(self, x:float, y:float, speed:float, dt:float) -> None:
        self.direction = math.atan2((y - self.y), (x - self.x)) + math.pi/2
        self.x += math.sin(self.direction) * speed * dt
        self.y -= math.cos(self.direction) * speed * dt

    def get_distance_to_object(self, object:GameObject) -> float:
        return math.sqrt((object.y - self.y)**2 + (object.x - self.x)**2)
    
    def check_collisions(self, objects:list) -> GameObject | None:
        for object in objects:
            if self.get_distance_to_object(object) < self.hitboxRadius + object.hitboxRadius:
                if object != self:
                    return object
        return None