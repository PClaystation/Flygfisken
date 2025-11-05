import pygame
import random

# --- Setup ---
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flygfisk")

# Fonts
font = pygame.font.SysFont('Arial', 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (135, 206, 235)

# Clock
clock = pygame.time.Clock()

# Character
character_img = pygame.image.load("Assets/Flygfisk_placeholder.png").convert()
character = pygame.transform.scale(character_img, (100, 100))

# --- Game Loop ---
running = True
GROUND_Y = 10

y = GROUND_Y
velocity = 0
gravity = 1.5
score = 0

obstacles = []
spawn_timer = 0



while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if y == 300:
                    velocity = -30  # jump impulse (negative = up)



    # physics
    velocity += gravity  # apply gravity
    y += velocity         # update position

    # floor collision
    if y > 300:
        y = 300
        velocity = 0

        # spawn new obstacles
    spawn_timer += 1
    if spawn_timer > 90:  # every ~1.5s at 60fps
        spawn_timer = 0
        height = random.randint(40, 100)
        obstacle_y = 400 - height  # spawn ON the ground
        obstacles.append(pygame.Rect(WIDTH, obstacle_y, 30, height))

    # move obstacles
    for rect in obstacles:
        rect.x -= 8
    # remove ones that are off-screen
    obstacles = [r for r in obstacles if r.x > -50]

    # score
    score += 1

    # Draw
    screen.fill(BLACK)
    pygame.draw.rect(screen, SKY_BLUE, (0, 0, WIDTH, HEIGHT//1.5))      # sky
    pygame.draw.rect(screen, BLUE, (0, HEIGHT // 1.5, WIDTH, HEIGHT // 2)) # water
    screen.blit(character, (100, y))
    pygame.draw.rect(screen, WHITE, (20, 30, 200, 50))
    screen.blit(font.render("Score:", True, BLACK), (30, 40))
    screen.blit(font.render(f"{score}", True, BLACK), (120, 41))
    for rect in obstacles:
        pygame.draw.rect(screen, WHITE, rect)




    # Update
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
