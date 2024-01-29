from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    """a class to represent bullets in game"""
    
    def __init__(self, game):
        super().__init__()
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        
        # bullet width
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        
        # bullet color 
        self.color = self.settings.bullet_color
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # set position based on the ship
        self.rect.midright = game.ship.rect.midright
        
        
    def draw_bullet(self):
        """make bullet visible on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
        
        
        
        