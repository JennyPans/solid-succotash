import pygame
from pygame.color import Color


class Constants:
    """
    Contient toutes les constantes du jeu
    """

    WIDTH = 1024
    HEIGHT = 576
    SIZE = (WIDTH, HEIGHT)
    FLAGS = pygame.RESIZABLE
    BOX_WIDTH = 64
    BOX_HEIGHT = 64
    BOX_COLOR = Color(255, 255, 255)
    BG_COLOR = Color(50, 50, 125)
    MS_PER_TICK = 1 / 60
