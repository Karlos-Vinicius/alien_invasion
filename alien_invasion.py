import sys
import pygame


from settings import Settings


class AlienInvasion():
    """Um jogo curto sobre invasao alien. Bem parecido com space invaders!"""
    def __init__(self) -> None:
        """Inicializa as variáveis e o jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_height))
        pygame.display.set_caption("Space invaders 2.0")

    def run_game(self):
        """Inicializa o loop do jogo"""
        while True:
            # Observa eventos do teclado
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()

            # Redesenha a tela a cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)
            
            # Deixa a tela desenhada mais recente visível
            self.clock.tick(60)
            pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e o executa
    game = AlienInvasion()
    game.run_game()
