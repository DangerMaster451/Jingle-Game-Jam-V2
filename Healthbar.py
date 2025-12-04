from GameObject import GameObject
import pygame

class Healthbar():
    def __init__(self, width:float, height:float, object:GameObject):
        self.width:float = width
        self.height:float = height
        self.object = object

    def render(self, screen:pygame.Surface):
        back_rect = pygame.Rect(self.object.x - self.width/2, self.object.y - (self.height + self.width), self.width, self.height)
        pygame.draw.rect(screen, "aquamarine4", back_rect)

        width = (self.object.health / self.object.max_health) * self.width
        front_rect = pygame.Rect(self.object.x - self.width/2, self.object.y - (self.height + self.width), width, self.height)
        pygame.draw.rect(screen, "aqua", front_rect)