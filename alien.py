import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Single alien class"""

    def __init__(self, ai_game):
        """Init the alien"""
        super().__init__()
        self.screen = ai_game.screen

        # Load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()

        # Spawn alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing position
        self.x = float(self.rect.x)