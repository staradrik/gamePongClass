import pygame

def update_scores(player1_score, player2_score, placar_player1, placar_player2, font):
    if player2_score >= 3 or player1_score >= 3:
        return "gameover"

    return "jogo"

def update_ball(ball, ball_dir_x, ball_dir_y, player1, player2, hit_sound):
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dir_x *= -1
        hit_sound.play()

    ball.x += ball_dir_x
    ball.y += ball_dir_y

    if ball.x <= 0 or ball.x >= 1280:
        ball_dir_x *= -1

    if ball.y <= 0 or ball.y >= 720 - 15:
        ball_dir_y *= -1

    return ball, ball_dir_x, ball_dir_y

def update_players(player1, player2, ball, player1_velocidade):
    player1.y = max(0, min(720 - 150, player1.y))
    player1.y += player1_velocidade

    player2.y = max(0, min(720 - 150, ball.y - 75))

    return player1, player2
