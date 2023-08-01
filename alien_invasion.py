import sys
import pygame


from settings import Settings
from ship import Ship


class AlienInvasion():
    """Um jogo curto sobre invasao alien. Bem parecido com space invaders!"""
    def __init__(self) -> None:
        """Método que gerencia o comportamento do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.running_game = True

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders 2.0")

        self.ship = Ship(self)

    def run_game(self):
        """Inicializa o loop do jogo"""
        while self.running_game:
            # Observa eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False

            # Redesenha a tela a cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # Deixa a tela desenhada mais recente visível
            self.clock.tick(60)
            pygame.display.flip()
        
        # Fecha o jogo
        sys.exit()

if __name__ == '__main__':
    # Cria uma instância do jogo e o executa
    game = AlienInvasion()
    game.run_game()
