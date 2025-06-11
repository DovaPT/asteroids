import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(30, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60.0)


if __name__ == "__main__":
    main()
