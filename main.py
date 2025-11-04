import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flygfisk")

# Set up fonts
font = pygame.font.SysFont('Arial', 24)
small_font = pygame.font.SysFont('Arial', 18)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
S_BLUE = (135, 206, 235)

# Clock
clock = pygame.time.Clock()

character = pygame.transform.scale(pygame.image.load("Assets/Flygfisk_placeholder.png"), (100, 100)).convert()

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen
    screen.fill(BLACK)

    # Draw some text
    text_surface = font.render("Hello, Pygame!", True, WHITE)
    screen.blit(text_surface, (50, 50))

    pygame.draw.rect(screen, BLUE, (-10, 450, 1000, 1000), 50000)
    pygame.draw.rect(screen, S_BLUE, (-10, -10, 1000, 460), 5000000)


    y = 100

    
    y += 10

    screen.blit(character, (100, y))




    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
