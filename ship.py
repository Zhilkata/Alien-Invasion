import pygame


class Ship:
    """Independent module for the ship."""

    def __init__(self, ai_game):
        """Init the ship."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()

        # Initial position
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for the ship's position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position continuously."""
        # Updating the ship's value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect when ready
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship."""
        self.screen.blit(self.image, self.rect)
