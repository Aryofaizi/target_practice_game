import pygame.font


class Target:
    """represent a target rect on screen"""
    
    def __init__(self, game):
        """initialize attributes"""
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.width, self.height = 70, 70
        self.bg = (255, 0, 0)
        
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright
    
        self.y = float(self.rect.y)    

        # direction
        self.direction = self.settings.direction
        # speed 
        self.speed = self.settings.target_speed
        
    def move(self):
        """moves the ship up and down at a steady rate"""
        self.y += self.speed * self.direction 
        self.rect.y = self.y
        
    def check_edges(self):
        if self.rect.top <= self.screen_rect.top or (
            self.rect.bottom >= self.screen_rect.bottom):
            return True
            
    def draw_target(self):
        """draw target rect on screen"""
        self.screen.fill(self.bg, self.rect)
        
        
        