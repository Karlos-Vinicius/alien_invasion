import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Classe que gerencia os projéteis disparados"""
    def __init__(self, other_class) -> None:
        """Cria um objeto bullet na posiçao atual da nave"""
        super().__init__()

        self.screen = other_class.screen
        self.settings = other_class.settings
        self.color = self.settings.bullet_bg_color
        self.image = pygame.image.load("images/bullet.png")

        # Cria um bullet rect e, em seguida, define a posiçao correta
        self.rect = self.image.get_rect()
        self.rect.midtop = other_class.ship.rect.midtop

        # Armazena a posiçao atual do projétil
        self.y = float(self.rect.y)


    def update(self):
        """Desloca o projétil verticalmente"""
        # Desloca o projétil no eixo y
        self.y -= self.settings.bullet_speed

        # Atualiza a posiçao do rect
        self.rect.y = self.y


    def draw_bullet(self):
        """Desenha o objeto bullet na tela"""
        pygame.draw.rect(self.screen, self.rect) 


    def blitme(self):
        self.screen.blit(self.image, self.rect)
