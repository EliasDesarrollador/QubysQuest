
# core/game.py
# Aquí definimos la clase Game que maneja todo el juego

import pygame
from core.settings import ANCHO, ALTO, FPS, AZUL  # importamos configuraciones globales

class Game:
    def __init__(self):
        # Inicializamos Pygame
        pygame.init()
        
        # Creamos la ventana
        self.screen = pygame.display.set_mode(( ANCHO, ALTO))
        pygame.display.set_caption("Quby's Quest: The Entangled Rescue")
        
        # Reloj para controlar los FPS
        self.clock = pygame.time.Clock()
        
        # Flag para saber si el juego sigue corriendo
        self.running = True

    # Loop principal del juego
    def run(self):
        while self.running:
            # 1️⃣ Manejo de eventos (teclado, cerrar ventana, etc.)
            self.handle_events()
            # 2️⃣ Actualizar la lógica del juego (jugador, enemigos, físicas, poderes)
            self.update()
            # 3️⃣ Dibujar todo en pantalla
            self.draw()
            # Limitamos los FPS
            self.clock.tick(FPS)
        # Cuando termina el loop, cerramos Pygame
        pygame.quit()

    # Función para manejar eventos
    def handle_events(self):
        for event in pygame.event.get():
            # Si el jugador cierra la ventana
            if event.type == pygame.QUIT:
                self.running = False

    # Función para actualizar la lógica del juego
    def update(self):
        # TODO: aquí luego agregaremos Quby, enemigos, colisiones y poderes
        pass

    # Función para dibujar todo en pantalla
    def draw(self):
        # Rellenamos el fondo con azul oscuro
        self.screen.fill(AZUL)
        # Actualizamos la pantalla
        pygame.display.flip()

