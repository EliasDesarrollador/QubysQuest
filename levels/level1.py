# levels/level1.py
from entities import Penguin, Seal, Orca, Jellyfish

def create_level(screen_width, screen_height):
    # Jugador
    player = Penguin(screen_width//2, screen_height//2)

    # Enemigos
    enemies = [
        Seal(100, 100),
        Seal(600, 150),
        Orca(50, 400),
        Jellyfish(300, 450)
    ]

    # Obstáculos
    obstacles = []

    return player, enemies, obstacles
