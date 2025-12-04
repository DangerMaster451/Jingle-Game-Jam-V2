from GameObject import GameObject
import pygame

class Healthbar():
    def __init__(self, object:GameObject):
        self.width:float = 50
        self.height:float = 10
        self.object = object

    def render(self, screen:pygame.Surface):
        back_rect = pygame.Rect(self.object.x - self.width/2, self.object.y - (self.height + 50), self.width, self.height)
        pygame.draw.rect(screen, "red", back_rect)

        width = (self.object.health / self.object.max_health) * self.width
        front_rect = pygame.Rect(self.object.x - self.width/2, self.object.y - (self.height + 50), width, self.height)
        pygame.draw.rect(screen, "orange", front_rect)