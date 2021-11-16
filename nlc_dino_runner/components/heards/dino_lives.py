from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import HEART, HEART_NUMBER


class Hearts(Sprite):
    def __init__(self):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 25
        self.hearts_number = 27 * HEART_NUMBER

    def draw_hearts(self, screen):
        print(self.hearts_number)
        for i in range(0, HEART_NUMBER):
            screen.blit(self.image, self.rect)
            self.rect.x = self.image.get_width() + self.rect.x
            if self.rect.x > self.hearts_number:
                self.rect.x = 20