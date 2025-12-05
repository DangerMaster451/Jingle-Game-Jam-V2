from __future__ import annotations
from GameObject import GameObject
from Healthbar import Healthbar
import pygame

class Enemy(GameObject):
    def __init__(self, x:float, y:float):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 75
        self.health = 30
        self.hitboxRadius = 60
        self.max_health = 30
        self.damage = 25
        self.health_bar = Healthbar(25, 5, 50, self)
        self.invincibility_frames:float = 0
        self.image = self.load_image("Assets/evil_snowman.png", (100,100))

    def take_damage(self, value:float):
        if self.invincibility_frames <= 0:
            self.health -= value
            self.invincibility_frames:float = 1     