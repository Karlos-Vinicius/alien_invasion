class Settings:
    """Uma classe que contém as configuraçoes iniciais do jogo"""
    def __init__(self) -> None:
        """Configuraçoes iniciais do jogo"""
        # Configuraçoes de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuraçoes da espaçonave
        self.ship_speed = 1.5