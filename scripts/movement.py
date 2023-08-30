def player_movement(player_collision, player_speed):
    player_collision.y += player_speed


def ball_movement(ball_collision, ball_speeds):
    ball_collision.x += ball_speeds[0]
    ball_collision.y += ball_speeds[1]


def enemy_movement(enemy_collision, ball_collision):
    enemy_collision.y = ball_collision.y - 75


def movement_master(player_rect, player_speed, enemy_rect, ball_rect, ball_dir):
    player_movement(player_rect, player_speed)
    ball_movement(ball_rect, ball_dir)
    enemy_movement(enemy_rect, ball_rect)