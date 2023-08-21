import sys
import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion():
    """Um jogo curto sobre invasao alien. Bem parecido com space invaders!"""
    def __init__(self) -> None:
        """Método que gerencia o comportamento do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.running_game = True

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_height()
        self.settings.screen_width = self.screen.get_width()
        pygame.display.set_caption("Space Invaders 2.0")

        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()


    def _check_events(self):
        """Responde as teclas pressionadas e eventos do mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running_game = False

            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)

            elif event.type == pygame.KEYUP:
                self._check_key_up(event)


    def _check_key_down(self, event):
        # Verificando qual tecla foi pressionada
        if event.key == pygame.K_RIGHT:
            # Move a espaçonave para a direita
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            # Move a espaçonave para a esquerda
            self.ship.moving_left = True

        elif event.key == pygame.K_UP:
            # Move a espaçonave para cima
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            # Move a espaçonave para baixo
            self.ship.moving_down = True

        elif event.key == pygame.K_q:
            # Sair do jogo
            self.running_game = False

        elif event.key == pygame.K_SPACE:
            # Atira projéteis na tela
            self._fire_bullet()


    def _check_key_up(self, event):
        # Verificando qual tecla deixou de ser pressionada
        if event.key == pygame.K_LEFT:
            # Para de mover a espaçonave para a esquerda
            self.ship.moving_left = False

        if event.key == pygame.K_RIGHT:
            # Para de mover a espaçonave para a direita
            self.ship.moving_right = False

        if event.key == pygame.K_UP:
            # Para de mover a espaçonave para cima
            self.ship.moving_up = False

        if event.key == pygame.K_DOWN:
            # Para de mover a espaçonave para baixo
            self.ship.moving_down = False
    

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)


    def _update_screen(self):
        """Atualiza as imagens na tela"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.bullet.update()

        for bullet in self.bullet.sprites():
            """Desenha cada projétil na tela"""
            bullet.blitme()

        pygame.display.flip()


    def run_game(self):
        """Inicializa o loop do jogo"""
        while self.running_game:
            # Observa eventos do teclado
            self._check_events()
            self.ship.update()

            # Redesenha a tela a cada passagem pelo loop
            self._update_screen()
            
            # Taxa de 60 quadros por segundo
            self.clock.tick(60)
        
        # Fecha o jogo
        sys.exit()


if __name__ == '__main__':
    # Cria uma instância do jogo e executa-o
    game = AlienInvasion()
    game.run_game()
