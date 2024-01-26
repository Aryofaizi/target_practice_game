import pygame, sys
from ship import Ship


class Target:
    """target practice class a class to represent a 
    rectangle on the edge of the screen as target 
    and a ship for the player to shoot the target with"""
    
    def __init__(self):
        """initialize screen"""
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("target practice!")
        
        # ship instance 
        self.ship = Ship(self)
        
    def run_game(self):
        """the main game loop"""
        while True:
            self._check_event()
            self._update_screen()
            
    def _check_event(self):
        """checks for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
                
    def _check_keydown_event(self, event):
        """checks keyboard keydown"""
        if event.key == pygame.K_q:
            sys.exit()
            
    def _update_screen(self):
        """update and flip screen to the latest frame"""
        self.screen.fill((255, 255, 255))
        self.ship.blit_me()
        pygame.display.flip()
        
    
    
if __name__ == "__main__":
    game = Target()
    game.run_game()