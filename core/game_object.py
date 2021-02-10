import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from constants import Constants


class GameObject:
    """
    Base pour tous les objets mobiles
    """

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0.1, 0)
        self.speed = Vector2(0, 0)

    def update(self):
        self.velocity += self.speed
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, Constants.BOX_COLOR,
                         Rect(self.position.x, self.position.y, Constants.BOX_WIDTH, Constants.BOX_HEIGHT))
