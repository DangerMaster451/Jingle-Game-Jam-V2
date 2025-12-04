from __future__ import annotations
from GameObject import GameObject
from Healthbar import Healthbar
import pygame

class Enemy(GameObject):
    def __init__(self, x:float, y:float):
        super().__init__(x, y, 0, 75, 20, "Assets/Evil Snowman.png", (100,100))
        self.health = 30
        self.max_health = 30
        self.damage = 25
        self.health_bar = Healthbar(25, 5, self)
        self.invincibility_frames:float = 0

    def take_damage(self, value:float):
        if self.invincibility_frames <= 0:
            self.health -= value
            self.invincibility_frames:float = 1

    def render(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "white", (self.x, self.y), 20)