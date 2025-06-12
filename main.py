import pygame

import asteroidfield
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatables, drawables, asteroids)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, drawables, updatables)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        screen.fill(pygame.Color(30, 0, 0))
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
        dt = clock.tick(60.0) / 1000


if __name__ == "__main__":
    main()
