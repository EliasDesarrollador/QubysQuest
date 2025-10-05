import pygame
from core.menu import Menu
import core.settings as settings
from levels import create_level1  # Solo nivel 1 por ahora


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.menu = Menu(screen)
        self.in_menu = True
        self.running = True

        # Nivel y jugador
        self.player = None
        self.enemies = []
        self.obstacles = []

    def run_level(self, player, enemies, obstacles):
        """Bucle básico del nivel 1 en pantalla completa"""
        level_running = True
        screen_width, screen_height = self.screen.get_size()

        # Posición inicial del jugador centrada
        player.x = screen_width // 2
        player.y = screen_height // 2

        while level_running:
            self.clock.tick(settings.FPS)
            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    level_running = False

            # Actualizar entidades
            player.update(keys)
            for enemy in enemies:
                enemy.update()

            # Dibujar
            self.screen.fill((0, 100, 255))  # fondo azul hielo
            player.draw(self.screen)
            for enemy in enemies:
                enemy.draw(self.screen)

            pygame.display.flip()

            # ESC para volver al menú
            if keys[pygame.K_ESCAPE]:
                level_running = False
                self.in_menu = True

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            if self.in_menu:
                selection = self.menu.get_selection(events)
                if selection == "Play":
                    # Crear nivel 1 con tamaño actual de pantalla
                    self.player, self.enemies, self.obstacles = create_level1(
                        self.screen.get_width(), self.screen.get_height()
                    )
                    self.in_menu = False
                    self.run_level(self.player, self.enemies, self.obstacles)

                elif selection == "Exit":
                    self.running = False

                # Dibujar menú
                self.menu.draw()
                pygame.display.flip()
                self.clock.tick(settings.FPS)

            else:
                # Por ahora dejamos vacío, la actualización se hace dentro de run_level
                pass
