
#Punto de entrada del juego 
#importamos la clase Game  que contiene el loop principal
from core.game import Game

#Funcion principal
    def main():
 #Creamos una instancia  del juego 
    game  = Game()
  #EJecutamos el loop principal 
    game.run()
  #Esto hace que main () se  ejecute  solo si corremos el archivo correctamente
    if __name__ == "__main__":
        main() 