from typing import Self
import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.surface.Surface):
        pass

    def update(self, dt: float):
        pass

    def collision(self, other: Self):
        return self.radius + other.radius >= other.position.distance_to(self.position)
