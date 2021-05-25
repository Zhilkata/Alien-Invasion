import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Single alien class"""

    def __init__(self, ai_game):
        """Init the alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()

        # Spawn alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is colliding with screen's edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x