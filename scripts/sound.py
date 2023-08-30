import pygame


def sound_player(sound, *args):
    pygame.mixer.Sound(sound).play(*args)