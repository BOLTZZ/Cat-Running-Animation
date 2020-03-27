import pygame


class SpriteSheet():

    def __init__(self, img_path):
        # Constructor function up above
        self.sprite_sheet = pygame.image.load("runningcat.png")
        # Loads up the running cat image.

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # Background is positioned in accordance to sprite_sheet.
        image.set_colorkey(image.get_at((0, 0)))
        return image
