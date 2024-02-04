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
        self.limited_bullet = 3
        self.missed_bullet = 3
        
        # a scale to make the game faster
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """initialize dynamic settings"""
        self.bullet_speed = 1
        # target 
        self.target_speed = 0.5
        self.direction = -1 
        
    def increase_speed(self):
        """to increase speed with every game progress"""
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale
        