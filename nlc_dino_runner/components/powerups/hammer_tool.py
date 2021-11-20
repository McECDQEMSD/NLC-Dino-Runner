from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER


class Hammer_Tool(Sprite):
    def __init__(self):
        self.image = HAMMER
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 15

    def draw(self, screen):
        screen.blit(self.image, self.rect)
