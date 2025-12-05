from __future__ import annotations
from Enemy import Enemy
from GameObject import GameObject
from Healthbar import Healthbar
import pygame

class Ghost(GameObject):
    def __init__(self, x:float, y:float, target:Enemy) -> None:
        self.x = x
        self.y = y
        self.target = target
        self.speed = 90
        super().__init__()

    def render(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "darkorchid2", (self.x, self.y), 20)