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
fish_image_flipped = pygame.transform.flip(fish_image, True, False)
rock_image = pygame.image.load("rock.png")

# Create a group for the fish sprites
fishies = pygame.sprite.Group()

# Create a fish that moves to the right
fish = Sprite(fish_image_flipped)
fish.position = (100, 200)
fish.speed = 1
fish.add(all_sprites, fishies)

# Create a fish that moves to the left
fish2 = Sprite(fish_image)
fish2.position = (300, 100)
fish2.direction = 45
fish2.rotates = False
fish2.speed = 3
fish2.add(all_sprites, fishies)

# Create a fish that moves up
fish3 = Sprite(fish_image)
fish3.position = (200, 400)
fish3.direction = 90
fish3.rotates = False
fish3.speed = 0.5
fish3.add(all_sprites, fishies)

# Create a fish that moves in circles
fish4 = Sprite(fish_image_flipped)
fish4.position = (700, 100)
fish4.rotates = False
fish4.speed = 2
fish4.add(all_sprites, fishies)

# Create a rock sprite
rock = Sprite(rock_image)
rock.center = (WIDTH / 2, 350)
rock.add(all_sprites)

# Main Loop
while True:
    # Set the frame rate to 60 frames per second
    time = clock.tick(60)

    ### MANAGE IN-GAME EVENTS HERE
    
    # Make the fourth fish turn as it moves
    fish4.turn_right(3)
    
    
    for fish in fishies:
        # Make the fish wrap around the ends
        if fish.left > WIDTH:
            fish.right = 0
        if fish.right < 0:
            fish.left = WIDTH
            
        # Makes it so fish bounce off top and bottom
        if fish.top < 0 or fish.bottom > HEIGHT:
            fish.direction = 360 - fish.direction
    
        # If a fish touches the rock, they die
        if pygame.sprite.collide_mask(fish, rock):
            fish.kill()
    
    
    # Redraw the background
    screen.blit(background_image, (0, 0))
    
    # Update all of the sprites for animation
    all_sprites.update()
    
    # Redraw the all of the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    #screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()
