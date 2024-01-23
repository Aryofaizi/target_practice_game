import pygame, sys


class Target:
    """target practice class a class to represent a 
    rectangle on the edge of the screen as target 
    and a ship for the player to shoot the target with"""
    
    def __init__(self):
        """initialize screen"""
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("target practice!")
        
    def run_game(self):
        """the main game loop"""
        while True:
            self._update_screen()
    def _update_screen(self):
        """update and flip screen to the latest frame"""
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
    
    
    
if __name__ == "__main__":
    game = Target()
    game.run_game()