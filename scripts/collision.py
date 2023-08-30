from scripts.settings import *
from scripts.sound import sound_player


def player_collision(player_collision):
    if player_collision.y <= 0:
        player_collision.y = 0
    elif player_collision.y >= HEIGHT - 150:
        player_collision.y = HEIGHT - 150


def ball_collision(ball_collision, ball_obj, player_collision, player_obj, enemy_collision, enemy_obj):
    if ball_collision.colliderect(player_collision) or ball_collision.colliderect(enemy_collision):
        ball_obj.directions[0] *= -1
        sound_player('assets/pong.wav')

    if ball_collision.x <= 0:
        enemy_obj.score += 1

        ball_collision.x = 600
        ball_obj.directions[0] *= -1

        sound_player('assets/pong.wav')
    elif ball_collision.x >= WIDTH - 15:
        player_obj.score += 1
        # placar_player1 = font.render(str(player_obj.score), True, 'white')

        ball_collision.x = 600
        ball_obj.directions[0] *= -1

    if ball_collision.y <= 0:
        ball_obj.directions[1] *= -1
        sound_player('assets/pong.wav')
    elif ball_collision.y >= HEIGHT - 15:
        ball_obj.directions[1] *= -1
        sound_player('assets/pong.wav')


def collision_master(player, player_rect, enemy, enemy_rect, ball, ball_rect):
    player_collision(player_rect)
    ball_collision(ball_rect, ball, player_rect, player, enemy_rect, enemy)
