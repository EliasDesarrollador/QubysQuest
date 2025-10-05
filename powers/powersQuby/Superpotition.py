import pygame

class Superposition:
    def __init__(self, duration=3, cooldown=5):
        self.active = False
        self.duration = duration       # Duración en segundos
        self.cooldown = cooldown       # Cooldown en segundos
        self.timer = 0
        self.cooldown_timer = 0

    def activate(self, player):
        if not self.active and self.cooldown_timer <= 0:
            self.active = True
            self.timer = self.duration
            player.intangible = True   # Quby se vuelve intocable

    def update(self, dt, player):
        if self.active:
            self.timer -= dt
            if self.timer <= 0:
                self.active = False
                self.cooldown_timer = self.cooldown
                player.intangible = False

        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt