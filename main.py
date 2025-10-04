# Punto de entrada del juego
# Importamos la clase Game que contiene el loop principal
from core.game import Game

# Función principal
def main():
    # Creamos una instancia del juego
    game = Game()
    # Ejecutamos el loop principal
    game.run()

# Esto hace que main() se ejecute solo si corremos el archivo directamente
if __name__ == "__main__":
    main()
