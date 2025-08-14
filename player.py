import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cd = 0
    # in the player class
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        vector = pygame.Vector2(0,1).rotate(self.rotation)
        velocity = vector * PLAYER_SHOOT_SPEED
        bullet = Shot(self.position.x, self.position.y, velocity)
        self.shoot_cd = 0.3
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt-1)
        if keys[pygame.K_d]:
            self.rotate(dt+1)
        if keys[pygame.K_w]:
            self.move(dt+1)
        if keys[pygame.K_s]:
            self.move(dt-1)
        if keys[pygame.K_SPACE]:
            if self.shoot_cd > 0:
                return
            else:
                self.shoot()
        self.shoot_cd -= dt
