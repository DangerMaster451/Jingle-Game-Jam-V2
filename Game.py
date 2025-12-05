from __future__ import annotations
from Upgrade import Upgrade, Default, Thorns, SweepingEdge
from Pickup import Pickup
from Enemy import Enemy
from Player import Player
from Particles import Particle, Blood, IceBlood
from Projectiles import Projectile, Snowball
from Healthbar import Healthbar
from Scorebar import Scorebar
from Ghost import Ghost

import math
import random
import pygame

class Game:
    def __init__(self) -> None:
        self.player = Player(500, 500)
        self.enemies:list[Enemy] = []
        self.ghosts:list[Ghost] = []
        self.projectiles:list[Projectile] = []
        self.pickups:list[Pickup] = []
        self.particles:list[Particle] = []
        self.upgrades:list[Upgrade] = [Default(), SweepingEdge()]
        self.health_bars:list[Healthbar] = [self.player.healthbar]
        self.score_bar:Scorebar = Scorebar()
        self.score = 0

        self.ghost_spawn_chance = 1

        self.player_hurt_sound = pygame.mixer.Sound("Assets/player_damage.wav")
        self.enemy_hurt_sound = pygame.mixer.Sound("Assets/ice_hit.mp3")
        self.pick_up_sound = pygame.mixer.Sound("Assets/pick_up.mp3")
        self.dash_sound = pygame.mixer.Sound("Assets/dash.mp3")

    def spawn_enemies(self, max_enemies:int, spawn_radius:int) -> None:
        if len(self.enemies) < max_enemies:
            direction = random.randint(0,360)
            x = math.sin(math.radians(direction)) * spawn_radius + self.player.x
            y = math.cos(math.radians(direction)) * spawn_radius + self.player.y
            enemy = Enemy(x, y)

            self.enemies.append(enemy)
            self.health_bars.append(enemy.health_bar)

    def handle_enemy_damage(self, enemy:Enemy, damage:float):
        enemy.take_damage(damage)
        self.enemy_hurt_sound.play()
        self.spawnIceBloodCloud(enemy.x, enemy.y, 25, 40, 0, 50)
        if enemy.health <= 0:
            self.enemies.remove(enemy)
            self.health_bars.remove(enemy.health_bar)
            self.spawn_pickup(enemy.x, enemy.y)
            self.handle_ghost_spawning(enemy.x, enemy.y)

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

    def apply_thorns(self):
        if any(isinstance(obj, Thorns) for obj in self.upgrades):
            for enemy in self.enemies:
                if enemy.get_distance_to_object(self.player) < Thorns.threshold:
                    self.handle_enemy_damage(enemy, Thorns.damage)

    def apply_sweeping_edge(self, hit_enemy:Enemy):
        if any(isinstance(obj, SweepingEdge) for obj in self.upgrades):
            for enemy in self.enemies:
                if enemy.get_distance_to_object(hit_enemy) < SweepingEdge.threshold and enemy != hit_enemy:
                    self.handle_enemy_damage(enemy, SweepingEdge.damage)

    def spawn_pickup(self, x:float, y:float):
        self.pickups.append(Pickup(x, y))

    def handle_ghost_spawning(self, x:float, y:float):
        if random.randint(1, self.ghost_spawn_chance) == 1:
            enemy = self.enemies[random.randint(0, len(self.enemies)-1)]
            self.ghosts.append(Ghost(x, y, enemy))

    def game_over(self):
        print("Game over lol")