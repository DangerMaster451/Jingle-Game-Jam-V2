from Game import Game
import pygame

game = Game()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    mouseX, mouseY = pygame.mouse.get_pos()

    # Particles
    for particle in game.particles:
        particle.render(screen)    
        if particle.lifetime < 0:
            game.particles.remove(particle)

    for pickup in game.pickups:
        pickup.render(screen)
        pickup.update_color(dt)
        if pickup.get_distance_to_object(game.player) < (pickup.hitboxRadius + game.player.hitboxRadius):
            # Add to score
            game.pickups.remove(pickup)
        if pickup.lifetime <= 0:
            game.pickups.remove(pickup)

    # Player
    game.player.render(screen)
    game.player.move_toward(mouseX, mouseY, dt)

    if game.player.health <= 0:
        game.game_over()
        running = False

    # Enemies
    game.spawn_enemies(10, 800)

    for enemy in game.enemies:
        enemy.render(screen)
        enemy.move_toward(game.player.x, game.player.y, dt)

        if game.player.invincibility_frames <= 0:
            if enemy.get_distance_to_object(game.player) < (game.player.hitboxRadius + enemy.hitboxRadius):
                game.player.take_damage(enemy.damage, dt)
                game.spawnBloodCloud(game.player.x, game.player.y, 25, 40, 0, 50)
        else:
            game.player.invincibility_frames -= 1 * dt

        for projectile in game.projectiles:
            if enemy.get_distance_to_object(projectile) < (projectile.hitboxRadius + enemy.hitboxRadius):
                enemy.take_damage(projectile.damage)
                game.spawnIceBloodCloud(enemy.x, enemy.y, 25, 40, 0, 50)
                if enemy.health <= 0:
                    game.enemies.remove(enemy)
                    game.spawn_pickup(enemy.x, enemy.y)

    # Projectiles
    for projectile in game.projectiles:
        projectile.render(screen)
        projectile.update(dt)
        if projectile.get_distance_to_object(game.player) > 1000:
            game.projectiles.remove(projectile)

    # Upgrades
    for upgrade in game.upgrades:
        if upgrade.check_cool_down(dt):
                game.handle_upgrade_actions(upgrade)

    # UI Elements

    game.player.healthbar.render(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()