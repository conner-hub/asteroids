import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameactive = True
    while gameactive == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None)
        pygame.display.flip()


if __name__ == "__main__":
    main()
