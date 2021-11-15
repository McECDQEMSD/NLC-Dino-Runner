import pygame

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacle = []

    def update(self, game):
        if len(self.obstacle) == 0:
            self.obstacle.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacle:
            obstacle.update(self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield :
                    self.obstacle.remove(obstacle)
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacle = []
