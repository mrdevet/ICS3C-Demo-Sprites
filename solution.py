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

# Group to store all of the fish in
fishies = pygame.sprite.Group()

# Fish that moves across the screen
fish1 = Sprite(fish_image)
fish1.position = (100,100)
fish1.speed = 1
fish1.add(all_sprites, fishies)

# Fish that moves from top to bottom
fish2 = Sprite(fish_image)
fish2.position = (400,50)
fish2.direction = 270
fish2.speed = 2
fish2.add(all_sprites, fishies)

# Fish that moves diagonally
fish3 = Sprite(fish_image)
fish3.position = (50,200)
fish3.direction = 30
fish3.speed = 1.5
fish3.add(all_sprites, fishies)

# Fish that spins in a circle
fish4 = Sprite(fish_image)
fish4.position = (300,150)
fish4.speed = 4
fish4.add(all_sprites, fishies)


# Main Loop
while True:
    # Set the frame rate to 30 frames per second
    time = clock.tick(60)

    ### MANAGE IN-GAME EVENTS HERE

    # Turn fish4
    fish4.turn_left(5)

    # Check if a fish is off the screen wrap it to the other side
    for fish in fishies:
        if fish.right < 0:
            fish.left = WIDTH
        if fish.left > WIDTH:
            fish.right = 0
        if fish.bottom < 0:
            fish.top = HEIGHT
        if fish.top > HEIGHT:
            fish.bottom = 0

    
    # Set the background color
    screen.blit(background_image, (0, 0))

    # Update the sprites' locations
    all_sprites.update()

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    #screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()