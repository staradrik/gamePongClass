import pygame
from scripts.actors import Player, Enemy, Ball
from scripts.collision import collision_master
from scripts.movement import movement_master
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *


class Game(Scene):
    def __init__(self, font):
        super().__init__()

        self.player = Player()
        self.enemy = Enemy()
        self.ball = Ball()

        self.font = font

        self.bg = Obj('assets/bg.png', self.all_sprites)

        self.player_sprite = Obj(self.player.sprite, self.all_sprites)

        self.enemy_sprite = Obj(self.enemy.sprite, self.all_sprites)
        self.enemy_sprite.rect = self.enemy_sprite.image.get_rect(right = WIDTH)  # override de método do Obj

        self.ball_sprite = Obj(self.ball.sprite, self.all_sprites)
        self.ball_sprite.rect = self.ball_sprite.image.get_rect(center = [WIDTH / 2, HEIGHT / 2])  # override de método do Obj

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.player.velocidade = 6
            if event.key == pygame.K_w:
                self.player.velocidade = -6

    def update(self):
        print(self.enemy.score)
        collision_master(self.player, self.player_sprite.rect,
                         self.enemy, self.enemy_sprite.rect,
                         self.ball, self.ball_sprite.rect)

        movement_master(self.player_sprite.rect, self.player.velocidade,
                        self.enemy_sprite.rect,
                        self.ball_sprite.rect, self.ball.directions)

        self.display.blit(self.font.render(str(self.player.score), True, 'white'), (500, 50))
        self.display.blit(self.font.render(str(self.enemy.score), True, 'white'), (780, 50))

        if self.enemy.score == 1 or self.player.score == 3:
            self.active = False
