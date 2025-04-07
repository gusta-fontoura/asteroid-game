from circleshape import CircleShape
from constants import *
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, all_sprites, asteroids_group):
        super().__init__(x, y, radius)
        self.all_sprites = all_sprites
        self.asteroids_group = asteroids_group

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, self.all_sprites, self.asteroids_group)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius,self.all_sprites, self.asteroids_group)

            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2

            self.all_sprites.add(asteroid1, asteroid2)
            self.asteroids_group.add(asteroid1, asteroid2)
