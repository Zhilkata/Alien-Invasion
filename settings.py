class Settings:
    """Class that stores all game settings."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Difficulty flag
        self.difficulty_easy = False

        # Cheat flag
        self.cheats_enabled = False

        # Bullet settings
        if self.difficulty_easy:
            self.bullet_speed = 9.0
            self.bullet_width = 600
            self.bullet_height = 3
            self.bullet_color = (220, 20, 60)
            self.bullets_allowed = 200
        else:
            self.bullet_speed = 2.5
            self.bullet_width = 7
            self.bullet_height = 39
            self.bullet_color = (60, 60, 60)
            self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 50

        # Speed of game speed-up & score scale
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init changeable settings during playtime"""
        # Ship settings
        if self.difficulty_easy:
            self.ship_speed = 9
            self.ship_limit = 6
        else:
            self.ship_speed = 2.5
            self.ship_limit = 3

        # 1 = right, -1 = left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase difficulty"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)