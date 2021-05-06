import pygame
import sys

pygame.init()  # Initiate pygame
screen = pygame.display.set_mode((1280, 720))  # Set display surface & size
clock = pygame.time.Clock()  # Create clock object


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super(SpaceShip, self).__init__()
        self.image = pygame.image.load(path)  # Creates surface
        self.rect = self.image.get_rect(center=(x_pos, y_pos))  # Creates rectangle


spaceship = SpaceShip('spaceship.png', 640, 500, 10)  # spaceship image and starting location
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

while True:  # MAIN GAME LOOP
    for event in pygame.event.get():  # Checks for EVENTS / PLAYER INPUT
        if event.type == pygame.QUIT:  # Close the game
            pygame.quit()
            sys.exit()

    screen.fill((42, 55, 70)) # colors the background of screen
    spaceship_group.draw(screen) # draws image on screen
    pygame.display.update()  # Draw frames
    clock.tick(140)  # Control the framerate
