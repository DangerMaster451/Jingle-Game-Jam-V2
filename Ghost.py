from __future__ import annotations
from Enemy import Enemy
from GameObject import GameObject
from Healthbar import Healthbar
import pygame
import math

class Ghost(GameObject):
    def __init__(self, x:float, y:float, target:Enemy) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.target = target
        self.speed = 175
        self.image = self.load_image("Assets/ghost.png", (60,60))
        

    def render(self, screen:pygame.Surface):
        x_component = self.speed * math.cos(self.direction)

        #if x_component > 0:
        #    rotated_image = pygame.transform.rotate(self.image,-35)
        #else:
        #    rotated_image = pygame.transform.rotate(self.image, 35)

        screen.blit(self.image, (self.x, self.y))