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

        # Ship settings
        if self.difficulty_easy:
            self.ship_speed = 3.0
            self.ship_limit = 6
        else:
            self.ship_speed = 1.5
            self.ship_limit = 3

        # Bullet settings
        if self.difficulty_easy:
            self.bullet_speed = 9.0
            self.bullet_width = 600
            self.bullet_height = 3
            self.bullet_color = (220, 20, 60)
            self.bullets_allowed = 200
        else:
            self.bullet_speed = 1.0
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = (60, 60, 60)
            self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 100
        # 1 = right, -1 = left
        self.fleet_direction = 1


