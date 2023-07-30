import sys
import pygame


class AlienInvasion():
    """Um jogo curto sobre invasao alien. Bem parecido com space invaders!"""
    def __init__(self) -> None:
        """Inicializa as variáveis e o jogo"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space invaders 2.0")

    def run_game(self):
        """Inicializa o loop do jogo"""
        while True:
            # Observa eventos do teclado
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
            
            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e o executa
    game = AlienInvasion()
    game.run_game()
