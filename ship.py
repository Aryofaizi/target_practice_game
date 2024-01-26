import pygame


class Ship:
    """a class to represent ship image on screen"""
    
    def __init__(self, game):
        """initialize ship attributes like ship image and rect"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # load image and rect
        self.image = pygame.image.load("images/gun.bmp")
        self.image_rect = self.image.get_rect()
        
        # set image position
        self.image_rect.midleft = self.image_rect.midleft
        
    def blit_me(self):
        """make image visible on screen"""
        self.screen.blit(self.image, self.image_rect)
        
        
        
        
        
    