import pygame
import core.settings as settings
from core.settings_menu import SettingsMenu


class Menu:
    def __init__(self, screen, game=None):
        self.screen = screen
        self.game = game  # referencia al juego (para pasar a SettingsMenu)
        self.font = pygame.font.Font(None, 50)
        self.options = ["Play", "Tutorial", "Settings", "Exit"]
        self.selected = 0

        # Colores
        self.color_inactive = settings.COLOR_MENU_INACTIVE
        self.color_active = settings.COLOR_MENU_ACTIVE

        # Separación vertical relativa de los botones
        self.spacing_ratio = 0.1  # 10% del alto de la pantalla

        # Para detectar pulsación única de teclado
        self.key_pressed = False

        # Inicializamos button_rects para evitar errores
        self.button_rects = []

    def draw(self):
        # Fondo
        self.screen.fill(settings.COLOR_BG)

        # Tamaño actual de pantalla
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        spacing = screen_height * self.spacing_ratio

        # Ajustar tamaño de fuente según alto de pantalla (opcional)
        font_size = int(screen_height * 0.08)
        self.font = pygame.font.Font(None, font_size)

        # Dibujar botones centrados y guardar rectángulos para mouse
        self.button_rects = []
        for i, option in enumerate(self.options):
            color = self.color_active if i == self.selected else self.color_inactive
            text = self.font.render(option, True, color)
            rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + (i - len(self.options)//2) * spacing))
            self.screen.blit(text, rect)
            self.button_rects.append(rect)

    def move_up(self):
        self.selected = (self.selected - 1) % len(self.options)

    def move_down(self):
        self.selected = (self.selected + 1) % len(self.options)

    def get_selection(self, events):
        mouse_pos = pygame.mouse.get_pos()

        # Cambiar selección si el mouse está sobre un botón
        for i, rect in enumerate(self.button_rects):
            if rect.collidepoint(mouse_pos):
                self.selected = i

        keys = pygame.key.get_pressed()
        # Subir/bajar solo una vez por pulsación
        if keys[pygame.K_UP] and not self.key_pressed:
            self.move_up()
            self.key_pressed = True
        elif keys[pygame.K_DOWN] and not self.key_pressed:
            self.move_down()
            self.key_pressed = True
        elif not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            self.key_pressed = False

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return self._handle_selection()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return self._handle_selection()

        return None

    def _handle_selection(self):
        selected_option = self.options[self.selected]
        if selected_option == "Settings":
            settings_menu = SettingsMenu(self.screen, self.game)
            settings_menu.run()
            return None  # No cerrar el menú principal
        else:
            return selected_option
