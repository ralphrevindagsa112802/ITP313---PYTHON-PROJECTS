import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
pygame.display.set_caption("Avoid the Enemies")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Enemy
enemy_size = 50
enemy_speed = 5
enemy_frequency = 25
enemies = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Spawn enemies
    if random.randint(1, enemy_frequency) == 1:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Check collisions
    for enemy in enemies:
        if (
            player_x < enemy[0] < player_x + player_size
            and player_y < enemy[1] < player_y + player_size
        ):
            running = False

    # Remove off-screen enemies
    enemies = [enemy for enemy in enemies if enemy[1] < height]

    # Update score
    score += 1

    # Clear the screen
    screen.fill(white)

    # Draw player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, white, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Draw score
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
