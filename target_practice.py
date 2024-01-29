import pygame, sys
from ship import Ship
from settings import Settings
from target import Target
from bullet import Bullet


class TargetGame:
    """target practice class a class to represent a 
    rectangle on the edge of the screen as target 
    and a ship for the player to shoot the target with"""
    
    def __init__(self):
        """initialize screen"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("target practice!")
        # ship instance 
        self.ship = Ship(self)
        
        # target instance
        self.target = Target(self)
        
        # bullet list
        self.bullets = pygame.sprite.Group()
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    def run_game(self):
        """the main game loop"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()
            
    def _check_event(self):
        """checks for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
                
    def _check_keydown_event(self, event):
        """checks keyboard keydown"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True    
            
    def _check_keyup_event(self, event):
        """checks keyboard keyup event"""
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False
            
    def _update_screen(self):
        """update and flip screen to the latest frame"""
        self.screen.fill((255, 255, 255))
        self.ship.blit_me()
        self.target.draw_target()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()
        
    
    
if __name__ == "__main__":
    game = TargetGame()
    game.run_game()