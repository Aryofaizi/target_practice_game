class Stats:
    """a class to set game stats"""
    
    def __init__(self, game):
        self.settings = game.settings
        self.game_active = True
        
    def reset(self):
        """reset game stats"""
        self.game_active = True