import pygame

class EntanglementCrystal:
    def __init__(self, cooldown=5):
        self.cooldown = cooldown
        self.cooldown_timer = 0
        self.linked_enemies = []  # Para enlazar enemigos

    def activate(self, player, target):
        if self.cooldown_timer <= 0:
            # Intercambia posición con target
            player.rect.center, target.rect.center = target.rect.center, player.rect.center
            self.cooldown_timer = self.cooldown

            # Enlazar enemigos si es un enemigo
            if target.is_enemy:
                self.linked_enemies.append(target)

    def enemy_linked_check(self):
        # Si algún enemigo enlazado muere, mueren todos los demás
        alive = [e for e in self.linked_enemies if e.alive]
        if len(alive) < len(self.linked_enemies):
            for e in self.linked_enemies:
                if e.alive:
                    e.alive = False
            self.linked_enemies.clear()

    def update(self, dt):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt