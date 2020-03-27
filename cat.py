import pygame
import random


class Cat(pygame.sprite.Sprite):
        # Cat class is used to divide up the whol sprite sheet into
        # indivual cat pieces.
    def __init__(self, pos, images):
        super().__init__()
        # Creates super instance
        self.images = images
        # Sets the images in the constructor to images input.
        self.image = images[0]
        # Sets image to the first value.
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = [8, 0]

    def update(self):
        frame = pygame.time.get_ticks() // 60 % 8
        # We are setting up frames using ticks and using 60 % 8 to find the
        # residue and rate of change.
        self.image = self.images[frame]
        # Splices up the images so we can loop through them.
        self.rect.move_ip(self.speed)
        # Moves the rect
        if self.rect.left > pygame.display.Info().current_w:
            # Checks if the left side of the rect is greater than the 
            # current_width of pygame display.
            self.rect.right = 0
            self.rect.centery = random.randint(
                50,
                pygame.display.Info().current_h - 50
            )
            # Picks a random height (y position) for the rect.

    def draw(self, screen):
        screen.blit(self.image, self.rect)
