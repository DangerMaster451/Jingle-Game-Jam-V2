from Projectiles import Projectile, Snowball
from Player import Player

class Upgrade():
    def __init__(self, cool_down):
        self.cool_down:float = cool_down

    def check_cool_down(self, dt:float) -> bool:
        if self.timer <= 0:
            self.timer = self.cool_down
            return True
        self.timer -= dt
        return False

class Default(Upgrade):
    def __init__(self):
        self.cool_down = 1
        self.timer:float = self.cool_down
        super().__init__(self.cool_down)

    def action(self, player:Player) -> Snowball:
        return Snowball(player.x, player.y, player.direction)