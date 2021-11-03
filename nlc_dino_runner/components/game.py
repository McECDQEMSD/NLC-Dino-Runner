import pygame.display
from nlc_dino_runner.utils.constants import TITLE
class Game:
    def __init__(self):
        pygame.init()
        self.playing = False
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode(())
        self.x_pos_bg = 0
        self.y_pos_bg = 400
        self.clock = pygame.time.Clock()
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw(
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = false

    def update(self):
        pass

    def draw(self):
        self.clock.tick(30)
        self.screen.fill((255, 255, 255))
        pygame.display.flip()


    def draw_background(self):
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
