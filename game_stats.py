class GameStats:
    """Track stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Init stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        # High score, not dynamic
        self.high_score = 0

    def reset_stats(self):
        """Init dynamic stats"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

