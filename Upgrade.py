from Projectiles import Projectile, Snowball
from Player import Player

class Upgrade():
    image_path:str
    
    def __init__(self):
        self.description:str
        pass

    def check_cool_down(self, dt:float) -> bool:
        return False

class Default(Upgrade):
    image_path = "Assets/evil_snowman.png"
    def __init__(self):
        self.cool_down:float = 0.5
        self.timer:float = self.cool_down
        super().__init__()

    def action(self, player:Player) -> Snowball:
        return Snowball(player.x, player.y, player.direction)
    
    def check_cool_down(self, dt:float) -> bool:
        if self.timer <= 0:
            self.timer = self.cool_down
            return True
        self.timer -= dt
        return False

class Thorns(Upgrade):
    threshold = 100
    damage = 30
    image_path = "Assets/Thorns Sprite.png"
    def __init__(self):
        self.description = "Thorns\nDeals damage to surrounding enemies\n when the player is damaged\n**SPACE to Select**"
        super().__init__()

class SweepingEdge(Upgrade):
    threshold = 100
    damage = 30
    image_path = "Assets/Sweeping Edge Sprite.png"
    def __init__(self):
        self.description = "Sweeping Edge\nDeals damage to surrounding\n enemies that get damaged\n**SPACE to Select**"
        super().__init__()

class Healing(Upgrade):
    image_path = "Assets/Health Pickup.png"
    def __init__(self):
        self.description = "Instant Health\nRestores Health by 30%\n**SPACE to Select**"
        super().__init__()

class Speed(Upgrade):
    image_path = "Assets/Speed Pickup.png"
    def __init__(self):
        self.description = "Speed Boost\nIncreases Player Speed by 50%\n**SPACE to Select**"
        super().__init__()

class Snowball_Upgrade(Upgrade):
    image_path = "Assets/More Snowballs.png"
    def __init__(self):
        self.description = "Snowball Upgrade\nIncreases number of snowballs thrown by 50%\n**Space to Select**"
        super().__init__()