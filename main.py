import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.get_init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    color = (0,0,0)
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    # must be declarated before Player instance
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    asteroids = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable, all_sprites, asteroids_group)
    asteroid_field = AsteroidField(all_sprites, asteroids_group)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        dt = fps.tick(60)/1000
        screen.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        
        for obj in asteroids:
            if obj.collision(player) == True:
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
        
        pygame.display.flip()

        

if __name__ == "__main__":
    main()
