from Game import Game
import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280*1.5, 720*1.5))
pygame.display.set_caption("Attack of the Deranged Mutant Killer Monster Snow Goons")
clock = pygame.time.Clock()
running = True
paused = False
startMenu = True
game_over = False
dt = 0

game = Game()

game.background_music.play(-1)

font = pygame.font.Font("Assets/Metal Glass.otf", 32)
title = font.render("Attack of the Deranged Mutant Killer Monster Snow Goons", True, "black")
next = font.render("Press SPACE to Continue", True, "black")
width = 100
height = 75

while startMenu:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startMenu = False
            running = False
            game_over = False

    keys = pygame.key.get_pressed()

    screen.fill("azure1")

    window_size = pygame.display.get_window_size()
    text_rect = title.get_rect(center=(window_size[0]/2, window_size[1]/2-150))
    next_rect = next.get_rect(center=(window_size[0]/2, window_size[1]/2))
    screen.blit(title, text_rect)
    screen.blit(next, next_rect)

    if keys[pygame.K_SPACE]:
        startMenu = False

    pygame.display.flip()
    dt = clock.tick(60) / 1000


while running or game_over:
    while running:
        keys = pygame.key.get_pressed()

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = False
                startMenu = False

        screen.fill("azure1")

        if not paused:
            game.game_loop(screen, keys, dt)

            if game.player.health <= 0:
                game.game_over()
                game_over = True
                running = False

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    while game_over:
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                startMenu = False
                game_over = False
                running = False

        keys = pygame.key.get_pressed()

        screen.fill("azure1")

        window_size = pygame.display.get_window_size()
        game_over_text = font.render("You Died!!", True, "black")
        game_over_rect = game_over_text.get_rect(center=(window_size[0]/2, window_size[1]/2-150))
        next_rect = next.get_rect(center=(window_size[0]/2, window_size[1]/2))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(next, next_rect)

        if keys[pygame.K_SPACE]:
            startMenu = False
            game_over = False
            running = True

            game = Game()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

pygame.quit()