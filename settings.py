class Settings:
    """Uma classe que contém as configuraçoes iniciais do jogo"""
    def __init__(self) -> None:
        """Configuraçoes iniciais do jogo"""
        # Configuraçoes de tela
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Configuraçoes da espaçonave
        self.ship_speed = 3

        # Configuraçoes do projétil
        self.bullet_speed = 7
        self.bullet_widht = 5
        self.bullet_height = 14
        self.bullet_bg_color = (60, 60, 60)
        self.bullet_max_numbers = 7
