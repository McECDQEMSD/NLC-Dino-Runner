import random

from nlc_dino_runner.utils.constants import SMALL_CACTUS
from nlc_dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self):
        self.index = random.randint(0, 2)
        super(Cactus, self).__init__(self.image_cactus, self.index)
        self.rect.y = 330