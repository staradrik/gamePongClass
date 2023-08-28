import pygame

def handle_events(player1, player1_velocidade):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.y += 10

            if event.key == pygame.K_s:
                player1_velocidade = 6
            elif event.key == pygame.K_w:
                player1_velocidade = -6

    return True
