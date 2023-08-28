import pygame
from scripts.game_start import start_game
from scripts.game_logic import update_scores, update_ball, update_players
from scripts.event_handling import handle_events
from scripts.game_over import game_over_logic
from scripts.menu_logic import menu_logic

game_state = start_game()

# Definición de las variables de menú
menu_img = pygame.image.load("assets/menu.png")
menu = menu_img.get_rect()

while True:
    if game_state.cena == "jogo":
        loop = handle_events(game_state.player1, game_state.player1_velocidade)

        game_state.cena = update_scores(game_state.player1_score, game_state.player2_score, game_state.placar_player1, game_state.placar_player2, game_state.font)

        game_state.ball, game_state.ball_dir_x, game_state.ball_dir_y = update_ball(game_state.ball, game_state.ball_dir_x, game_state.ball_dir_y, game_state.player1, game_state.player2, pygame.mixer.Sound("assets/pong.wav"))

        game_state.player1, game_state.player2 = update_players(game_state.player1, game_state.player2, game_state.ball, game_state.player1_velocidade)

        game_state.display.fill((0, 0, 0))

        game_state.display.blit(game_state.campo_img, game_state.campo)
        game_state.display.blit(game_state.player1_img, game_state.player1)
        game_state.display.blit(game_state.player2_img, game_state.player2)
        game_state.display.blit(game_state.ball_img, game_state.ball)
        game_state.display.blit(game_state.placar_player1, (500, 50))
        game_state.display.blit(game_state.placar_player2, (780, 50))
        game_state.display.blit(game_state.fade_img, game_state.fade)

    elif game_state.cena == "gameover":
        loop, loop = game_over_logic(game_state)

    elif game_state.cena == "menu":
        loop, loop = menu_logic(game_state)

    game_state.fps.tick(60)
    pygame.display.flip()
