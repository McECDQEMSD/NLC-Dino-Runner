import random

import pygame.time
from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import SCREEN_WIDTH

# The one who moves the image


class Obstacle(Sprite):

    def __init__(self, png_array, bird_case=False):
        self.bird_case = bird_case
        if bird_case:
            self.counter = 0
            self.bird_list = png_array
            self.bird_image = png_array[0]
        self.image = self.bird_image if bird_case else png_array[random.randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 20
        self.step_index = 0

    def update(self, img_list, game):
        if self.step_index == 10:
            self.step_index = 0

        self.rect.x -= game.game_speed
        if self.rect.x < -self.rect.width:
            img_list.pop()

    def unpack_bird_list(self):
        self.bird_image = self.bird_list[self.step_index // 5]
        self.step_index += 1

    def draw(self, screen):
        if self.bird_case:
            self.unpack_bird_list()
            screen.blit(self.bird_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
