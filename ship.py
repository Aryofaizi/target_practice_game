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
        
        # set y coordinate
        self.y = float(self.image_rect.y)
        # set move up and down flags
        self.move_up, self.move_down = False, False
    def blit_me(self):
        """make image visible on screen"""
        self.screen.blit(self.image, self.image_rect)
        
    def update(self):
        """update image coordinate"""
        if self.image_rect.top >=0 and self.move_up:
            self.y -=1
        if self.image_rect.bottom <= self.screen_rect.bottom and self.move_down:
            self.y +=1
        self.image_rect.y = self.y

        
        
        
    