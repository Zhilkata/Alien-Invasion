class GameStats:
    """Track stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Init stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Init dynamic stats"""
        self.ships_left = self.settings.ship_limit

