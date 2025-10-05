import pygame

class HiggsParticle:
    def __init__(self, duration=5):
        self.duration = duration
        self.active = False
        self.timer = 0

    def activate(self, player, increase=True):
        self.active = True
        self.timer = self.duration
        if increase:
            player.weight_multiplier = 2.0  # Quby cae más rápido y aplasta cosas
        else:
            player.weight_multiplier = 0.5  # Quby flota más y salta más alto

    def update(self, dt, player):
        if self.active:
            self.timer -= dt
            if self.timer <= 0:
                self.active = False
                player.weight_multiplier = 1.0  # Volver al peso normal
