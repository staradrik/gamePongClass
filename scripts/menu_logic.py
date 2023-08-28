import pygame

def menu_logic(game_state):
    if game_state.fade_alpha > 0:
        game_state.fade_alpha -= 10
        game_state.fade_img.set_alpha(game_state.fade_alpha)

    game_state.display.fill((0, 0, 0))
    game_state.display.blit(game_state.menu_img, game_state.menu)
    game_state.display.blit(game_state.fade_img, game_state.fade)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True, False
            if event.key == pygame.K_q:
                return False, True

    pygame.display.flip()
    return False, False
