import pygame
from entities import Entity

class Orca(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, width=100, height=50, speed=4, max_health=5)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x + self.rect.width > 800:
            self.speed *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        # Barra de vida
        bar_width = self.rect.width
        bar_height = 5
        health_ratio = self.health / self.max_health
        bar_rect = pygame.Rect(self.rect.x, self.rect.y - bar_height - 2, int(bar_width * health_ratio), bar_height)
        pygame.draw.rect(screen, (255, 0, 0), bar_rect)
