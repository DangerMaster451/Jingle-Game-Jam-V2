from GameObject import GameObject
from Upgrade import Upgrade
import pygame

class UpgradePickup(GameObject):
    def __init__(self, x:float, y:float, upgrade:Upgrade) -> None:
        self.x = x
        self.y = y
        self.height = 100
        self.width = 25
        self.upgrade = upgrade

    def render(self, screen:pygame.Surface) -> None:
        rect = pygame.Rect(round(self.x - self.width/2), round(self.y - self.height/2), self.width, self.height)
        pygame.draw.rect(screen, "red", rect)