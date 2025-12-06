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
        self.image = self.load_image(upgrade.image_path, (18*10,23*10))

    def render(self, screen:pygame.Surface) -> None:
        screen.blit(self.image, (round(self.x - self.width/2), round(self.y - self.height/2), self.width, self.height))
        