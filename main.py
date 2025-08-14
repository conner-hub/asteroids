import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    
    #Initialize the clock.
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Initialize the player


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")
    gameactive = True
   
    dt = 0
    
    
    #Game loop
    while gameactive == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill((0,0,0), rect=None)
        
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                exit("Game over!")
        for bullet in shots:
            for asteroid in asteroids:
                if asteroid.collision(bullet) == True:
                    asteroid.split()
                    bullet.kill()

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()
