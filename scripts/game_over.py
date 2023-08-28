import pygame

def game_over_logic(game_state):
    if game_state.fade_alpha > 0:
        game_state.fade_alpha -= 10
        game_state.fade_img.set_alpha(game_state.fade_alpha)

    game_state.display.fill((0, 0, 0))
    game_state.display.blit(game_state.gameover_img, game_state.gameover)
    game_state.display.blit(game_state.fade_img, game_state.fade)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_state.player1_score = 0
                game_state.player2_score = 0
                game_state.placar_player1 = game_state.font.render(str(game_state.player1_score), True, "white")
                game_state.placar_player2 = game_state.font.render(str(game_state.player2_score), True, "white")

                game_state.player1.y = 0
                game_state.player2.y = 0
                game_state.ball.x = 640
                game_state.ball.y = 320
                return True, False

    pygame.display.flip()
    return False, False
