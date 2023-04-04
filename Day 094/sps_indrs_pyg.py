import pygame

import random

# Initialize Pygame

pygame.init()

# Set up the game window

WIDTH, HEIGHT = 600, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invaders")

# Load the images

player_img = pygame.image.load("player.png").convert_alpha()

bullet_img = pygame.image.load("bullet.png").convert_alpha()

alien_imgs = [

    pygame.image.load("alien1.png").convert_alpha(),

    pygame.image.load("alien2.png").convert_alpha(),

    pygame.image.load("alien3.png").convert_alpha(),

]

explosion_img = pygame.image.load("explosion.png").convert_alpha()

# Set up the game variables

player_x, player_y = WIDTH // 2, HEIGHT - 100

player_speed = 5

bullets = []

bullet_speed = 10

alien_speed = 2

aliens = []

for i in range(10):
    alien_x = random.randint(50, WIDTH - 50)

    alien_y = random.randint(50, 200)

    alien_type = random.randint(0, 2)

    alien_img = alien_imgs[alien_type]

    aliens.append({"x": alien_x, "y": alien_y, "img": alien_img})

explosions = []

# Set up the game fonts

font = pygame.font.Font(None, 36)

# Main game loop

clock = pygame.time.Clock()

game_over = False

while not game_over:

    # Handle events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                player_x -= player_speed

            elif event.key == pygame.K_RIGHT:

                player_x += player_speed

            elif event.key == pygame.K_SPACE:

                bullets.append({"x": player_x + 20, "y": player_y - 20})

    # Update game state

    for bullet in bullets:

        bullet["y"] -= bullet_speed

        if bullet["y"] < -20:
            bullets.remove(bullet)

    for alien in aliens:

        alien["x"] += alien_speed

        if alien["x"] > WIDTH - 50 or alien["x"] < 0:

            alien_speed = -alien_speed

            for a in aliens:
                a["y"] += 10

        for bullet in bullets:

            if bullet["x"] > alien["x"] and bullet["x"] < alien["x"] + 50 and bullet["y"] > alien["y"] and bullet["y"] < \
                    alien["y"] + 50:
                explosions.append({"x": alien["x"], "y": alien["y"]})

                aliens.remove(alien)

                bullets.remove(bullet)

    for explosion in explosions:
        explosions.remove(explosion)

    # Draw the game

    WIN.fill((0, 0, 0))

    WIN.blit(player_img, (player_x, player_y))

    for bullet in bullets:
        WIN.blit(bullet_img, (bullet["x"], bullet["y"]))

    for alien in aliens:
        WIN.blit(alien["img"], (alien["x"], alien["y"]))

    for explosion in explosions:
        WIN.blit(explosion_img, (explosion["x"], explosion["y"]))

    pygame.display.update()

    # Set the game
