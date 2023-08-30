import pygame

# inicializa pygame e fonte
pygame.init()
pygame.font.init()

# janela
display = pygame.display.set_mode((1280, 720))

# campo
campo_img = pygame.image.load('../assets/bg.png')
campo = campo_img.get_rect()

'''
    PLAYER 1:
    (0,0) = canto superior esquerdo
    30 = largura
    150 = altura
'''
player1_img = pygame.image.load('../assets/player1.png')
player1 = player1_img.get_rect()
# player1 = pygame.Rect(0, 0, 30, 150)
player1_velocidade = 6
player1_score = 0

'''
    PLAYER 2:
    (1250, 0) = canto superior direito (considerando largura)
    30 = largura
    150 = altura
'''
player2_img = pygame.image.load('../assets/player2.png')
player2 = player2_img.get_rect(right=1280)
# player2 = pygame.Rect(1250, 0, 30, 150)
player2_score = 0

'''
    BOLA:
    (600, 350) = centro da tela (considerando largura)
    30 = largura
    150 = altura
'''
ball_img = pygame.image.load('../assets/ball.png')
ball = ball_img.get_rect(center=[1280 / 2, 720 / 2])
# ball = pygame.Rect(600, 350, 15, 15)
ball_dir_x = 6
ball_dir_y = 6

# cria placares
font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, 'white')
placar_player2 = font.render(str(player2_score), True, 'white')

# define menu
menu_img = pygame.image.load('../assets/menu.png')
menu = menu_img.get_rect()
cena = 'menu'

# define gameover
gameover_img = pygame.image.load('../assets/gameover.png')
gameover = gameover_img.get_rect()

# define fade
fade_img = pygame.Surface((1280, 720)).convert_alpha()
fade = fade_img.get_rect()
fade_img.fill('black')
fade_alpha = 255

music = pygame.mixer.Sound('../assets/music.ogg')
music.play(-1)

fps = pygame.time.Clock()

# loop do jogo
loop = True
while loop:

    if cena == 'jogo':
        # eventos
        for event in pygame.event.get():
            # evento do 'X' de fechar
            if event.type == pygame.QUIT:
                loop = False

            # evento de controle do 'player1'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player1_velocidade = 6
                if event.key == pygame.K_w:
                    player1_velocidade = -6
                if event.key == pygame.K_SPACE:
                    player1_velocidade *= 100

        # game over
        if player2_score >= 3:
            cena = 'gameover'
            fade_alpha = 255
        if player1_score >= 3:
            cena = 'gameover'
            fade_alpha = 255

        # colisão da bola
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dir_x *= -1
            hit = pygame.mixer.Sound('../assets/pong.wav')
            hit.play()

        # colisão do player1
        if player1.y <= 0:
            player1.y = 0
        elif player1.y >= 720 - 150:
            player1.y = 720 - 150

        # colisão do player2
        '''if player2.y <= 0:
            player2.y = 0
        elif player2.y >= 720 - 150:
            player2.y = 720 - 150'''

        player1.y += player1_velocidade

        # colisão do eixo x da bola
        if ball.x <= 0:
            player2_score += 1
            placar_player2 = font.render(str(player2_score), True, 'white')

            ball.x = 600
            ball_dir_x *= -1
        elif ball.x >= 1280 - 15:
            player1_score += 1
            placar_player1 = font.render(str(player1_score), True, 'white')

            ball.x = 600
            ball_dir_x *= -1

        # colisão do eixo y da bola
        if ball.y <= 0:
            ball_dir_y *= -1
        elif ball.y >= 720 - 15:
            ball_dir_y *= -1

        ball.x += ball_dir_x
        ball.y += ball_dir_y

        player2.y = ball.y - 75

        # preenche a tela
        display.fill((0, 0, 0))

        # desenha os objetos
        display.blit(campo_img, campo)
        display.blit(player1_img, player1)
        display.blit(player2_img, player2)
        display.blit(ball_img, ball)
        # pygame.draw.rect(display, 'white', player1)
        # pygame.draw.rect(display, 'white', player2)
        # pygame.draw.circle(display, 'white', ball.center, 8)

        # desenha o placar
        display.blit(placar_player1, (500, 50))
        display.blit(placar_player2, (780, 50))

    elif cena == 'gameover':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    loop = False
                if event.key == pygame.K_r:
                    player1_score = 0
                    player2_score = 0
                    placar_player1 = font.render(str(player1_score), True, 'white')
                    placar_player2 = font.render(str(player2_score), True, 'white')
                    ball.x = 640
                    ball.y = 320
                    player1.y = 0
                    player2.y = 0
                    cena = 'jogo'

        if fade_alpha > 0:
            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)

        display.fill((0, 0, 0))
        display.blit(gameover_img, gameover)
        display.blit(fade_img, fade)

    elif cena == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'jogo'
                    fade_alpha = 255
                    start = pygame.mixer.Sound('../assets/start.wav')
                    start.play()
                if event.key == pygame.K_q:
                    loop = False

        display.fill((0, 0, 0))
        display.blit(menu_img, menu)

    # atualiza a tela
    fps.tick(60)
    pygame.display.flip()
