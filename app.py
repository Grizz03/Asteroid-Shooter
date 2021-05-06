import pygame
import sys

pygame.init()  # Initiate pygame
screen = pygame.display.set_mode((1280, 720))  # Set display surface & size
clock = pygame.time.Clock()  # Create clock object

while True:  # MAIN GAME LOOP
    for event in pygame.event.get():  # Checks for EVENTS / PLAYER INPUT
        if event.type == pygame.QUIT:  # Close the game
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Draw frames
    clock.tick(140)  # Control the framerate
