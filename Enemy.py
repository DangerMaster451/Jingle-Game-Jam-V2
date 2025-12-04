from __future__ import annotations
from GameObject import GameObject
import pygame

class Enemy(GameObject):
    def __init__(self, x:float, y:float):
        super().__init__(x, y, 0, 75, 20, "Assets/Evil Snowman.png", (100,100))
        self.health = 30
        self.damage = 25

    def take_damage(self, value:float):
        self.health -= value
        #Spawners.spawnIceBloodCloud(self.x, self.y, 15, 35, 10, 125, game.particles)

    def render(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "white", (self.x, self.y), 20)