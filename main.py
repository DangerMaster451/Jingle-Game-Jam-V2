from Game import Game
import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Attack of the Deranged Mutant Killer Monster Snow Goons")
clock = pygame.time.Clock()
running = True
dt = 0

game = Game()

#game.background_music.play(-1)

while running:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("azure1")
    mouseX, mouseY = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    window_size = pygame.display.get_window_size()

    # Particles
    for particle in game.particles:
        particle.render(screen)    
        if particle.lifetime < 0:
            game.particles.remove(particle)

    # Pickups
    for pickup in game.pickups:
        pickup.render(screen)
        if pickup.get_distance_to_object(game.player) < (pickup.hitboxRadius + game.player.hitboxRadius):
            game.score += 5
            game.pickups.remove(pickup)
            game.pick_up_sound.play()
        if pickup.lifetime <= 0:
            game.pickups.remove(pickup)

    # Player
    game.player.render(screen)
    game.handle_player_animation(mouseX, mouseY, dt)
    game.player.move_toward(mouseX, mouseY, game.player.speed, dt)

    if game.player.health <= 0:
        game.game_over()
        running = False

    mouseDown = pygame.mouse.get_pressed()[0]
    game.player.dash(mouseX, mouseY, mouseDown, game.dash_sound, dt)
    
    if game.player.dash_cooldown > 0:
        game.player.dash_cooldown -= 1 * dt

    if game.player.dash_length <= 0:
        game.player.dashing = False

    # Enemies
    if not game.disable_spawning:
        game.spawn_enemies(10, round(window_size[0]/2), (window_size[0]/2, window_size[1]/2))

    for enemy in game.enemies:
        enemy.render(screen)

        enemy.move_toward(game.player.x, game.player.y, enemy.speed, dt)

        if game.player.invincibility_frames <= 0:
            if enemy.get_distance_to_object(game.player) < (game.player.hitboxRadius + enemy.hitboxRadius):
                game.player.take_damage(enemy.damage)
                game.player_hurt_sound.play()
                game.apply_thorns()
                game.spawnBloodCloud(game.player.x, game.player.y, 50, 75, 0, 300)
                
        else:
            game.player.invincibility_frames -= 1 * dt

        for projectile in game.projectiles:
            if enemy.get_distance_to_object(projectile) < (projectile.hitboxRadius + enemy.hitboxRadius):
                if enemy.invincibility_frames <= 0:
                    game.handle_enemy_damage(enemy, projectile.damage)
                    game.apply_sweeping_edge(enemy)
            if enemy.invincibility_frames > 0:
                enemy.invincibility_frames -= 1 * dt  

    # Ghosts
    for ghost in game.ghosts:
        ghost.move_toward(ghost.target.x, ghost.target.y, ghost.speed, dt)
        ghost.render(screen)

        if ghost.get_distance_to_object(ghost.target) < 10:
            game.ghosts.remove(ghost)
            if ghost.target in game.enemies:
                game.handle_enemy_damage(ghost.target, 1000)

    # Projectiles
    for projectile in game.projectiles:
        projectile.render(screen)
        projectile.update(dt)
        if projectile.get_distance_to_object(game.player) > 2000:
            game.projectiles.remove(projectile)

    # Upgrades
    for upgrade in game.upgrades:
        if upgrade.check_cool_down(dt):
                game.handle_upgrade_actions(upgrade)

    # Upgrade Pickups
    game.handle_upgrade_spawning(window_size)

    for upgrade_pickup in game.upgrade_pickups:
        upgrade_pickup.render(screen)

        if upgrade_pickup.get_distance_to_object(game.player) <= (game.player.hitboxRadius + upgrade_pickup.height):
            upgrade_pickup.render_textbox(screen)
            if keys[pygame.K_SPACE]:
                game.upgrades.append(upgrade_pickup.upgrade)
                game.disable_spawning = False
                game.score = 0
                game.upgrade_pickups = []

    # UI Elements
    for healthbar in game.health_bars:
        healthbar.render(screen)

    game.score_bar.render(game.score, game.required_score, screen)
    if game.score >= game.required_score:
        game.disable_spawning = True

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()