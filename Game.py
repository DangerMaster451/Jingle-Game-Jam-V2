from __future__ import annotations
from Upgrade import Upgrade, Default, Thorns, SweepingEdge, Healing, Speed, Snowball_Upgrade, Necromancer
from UpgradePickup import UpgradePickup
from Pickup import Pickup
from Enemy import Enemy
from Player import Player
from Particles import Particle, Blood, IceBlood
from GameObject import GameObject
from Projectiles import Projectile, Snowball
from Healthbar import Healthbar
from Scorebar import Scorebar
from Ghost import Ghost

import math
import random
import pygame

class Game:
    def __init__(self, screen_size:tuple[int,int]) -> None:
        self.player = Player(500, 500)
        self.enemies:list[Enemy] = []
        self.ghosts:list[Ghost] = []
        self.projectiles:list[Projectile] = []
        self.pickups:list[Pickup] = []
        self.particles:list[Particle] = []
        self.upgrades:list[Upgrade] = [Default()]
        self.upgrade_pickups:list[UpgradePickup] = []
        self.health_bars:list[Healthbar] = [self.player.healthbar]
        self.score_bar:Scorebar = Scorebar(screen_size)
        self.score = 0
        self.required_score = 25
        self.wave = 1

        self.disable_spawning:bool = False

        self.ghost_spawn_chance = 7
        self.enemy_spawn_chance = 10

        self.background_music = pygame.mixer.Sound("Assets/Light Jazz (loop).wav")
        self.player_hurt_sound = pygame.mixer.Sound("Assets/grunt.mp3")
        self.enemy_hurt_sound = pygame.mixer.Sound("Assets/ice_hit.mp3")
        self.pick_up_sound = pygame.mixer.Sound("Assets/pick_up.mp3")
        self.dash_sound = pygame.mixer.Sound("Assets/dash.mp3")
        self.ghost_spawn_sound = pygame.mixer.Sound("Assets/ghost_spawn.mp3")
        self.win_wave_sound = pygame.mixer.Sound("Assets/win wave.mp3")

    def spawn_enemies(self, max_enemies:int, spawn_radius:int, center:tuple[float,float]) -> None:
        if random.randint(1, self.enemy_spawn_chance) == 1:
            if len(self.enemies) < max_enemies:
                direction = random.randint(0,360)
                x = math.sin(math.radians(direction)) * spawn_radius + center[0]
                y = math.cos(math.radians(direction)) * spawn_radius + center[1]
                enemy = Enemy(x, y)

                self.enemies.append(enemy)
                self.health_bars.append(enemy.health_bar)

    def handle_enemy_damage(self, enemy:Enemy, damage:float):
        enemy.take_damage(damage)
        self.enemy_hurt_sound.play()
        self.spawnIceBloodCloud(enemy.x, enemy.y, 50, 75, 0, 150)
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
        if random.randint(1, self.ghost_spawn_chance) == 1 and len(self.enemies) != 0:
            enemy = self.enemies[random.randint(0, len(self.enemies)-1)]
            self.ghosts.append(Ghost(x, y, enemy))
            self.ghost_spawn_sound.play()

    def handle_player_animation(self, mouseX:int, mouseY:int, dt:float):
        if self.player.animation_frames <= 0:
            if self.player.current_frame == 0:
                self.player.current_frame = 1
            else:
                self.player.current_frame = 0

            self.player.animation_frames = self.player.max_animation_frames
        else:
            self.player.animation_frames -= 1 * dt

        mouse = GameObject()
        mouse.x = mouseX
        mouse.y = mouseY
        if self.player.x > mouseX and self.player.get_distance_to_object(mouse) > 15:
            self.player.image = pygame.transform.flip(self.player.frames[self.player.current_frame], True, False)
        else:
            self.player.image = self.player.frames[self.player.current_frame]

    def handle_upgrade_spawning(self, screen_size:tuple[int,int]) -> None:
        if not self.disable_spawning:
            return None
        if len(self.enemies) != 0:
            return None
        if len(self.upgrade_pickups) != 0:
            return None
        
        self.win_wave_sound.play()
        upgrade1 = UpgradePickup(screen_size[0]/4, screen_size[1]/2, Healing())
        upgrade2 = UpgradePickup(screen_size[0]/4*3, screen_size[1]/2, Necromancer())

        self.upgrade_pickups.append(upgrade1)
        self.upgrade_pickups.append(upgrade2)

    def game_over(self):
        pass

    def game_loop(self, screen:pygame.Surface, keys, dt:float):
        mouseX, mouseY = pygame.mouse.get_pos()
        window_size = pygame.display.get_window_size()

        # Particles
        for particle in self.particles:
            particle.render(screen)    
            if particle.lifetime < 0:
                self.particles.remove(particle)

        # Pickups
        for pickup in self.pickups:
            pickup.render(screen)
            if pickup.get_distance_to_object(self.player) < (pickup.hitboxRadius + self.player.hitboxRadius):
                self.score += 1
                self.pickups.remove(pickup)
                self.pick_up_sound.play()
            if pickup.lifetime <= 0:
                self.pickups.remove(pickup)

        self.required_score = self.get_required_score(self.wave)
        if self.wave < 10:
            self.enemy_spawn_chance = 11 - self.wave
        else:
            self.enemy_spawn_chance = 1

        # Player
        self.player.render(screen)
        self.handle_player_animation(mouseX, mouseY, dt)
        self.player.move_toward(mouseX, mouseY, self.player.speed, dt)

        mouseDown = pygame.mouse.get_pressed()[0]
        self.player.dash(mouseX, mouseY, mouseDown, self.dash_sound, dt)
        
        if self.player.dash_cooldown > 0:
            self.player.dash_cooldown -= 1 * dt

        if self.player.dash_length <= 0:
            self.player.dashing = False

        # Enemies
        if not self.disable_spawning:
            self.spawn_enemies(self.get_total_enemies(self.wave), round(window_size[0]/2), (window_size[0]/2, window_size[1]/2))

        for enemy in self.enemies:
            enemy.render(screen)

            enemy.move_toward(self.player.x, self.player.y, enemy.speed, dt)

            if self.player.invincibility_frames <= 0:
                if enemy.get_distance_to_object(self.player) < (self.player.hitboxRadius + enemy.hitboxRadius):
                    self.player.take_damage(enemy.damage)
                    self.player_hurt_sound.play()
                    self.apply_thorns()
                    self.spawnBloodCloud(self.player.x, self.player.y, 50, 75, 0, 300)
                    
            else:
                self.player.invincibility_frames -= 1 * dt

            for projectile in self.projectiles:
                if enemy.get_distance_to_object(projectile) < (projectile.hitboxRadius + enemy.hitboxRadius):
                    if enemy.invincibility_frames <= 0:
                        self.handle_enemy_damage(enemy, projectile.damage)
                        self.apply_sweeping_edge(enemy)
                if enemy.invincibility_frames > 0:
                    enemy.invincibility_frames -= 1 * dt  

        # Ghosts
        for ghost in self.ghosts:
            ghost.move_toward(ghost.target.x, ghost.target.y, ghost.speed, dt)
            ghost.render(screen)

            if ghost.get_distance_to_object(ghost.target) < 10:
                self.ghosts.remove(ghost)
                if ghost.target in self.enemies:
                    self.handle_enemy_damage(ghost.target, 1000)

        # Projectiles
        for projectile in self.projectiles:
            projectile.render(screen)
            projectile.update(dt)
            if projectile.get_distance_to_object(self.player) > 2000:
                self.projectiles.remove(projectile)

        # Upgrades
        for upgrade in self.upgrades:
            if upgrade.check_cool_down(dt):
                    self.handle_upgrade_actions(upgrade)

            if type(upgrade) == Healing:
                if self.player.health < 70:
                    self.player.health += 30
                else:
                    self.player.health = 100
                self.upgrades.remove(upgrade)

            if type(upgrade) == Speed:
                self.player.speed = self.player.speed * 1.50
                self.upgrades.remove(upgrade)

            if type(upgrade) == Snowball_Upgrade:
                if type(self.upgrades[0]) == Default:
                    self.upgrades[0].cool_down = 0.5 * self.upgrades[0].cool_down
                    self.upgrades.remove(upgrade)   

            if type(upgrade) == Necromancer:
                if self.ghost_spawn_chance == 7:
                    self.ghost_spawn_chance = 3
                elif self.ghost_spawn_chance == 3:
                    self.ghost_spawn_chance = 1
                self.upgrades.remove(upgrade)

        # Upgrade Pickups
        self.handle_upgrade_spawning(window_size)

        for upgrade_pickup in self.upgrade_pickups:
            upgrade_pickup.render(screen)

            if upgrade_pickup.get_distance_to_object(self.player) <= (self.player.hitboxRadius + upgrade_pickup.height):
                upgrade_pickup.render_textbox(screen)
                if keys[pygame.K_SPACE]:
                    self.upgrades.append(upgrade_pickup.upgrade)
                    self.disable_spawning = False
                    self.score = 0
                    self.upgrade_pickups = []
                    self.pickups = []
                    self.wave += 1

        # UI Elements
        for healthbar in self.health_bars:
            healthbar.render(screen)

        self.score_bar.render(self.score, self.required_score, screen)
        if self.score >= self.required_score:
            self.disable_spawning = True

    def get_total_enemies(self, wave:int) -> int:
        return round(0.5 * wave*wave) + 30
    
    def get_required_score(self, wave:int) -> int:
        return round(0.4*wave*wave) + 25
    