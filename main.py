import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collect the Coins')

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 36)

# Player properties
player_size = 50
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Coin properties
coin_size = 30
coin_x = random.randint(0, screen_width - coin_size)
coin_y = random.randint(0, screen_height - coin_size)

# Score
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Boundaries
    if player_x < 0:
        player_x = 0
    elif player_x + player_size > screen_width:
        player_x = screen_width - player_size

    if player_y < 0:
        player_y = 0
    elif player_y + player_size > screen_height:
        player_y = screen_height - player_size

    # Check for collision with coin
    if (player_x < coin_x + coin_size and
        player_x + player_size > coin_x and
        player_y < coin_y + coin_size and
        player_y + player_size > coin_y):
        score += 1
        coin_x = random.randint(0, screen_width - coin_size)
        coin_y = random.randint(0, screen_height - coin_size)

    # Fill screen with black
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    # Draw coin
    pygame.draw.rect(screen, red, (coin_x, coin_y, coin_size, coin_size))

    # Display score
    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

