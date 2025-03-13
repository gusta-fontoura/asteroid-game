import pygame
from constants import *
from player import Player


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


    while True:
        dt = fps.tick(60)/1000
        screen.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()

        

if __name__ == "__main__":
    main()
