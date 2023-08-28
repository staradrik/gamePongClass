import pygame

pygame.init()
pygame.font.init()

player1_img = pygame.image.load("assets/player1.png")
player1 = player1_img.get_rect()

player2_img = pygame.image.load("assets/player2.png")
player2 = player2_img.get_rect(right=1280)

ball_img = pygame.image.load("assets/ball.png")
ball = ball_img.get_rect(center=[1280 / 2, 720 / 2])

font = pygame.font.Font(None, 50)
