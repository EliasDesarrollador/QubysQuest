import pygame
from entities import Entity

class Penguin(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, width=50, height=50, speed=3, max_health=3)
        self.power_active = None
        self.intangible = False
        self.immortal_totem = False
        self.weight_multiplier = 1.0

    def update(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed

        self.rect.x += dx
        self.rect.y += dy

    def take_damage(self, amount):
        # Ignorar daño si es intangible o tiene totem de inmortalidad
        if self.intangible or self.immortal_totem:
            return
        super().take_damage(amount)

    def check_collision(self, enemies):
        """Verifica colisiones con enemigos y aplica daño si corresponde."""
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                self.take_damage(1)  # Cada colisión resta 1 de vida (ajustable)

    def draw(self, screen):
        # Dibujar a Quby
        pygame.draw.rect(screen, (0, 0, 255), self.rect)  # azul para Quby

        # Dibujar barra de vida roja sobre la cabeza
        bar_width = self.rect.width
        bar_height = 5
        health_ratio = self.health / self.max_health
        bar_rect = pygame.Rect(self.rect.x, self.rect.y - bar_height - 2, int(bar_width * health_ratio), bar_height)
        pygame.draw.rect(screen, (255, 0, 0), bar_rect)
