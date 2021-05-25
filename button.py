import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        """Init button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (144, 238, 144)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('calibri', 48)

        # Build and center the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn the message into rendered text image and center it on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)