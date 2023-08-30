import pygame
from scripts.obj import Obj
from scripts.settings import *


class Player:
    def __init__(self, velocidade = 6):
        self.sprite = 'assets/player1.png'
        self.velocidade = velocidade
        self.score = 0


class Enemy:
    def __init__(self):
        self.sprite = 'assets/player2.png'
        self.score = 0


class Ball:
    def __init__(self):
        self.sprite = 'assets/ball.png'
        self.directions = [6, 6]  # (x, y)
