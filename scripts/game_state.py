import pygame

class GameState:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.display = pygame.display.set_mode((1280, 720))

        self.player1_img = pygame.image.load("assets/player1.png")
        self.player1 = self.player1_img.get_rect()

        self.player2_img = pygame.image.load("assets/player2.png")
        self.player2 = self.player2_img.get_rect(right=1280)

        self.ball_img = pygame.image.load("assets/ball.png")
        self.ball = self.ball_img.get_rect(center=[1280 / 2, 720 / 2])

        self.font = pygame.font.Font(None, 50)

        self.campo_img = pygame.image.load("assets/bg.png")
        self.campo = self.campo_img.get_rect()

        self.gameover_img = pygame.image.load("assets/gameover.png")
        self.gameover = self.gameover_img.get_rect()

        self.menu_img = pygame.image.load("assets/menu.png")
        self.menu = self.menu_img.get_rect()

        self.fade_img = pygame.Surface((1280, 720)).convert_alpha()
        self.fade = self.fade_img.get_rect()
        self.fade_img.fill("black")
        self.fade_alpha = 255

        self.music = pygame.mixer.Sound("assets/music.ogg")
        self.music.play(-1)

        self.player1_score = 0
        self.player2_score = 0

        self.player1_velocidade = 6

        self.ball_dir_x = 6
        self.ball_dir_y = 6

        self.placar_player1 = self.font.render(str(self.player1_score), True, "white")
        self.placar_player2 = self.font.render(str(self.player2_score), True, "white")

        self.cena = "menu"

        self.fps = pygame.time.Clock()
