import pygame
from constants import *
from player import *

def main():
    pygame.init()
    
    #Initialize the clock.
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")
    gameactive = True
   
    #Initialize the player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    
    
    #Game loop
    while gameactive == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill((0,0,0), rect=None)
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
