import pygame


class SchrodingerHat:
    def __init__(self, duration=5):
        self.duration = duration   # Tiempo que dura el efecto
        self.active = False
        self.timer = 0

    def activate(self, player):
        self.active = True
        self.timer = self.duration
        player.immortal_totem = True  # El totem de inmortalidad activa

    def update(self, dt, player):
        if self.active:
            self.timer -= dt
            if self.timer <= 0:
                self.active = False
                player.immortal_totem = False