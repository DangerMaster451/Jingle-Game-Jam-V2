from Projectiles import Projectile, Snowball
from Player import Player

class Upgrade():
    def __init__(self):
        pass

    def check_cool_down(self, dt:float) -> bool:
        return False

class Default(Upgrade):
    def __init__(self):
        self.cool_down:float = 1
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
    damage = 15
    def __init__(self):
        super().__init__()
        