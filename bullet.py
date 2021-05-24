import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet class for player's ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the player's position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create a bullet at the top-left at then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet's position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet as if it's flying."""
        # Update decimal position
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
