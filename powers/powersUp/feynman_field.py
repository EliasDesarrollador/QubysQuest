import pygame

class FeynmanField:
    def __init__(self, duration=3):
        self.duration = duration
        self.active = False
        self.timer = 0
        self.positions = []  # Guarda posiciones recientes

    def activate(self, player):
        self.active = True
        self.timer = self.duration
        self.positions = []

    def update(self, dt, player):
        if self.active:
            # Guardar la posición cada frame
            self.positions.append(player.rect.center)
            # Mantener solo los últimos 3 segundos (aprox. 60 fps)
            if len(self.positions) > int(3 * 60):
                self.positions.pop(0)

            self.timer -= dt
            if self.timer <= 0:
                # Teletransportar a la posición de hace 3 segundos
                if self.positions:
                    player.rect.center = self.positions[0]
                self.active = False
                self.positions = []