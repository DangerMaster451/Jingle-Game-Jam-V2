from GameObject import GameObject
from Upgrade import Upgrade
import pygame

class UpgradePickup(GameObject):
    def __init__(self, x:float, y:float, upgrade:Upgrade) -> None:
        self.x = x
        self.y = y
        self.height = 100
        self.width = 25
        self.upgrade = upgrade
        self.image = self.load_image(upgrade.image_path, (18*8,23*8))
        self.font = pygame.font.Font("Assets/font.ttf", 16)
        self.text_lines:list[str] = upgrade.description.splitlines()
        self.rendered_lines:list[pygame.Surface] = [self.font.render(line, True, (139,202,221)) for line in self.text_lines]
    
    def render(self, screen:pygame.Surface) -> None:
        screen.blit(self.image, (round(self.x - self.width/2), round(self.y - self.height/2), self.width, self.height))

    def render_textbox(self, screen:pygame.Surface) -> None:
        rect = pygame.Rect(round(self.x+self.width-25), round(self.y + self.height*2-15), self.width*15, self.height*0.75+30)
        pygame.draw.rect(screen, (32,40,78), rect)

        for index, line in enumerate(self.rendered_lines):
            textRect = line.get_rect()
            textRect.topleft = (round(self.x+self.width-25), round(self.y + self.height*2 + 25*index))
            screen.blit(line, textRect)

        
        