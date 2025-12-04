from __future__ import annotations
from Upgrade import Upgrade, Default
from Pickup import Pickup
from Enemy import Enemy
from Player import Player
from Particles import Particle, Blood, IceBlood
from Projectiles import Projectile, Snowball
from Healthbar import Healthbar

import math
import random

class Game:
    def __init__(self) -> None:
        self.player = Player(500, 500)
        self.enemies:list[Enemy] = []
        self.projectiles:list[Projectile] = []
        self.pickups:list[Pickup] = []
        self.particles:list[Particle] = []
        self.upgrades:list[Upgrade] = [Default()]
        self.health_bars:list[Healthbar] = [self.player.healthbar]

    def spawn_enemies(self, max_enemies:int, spawn_radius:int) -> None:
        if len(self.enemies) < max_enemies:
            direction = random.randint(0,360)
            x = math.sin(math.radians(direction)) * spawn_radius + self.player.x
            y = math.cos(math.radians(direction)) * spawn_radius + self.player.y
            enemy = Enemy(x, y)

            self.enemies.append(enemy)
            self.health_bars.append(enemy.health_bar)

    def spawnBloodCloud(self, spawnX:float, spawnY:float, radius_min:int, radius_max:int, spread:int, count:int) -> None:
        radius = random.randint(radius_min, radius_max)
        for i in range(count):
            direction = random.randint(0,360)
            distance = random.randint(0, radius)
            x = math.sin(math.radians(direction)) * distance
            y = math.cos(math.radians(direction)) * distance
            lifetime = round(radius_max - distance) * 5
            self.particles.append(Blood(spawnX+x, spawnY+y, lifetime))

    def spawnIceBloodCloud(self, spawnX:float, spawnY:float, radius_min:int, radius_max:int, spread:int, count:int) -> None:
        radius = random.randint(radius_min, radius_max)
        for i in range(count):
            direction = random.randint(0,360)
            distance = random.randint(0, radius)
            x = math.sin(math.radians(direction)) * distance
            y = math.cos(math.radians(direction)) * distance
            lifetime = round(radius_max - distance) * 5
            self.particles.append(IceBlood(spawnX+x, spawnY+y, lifetime))

    def handle_upgrade_actions(self, upgrade:Upgrade):
        if type(upgrade) == Default:
            self.projectiles.append(upgrade.action(self.player))

    def spawn_pickup(self, x:float, y:float):
        self.pickups.append(Pickup(x, y))

    def game_over(self):
        print("Game over lol")


