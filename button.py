import pygame


class Button:
    """a class to represent a button on screen"""
    
    def __init__(self, game, msg):
        """initialize button attributes like color and text"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        # rect size
        self.width, self.height = 200, 50
        # create rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # set rect position
        self.rect.center = self.screen_rect.center
        
        # set font 
        self.font = pygame.font.SysFont(None, 42)
        
        # set font color and bg colof
        self.bg = (0, 255, 0) # green
        self.color = (255, 255, 255)
        
        self.msg = self.font.render(msg, True, self.color, self.bg)
        
        self.msg_rect = self.msg.get_rect()
        # set msg in center of the rectangle
        self.msg_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.bg, self.rect)
        self.screen.blit(self.msg, self.msg_rect)
        
        
        