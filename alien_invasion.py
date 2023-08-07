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


    def _check_events(self):
        """Responde as teclas pressionadas e eventos do mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        """Atualiza as imagens na tela"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


    def run_game(self):
        """Inicializa o loop do jogo"""
        while self.running_game:
            # Observa eventos do teclado
            self._check_events()

            # Redesenha a tela a cada passagem pelo loop
            self._update_screen()

            # Taxa de 60 quadros por segundo
            self.clock.tick(60)
        
        # Fecha o jogo
        sys.exit()


if __name__ == '__main__':
    # Cria uma instância do jogo e o executa
    game = AlienInvasion()
    game.run_game()
