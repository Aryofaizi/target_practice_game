import pygame.font


class Target:
    """represent a target rect on screen"""
    
    def __init__(self, game):
        """initialize attributes"""
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 70, 70
        self.bg = (255, 0, 0)
        
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright
        
        
    def draw_target(self):
        """draw target rect on screen"""
        self.screen.fill(self.bg, self.rect)
        
        
        