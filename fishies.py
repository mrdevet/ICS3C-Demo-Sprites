# Programmer: Mr. Devet
# Description: Some fish sprites that move on the screen in different ways.

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

from pygame_grid import *
from ucc_sprite import Sprite

# Create and open a pygame screen with the given size
WIDTH = 960
HEIGHT = 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("Fishies")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.Group()

### SET UP YOUR GAME HERE

# Load the images
background_image = pygame.image.load("underwater.png")
fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.flip(fish_image, True, False)




# Main Loop
while True:
    # Set the frame rate to 30 frames per second
    time = clock.tick(60)

    ### MANAGE IN-GAME EVENTS HERE
    



    # Uncomment the next line to show a grid
    #screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()