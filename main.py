import pygame
import random
from pygame.locals import*
# Imports everything from pygame.
from sprite_loader import SpriteSheet
from cat import Cat

pygame.init()
# Initalizes pygame

screen_info = pygame.display.Info()
# Gets information about user's screen.

size = (width, height) = (800, 600)
# Sets size parameters

screen = pygame.display.set_mode(size)
# Sets up the variable screen which will set up the user's screen.

clock = pygame.time.Clock()
# Sets up the clock variable

color = (0, 147, 255)
# Sets the color variable to a color using RGB

cat_images = []
# Sets an empty arraylist for cat_image


def get_cat_images():
        cat_sheet = SpriteSheet("runningcat.png")
        # Sets the cat_sheet equal to the runningcat.png
        cat_sheet_width = cat_sheet.sprite_sheet.get_rect().width
        # Sets cat_sheet width to the width of the display.
        cat_sheet_height = cat_sheet.sprite_sheet.get_rect().height
        # Sets cat_sheet width to the width of the display.
        nrows = 4
        # Sets the number rows to 4.
        ncols = 2
        # Sets the number colums to 2.
        cat_width = cat_sheet_width / ncols
        # Sets the cat_width by diving the width by number of columns.
        cat_height = cat_sheet_height / nrows
        for row in range(nrows):
            for col in range(ncols):
                cat_images.append(
                    cat_sheet.get_image(
                        col * cat_width,
                        row * cat_height,
                        cat_width,
                        cat_height
                    )
                )
                # Appends the chat sheet and adds it to the images.\
                scale = 0.5
                cat_images[-1] = pygame.transform.smoothscale(
                    cat_images[-1],
                    (int(cat_width * scale),
                        int(cat_height * scale)
                    )
                )
                # Smoothscales the animation of the cat running.abs


def main():
    get_cat_images()
    cat = Cat((-90, random.randint(50, (height - 50))), cat_images)
    while True:
        # Creates an infinite loop.
        clock.tick(60)
    # for event in pygame.event.get():
    #   if event.type == QUIT:
    #     pygame.exit()
    # Makes sure that if a user presses any keys or moves the mouse the 
    # program doesnt crash.
        cat.update()
        screen.fill(color)
        cat.draw(screen)
        pygame.display.flip()
    # Fills the screen with color and flips the display.


if __name__ == "__main__":
    main()
