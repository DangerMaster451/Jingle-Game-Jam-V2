import pygame

class Scorebar():
    def __init__(self) -> None:
        self.width = 200
        self.height = 50
        self.padding = 20

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