import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit
from shot import Shot
#source venv/bin/activate

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    #grouping
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2,PLAYER_RADIUS)


    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill('black')
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        for obj in asteroids:
            if player.check_collision(obj) == True:
                print("Game Over!")
                exit()

        for a in asteroids:
            for s in shots:
                if a.check_collision(s) == True:
                    a.split()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()