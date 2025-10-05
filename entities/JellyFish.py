import pygame
import random
from entities import Entity

class Jellyfish(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, width=40, height=40, speed=1, max_health=1)
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x < 0 or self.rect.x + self.rect.width > 800:
            self.direction *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 255), self.rect)
        # Barra de vida
        bar_width = self.rect.width
        bar_height = 4
        health_ratio = self.health / self.max_health
        bar_rect = pygame.Rect(self.rect.x, self.rect.y - bar_height - 2, int(bar_width * health_ratio), bar_height)
        pygame.draw.rect(screen, (255, 0, 0), bar_rect)

