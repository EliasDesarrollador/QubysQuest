import pygame
from entities import Entity

class Seal(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, width=60, height=40, speed=2, max_health=2)
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x + self.rect.width > 800:
            self.speed *= -1

    def draw(self, screen):
        # Dibujar cuerpo
        pygame.draw.rect(screen, (150, 75, 0), self.rect)
        # Dibujar barra de vida
        bar_width = self.rect.width
        bar_height = 5
        health_ratio = self.health / self.max_health
        bar_rect = pygame.Rect(self.rect.x, self.rect.y - bar_height - 2, int(bar_width * health_ratio), bar_height)
        pygame.draw.rect(screen, (255, 0, 0), bar_rect)
