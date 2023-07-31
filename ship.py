import pygame


class Ship:
    """Classe responsável pela nave"""
    def __init__(self, central_game) -> None:
        """Inicializando a espaçonave e suas configuraçoes iniciais"""
        self.screen = central_game.screen
        self.screen_rect = central_game.screen.get_rect()
        self.size = (100, 100)
        self.rotate = 180

        # Sobe a imagem da espaçonave e obtém seu rect
        self.image_incorrect_size = pygame.image.load('images/ship_official.bmp')
        self.image_incorrect_rotate = pygame.transform.scale(self.image_incorrect_size, self.size)
        self.image = pygame.transform.rotate(self.image_incorrect_rotate, self.rotate)
        self.rect = self.image.get_rect()

        # Começa cada espaçona no centro inferior da imagem
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha a nave em sua localizaçao atual"""
        self.screen.blit(self.image, self.rect)
