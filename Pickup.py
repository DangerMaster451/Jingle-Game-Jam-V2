from GameObject import GameObject
import math
import pygame

class Pickup(GameObject):
    def __init__(self, x:float, y:float, lifetime:int=50) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.hitboxRadius = 15
        self.imagePath = "Assets/Player.png"
        self.imageSize = (15,15)
        self.lifetime = lifetime
        self.color:tuple[int,int,int] = (0,0,0)
        
    
    def render(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
        

    def update_color(self, dt:float) -> None:
        green = round(220 + math.sin(self.lifetime/10) * 35)
        self.color = (36, green, 122)
        self.lifetime -= 1 * dt
