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

    #  Movements of ship
    def update(self):
        self.rect.center = pygame.mouse.get_pos()  # Centers mouse in center of rectangle of spaceship
        self.screen_constraints()

    #  Constraints of spaceship on x-axis
    def screen_constraints(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720
        if self.rect.top <= 0:
            self.rect.top = 0


class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super(Meteor, self).__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


spaceship = SpaceShip('./assets/spaceship.png', 640, 500, 10)  # spaceship image and starting location
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor1 = Meteor('./assets/Meteor1.png', 640, 200, 1, 1)  # meteor image
meteor_group = pygame.sprite.Group()
meteor_group.add(meteor1)

while True:  # MAIN GAME LOOP
    for event in pygame.event.get():  # Checks for EVENTS / PLAYER INPUT
        if event.type == pygame.QUIT:  # Close the game
            pygame.quit()
            sys.exit()

    screen.fill((42, 55, 65))  # colors the background of screen
    meteor_group.draw(screen)
    spaceship_group.draw(screen)  # draws image on screen
    spaceship_group.update()  # Updates sprites
    pygame.display.update()  # Draw frames
    clock.tick(140)  # Control the framerate
