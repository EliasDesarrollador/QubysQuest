import pygame
from core.game import Game

def main():
    pygame.init()
    
    # Inicializar pantalla en FULLSCREEN
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Quby's Quest: The Entangled Rescue")

    game = Game(screen)
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()
