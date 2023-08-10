import pygame


class Ship:
    """Classe responsável pela nave"""
    def __init__(self, central_game) -> None:
        """Inicializando a espaçonave e suas configuraçoes iniciais"""
        self.screen = central_game.screen
        self.screen_rect = central_game.screen.get_rect()
        self.size = (100, 100)
        self.rotate = 180
        self.settings = central_game.settings

        # Sobe a imagem da espaçonave e obtém seu rect
        self.image_incorrect_size = pygame.image.load('images/ship_official.bmp')
        self.image_incorrect_rotate = pygame.transform.scale(self.image_incorrect_size, self.size)
        self.image = pygame.transform.rotate(self.image_incorrect_rotate, self.rotate)
        self.rect = self.image.get_rect()

        # Começa cada espaçona no centro inferior da imagem
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um float para a posiçao horizontal exata da espaçonave
        self.x = float(self.rect.y)

        # Armazxena um float para a posiçao vertical exata da espaçonave
        self.y = float(self.rect.y)

        # Flag de movimentaçao, começa com uma espaçonave que não está se movento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        """Desenha a nave em sua localizaçao atual"""
        self.screen.blit(self.image, self.rect)

    
    def update(self):
        """Avalia se para ou se deve movimentar a nave"""
        if self.moving_right and self.screen_rect.right > self.rect.right:
            self.x += self.settings.ship_speed

        elif self.moving_left and self.screen_rect.left < self.rect.left:
            self.x -= self.settings.ship_speed
            
        if self.moving_up and self.screen_rect.top < self.rect.top:
            self.y -= self.settings.ship_speed

        elif self.moving_down and self.screen_rect.bottom > self.rect.bottom:
            self.y += self.settings.ship_speed

        # Atualiza o objeto rect de self.x
        self.rect.x = self.x

        # Atualiza o objeto rect de self.y
        self.rect.y = self.y
