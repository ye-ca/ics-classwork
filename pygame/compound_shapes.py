#Compound shapes
# Draw with a loop
# pygame template

import pygame
import math

pygame.init()

WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x = 148
cloud_y = 72

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    cloud_x += 5 

    if cloud_x > WIDTH + 40:
        cloud_x = -120

    # DRAWING
    screen.fill((135, 206, 235))  # always the first drawing command

    cloud_colour = (240, 240, 240)


    pygame.draw.circle(screen, cloud_colour, (cloud_x, cloud_y), 40) # 148, 72
    pygame.draw.circle(screen, cloud_colour, (cloud_x + 44, cloud_y + 8), 50)
    pygame.draw.circle(screen, cloud_colour, (cloud_x + 76, cloud_y - 16), 48)

    # Hill
    rect = (-50, HEIGHT - 100, WIDTH + 100, HEIGHT // 2) 
    pygame.draw.ellipse(screen, (100, 180, 100), rect)

    # Grass

    for i in range(40, WIDTH - 20, 10):
        pygame.draw.rect(screen, (65, 120, 35), (i, (math.cos(i) * 30) + HEIGHT - 40, 3, 30))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
