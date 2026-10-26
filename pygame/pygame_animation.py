# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = WIDTH / 2
circle_y = HEIGHT / 2
circle_radius = 30
circle_x_speed = 2
circle_y_speed = 3

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    circle_y_speed += 4.9

    circle_x += circle_x_speed

    # boundary checking
    if circle_x > WIDTH - circle_radius:
        circle_x_speed = -circle_x_speed
        circle_x = WIDTH - circle_radius
    elif circle_x <= 0 + circle_radius:
        circle_x_speed = -circle_x_speed

    # Circle y
    if circle_y + circle_y_speed > HEIGHT - circle_radius: # check to see if the ball will go beyond the boundary
        circle_y = HEIGHT - circle_radius # if it will, make it be at the boundry
    else:
        circle_y += circle_y_speed # otherwise, move normally

    if circle_y >= HEIGHT - circle_radius:
        circle_y_speed = -circle_y_speed 
    elif circle_y <= 0 + circle_radius:
        circle_y_speed = -circle_y_speed

    # DRAWING
     
    screen.fill((255, 255, 255))  # always the first drawing command

    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_radius)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
