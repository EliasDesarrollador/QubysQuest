import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, max_health=100):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # color temporal
        self.rect = self.image.get_rect(center=(x, y))
        
        self.max_health = max_health
        self.health = max_health
        self.alive = True

    def take_damage(self, amount):
        if self.alive:
            self.health -= amount
            if self.health <= 0:
                self.die()

    def heal(self, amount):
        if self.alive:
            self.health += amount
            if self.health > self.max_health:
                self.health = self.max_health

    def die(self):
        self.alive = False
        # Aquí podés agregar animaciones de muerte o efectos
        self.kill()