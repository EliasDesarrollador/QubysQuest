import pygame
import core.settings as settings

class SettingsMenu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        # Colores
        self.bg_color = (0, 0, 128)  # Azul
        self.text_color = (255, 255, 255)  # Blanco
        self.bar_bg_color = (100, 100, 150)
        self.bar_fill_color = (0, 200, 255)

        # Fuente
        self.font = pygame.font.Font(None, 60)
        self.small_font = pygame.font.Font(None, 40)

        # Volumen inicial
        self.volume = getattr(game, "volume", 0.5)

        # Barra de volumen
        self.bar_width = 400
        self.bar_height = 25
        self.bar_x = (self.screen.get_width() - self.bar_width) // 2
        self.bar_y = 200

        self.dragging = False

        # Opciones
        self.other_options = ["Controles", "Volver"]
        self.selected = 0

        # Control info
        self.controls_info = [
            "Mover: WASD",
            "Seleccionar: Enter / Click",
            "Menu: Esc"
        ]

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self._bar_rect().collidepoint(event.pos):
                            self.dragging = True
                            self._update_volume(event.pos[0])
                        else:
                            selection = self._check_option_click(event.pos)
                            if selection == "Volver":
                                return
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.dragging = False
                elif event.type == pygame.MOUSEMOTION and self.dragging:
                    self._update_volume(event.pos[0])

            self._handle_keyboard()
            self.draw()
            pygame.display.flip()
            clock.tick(60)

    def draw(self):
        self.screen.fill(self.bg_color)

        # Título
        title_text = self.font.render("Configuración", True, self.text_color)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title_text, title_rect)

        # Volumen centrado
        vol_text = self.small_font.render("Volumen", True, self.text_color)
        vol_rect = vol_text.get_rect(center=(self.screen.get_width() // 2, self.bar_y - 40))
        self.screen.blit(vol_text, vol_rect)

        pygame.draw.rect(self.screen, self.bar_bg_color, self._bar_rect())
        fill_width = int(self.bar_width * self.volume)
        fill_rect = pygame.Rect(self.bar_x, self.bar_y, fill_width, self.bar_height)
        pygame.draw.rect(self.screen, self.bar_fill_color, fill_rect)

        # Knob
        knob_x = self.bar_x + fill_width
        knob_y = self.bar_y + self.bar_height // 2
        pygame.draw.circle(self.screen, (255, 255, 255), (knob_x, knob_y), 10)

        # Porcentaje
        vol_percent = self.small_font.render(f"{int(self.volume * 100)}%", True, self.text_color)
        vol_percent_rect = vol_percent.get_rect(center=(self.screen.get_width() // 2, self.bar_y + 50))
        self.screen.blit(vol_percent, vol_percent_rect)

        # Otras opciones a los lados
        spacing = 300
        y_pos = self.bar_y + 150
        for i, opt in enumerate(self.other_options):
            x_pos = (self.screen.get_width() // 2) - spacing + (i * spacing)
            color = self.text_color
            text = self.small_font.render(opt, True, color)
            rect = text.get_rect(center=(x_pos, y_pos))
            self.screen.blit(text, rect)

        # Mostrar controles si seleccionado
        if self.selected == 0:  # Controles
            for idx, line in enumerate(self.controls_info):
                info_text = self.small_font.render(line, True, self.text_color)
                info_rect = info_text.get_rect(left=50, top=y_pos + 50 + idx * 40)
                self.screen.blit(info_text, info_rect)

    def _update_volume(self, mouse_x):
        rel_x = mouse_x - self.bar_x
        self.volume = max(0, min(1, rel_x / self.bar_width))
        if hasattr(self.game, "volume"):
            self.game.volume = self.volume
        pygame.mixer.music.set_volume(self.volume)

    def _bar_rect(self):
        return pygame.Rect(self.bar_x, self.bar_y, self.bar_width, self.bar_height)

    def _check_option_click(self, pos):
        spacing = 300
        y_pos = self.bar_y + 150
        for i, opt in enumerate(self.other_options):
            x_pos = (self.screen.get_width() // 2) - spacing + (i * spacing)
            rect = self.small_font.render(opt, True, self.text_color).get_rect(center=(x_pos, y_pos))
            if rect.collidepoint(pos):
                return opt  # retorna la opción clickeada

    def _handle_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.volume = max(0, self.volume - 0.01)
        elif keys[pygame.K_RIGHT]:
            self.volume = min(1, self.volume + 0.01)
        if hasattr(self.game, "volume"):
            self.game.volume = self.volume