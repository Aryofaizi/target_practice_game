class Settings:
    """the game settings can be changed through this class"""
    
    def __init__(self):
        """initialize attributes"""
        self.screen_width = 700
        self.screen_height = 1_000
        
        # bullets 
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0, 0, 255)
        self.bullet_speed = 0.1