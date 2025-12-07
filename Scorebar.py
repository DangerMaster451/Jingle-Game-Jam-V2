import pygame

class Scorebar():
    def __init__(self, screen_size:tuple[int,int]) -> None:
        self.width = screen_size[0]/10
        self.height = screen_size[1]/35
        self.padding = screen_size[0]/100

    def render(self, score:float, required_score:float, screen:pygame.Surface):
        score_width = (score / required_score) * self.width
        if score_width < self.width:
            back_rect = pygame.Rect(self.padding, self.padding, self.width, self.height)
            pygame.draw.rect(screen, "darkslategray4", back_rect)
            front_rect = pygame.Rect(self.padding, self.padding, score_width, self.height)
            pygame.draw.rect(screen, "darkslategray1", front_rect)
        else:
            back_rect = pygame.Rect(self.padding, self.padding, self.width, self.height)
            pygame.draw.rect(screen, "darkslategray1", back_rect)