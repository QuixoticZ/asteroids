# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers= (updateable,drawable)
    Asteroid.containers= (updateable,drawable,asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable,drawable,shots)
    asteroidfield = AsteroidField()
    dt = 0
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        updateable.update(dt)
        for a in asteroids:
            if a.collision(player) == True:
                sys.exit("Game Over!")
            for s in shots:
                if a.collision(s) == True:
                    s.kill()
                    a.split()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()