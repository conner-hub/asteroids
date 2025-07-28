import pygame
from constants import *
from player import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")
    gameactive = True
    
    #Initialize the clock.
    clock = pygame.time.Clock()
    #Initialize the player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #Game loop
    while gameactive == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
