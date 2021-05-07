import pygame
import sys
import random

pygame.init()  # Initiate pygame
screen = pygame.display.set_mode((1280, 720))  # Set display surface & size
clock = pygame.time.Clock()  # Create clock object


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super(SpaceShip, self).__init__()
        self.image = pygame.image.load(path)  # Creates surface
        self.rect = self.image.get_rect(center=(x_pos, y_pos))  # Creates rectangle
        self.shield_surface = pygame.image.load('./assets/shield.png')
        self.health = 5

    #  Movements of ship
    def update(self):
        self.rect.center = pygame.mouse.get_pos()  # Centers mouse in center of rectangle of spaceship
        self.screen_constraints()
        self.display_health()

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

    # Displaying shield/health
    def display_health(self):
        for index, shield in enumerate(range(self.health)):
            screen.blit(self.shield_surface, (10 + index * 40, 10))

    def get_damage(self, damage_amount):
        self.health -= damage_amount


class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super(Meteor, self).__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.y_speed = y_speed
        self.x_speed = x_speed

    def update(self):  # continuous movement of meteor
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
        # Destroys sprite when outside screen
        if self.rect.centery >= 800:
            self.kill()


class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super(Laser, self).__init__()
        self.image = pygame.image.load(path)  # Creates surface
        self.rect = self.image.get_rect(center=pos)  # Creates rectangle
        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed
        if self.rect.centery <= -100:
            self.kill()


spaceship = SpaceShip('./assets/spaceship.png', 640, 500)  # spaceship image and starting location
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_group = pygame.sprite.Group()

METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, 200)

laser_group = pygame.sprite.Group()

while True:  # MAIN GAME LOOP
    for event in pygame.event.get():  # Checks for EVENTS / PLAYER INPUT
        if event.type == pygame.QUIT:  # Close the game
            pygame.quit()
            sys.exit()

        # Meteor Loop
        if event.type == METEOR_EVENT:
            meteor_path = random.choice(('./assets/Meteor1.png', './assets/Meteor2.png', './assets/Meteor3.png'))
            random_x_pos = random.randrange(0, 1280)
            random_y_pos = random.randrange(-500, -100)
            random_y_speed = random.randrange(2, 8)
            random_x_speed = random.randrange(-1, 1)
            meteor = Meteor(meteor_path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)
            meteor_group.add(meteor)

        # Laser Loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_laser = Laser('./assets/Laser.png', event.pos, 7)
            laser_group.add(new_laser)

        # Collisions
        if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
            spaceship_group.sprite.get_damage(1)

        for laser in laser_group:
            pygame.sprite.spritecollide(laser, meteor_group, True)

    screen.fill((42, 55, 65))  # colors the background of screen

    laser_group.draw(screen)
    meteor_group.draw(screen)
    spaceship_group.draw(screen)  # draws image on screen

    laser_group.update()
    spaceship_group.update()  # Updates sprites
    meteor_group.update()
    pygame.display.update()  # Draw frames

    clock.tick(140)  # Control the framerate
