from GameObject import GameObject
import math
import pygame

class Pickup(GameObject):
    def __init__(self, x:float, y:float, lifetime:int=50) -> None:
        self.lifetime = lifetime
        self.color:tuple[int,int,int] = (0,0,0)
        super().__init__(x, y, 0, 0, 15, "Assets/Player.png", (15,15))
    
    def render(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
        

    def update_color(self, dt:float) -> None:
        green = round(220 + math.sin(self.lifetime/10) * 35)
        self.color = (36, green, 122)
        self.lifetime -= 1 * dt
