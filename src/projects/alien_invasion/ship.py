import pygame

from settings import Settings

class Ship:
    """A class to manage ship"""

    def __init__(self, ai_game):
        """initialize the game and set the starting position"""
        # settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.jpg")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False



    def update(self):
        """Update the ships based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
            


    def blitme(self):
        """Draw the ship at it current location"""
        self.screen.blit(self.image, self.rect)

