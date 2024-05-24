import sys

import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random

pygame.init() # Driver function

# Constant
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
TITLE_SIZE = 32
BLACK = (0,0,0)
WHITE = (255,255,255)

# Main screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("PACMAN GAME")

def main():
    running = True
    clock = pygame.time.Clock() # Create object to help keep track of time

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit() # System Exit with a status of 0

if __name__ == "__main__":
    main()

