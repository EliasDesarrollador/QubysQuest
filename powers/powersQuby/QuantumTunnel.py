import pygame

class QuantumTunnel:
    def __init__(self, range=200, cooldown=5):
        self.range = range            # Máximo alcance del teletransporte
        self.cooldown = cooldown
        self.cooldown_timer = 0

    def activate(self, player, target_pos):
        if self.cooldown_timer <= 0:
            # Limitar rango
            dx = target_pos[0] - player.rect.centerx
            dy = target_pos[1] - player.rect.centery
            distance = (dx**2 + dy**2) ** 0.5
            if distance > self.range:
                factor = self.range / distance
                target_pos = (
                    player.rect.centerx + dx * factor,
                    player.rect.centery + dy * factor
                )

            player.rect.center = target_pos
            self.cooldown_timer = self.cooldown

    def update(self, dt):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt