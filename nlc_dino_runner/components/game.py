import pygame
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from nlc_dino_runner.utils.constants import (TITTLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS)

class Game:
    def __init__(self):
        pygame.init()
        self.playing = False
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.game_speed = 30
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.death_count = 0

    def score(self):
        self.points += 1
        if self.points % 10 == 0:
            self.game_speed += 1
        score_element, score_element_rec = text_utils.get_score_element(self.points, )
        self.screen.blit(score_element, score_element_rec)

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_width = SCREEN_WIDTH // 2
        half_heigth = SCREEN_HEIGHT //2
        text_element, text_element_rec = text_utils.get_centered_message('Press any key to start', )
        self.screen.blit(text_element, text_element_rec)
        text_element, text_element_rec = text_utils.get_centered_message('Death Count: ' + str(self.death_count), height = half_heigth + 50)
        self.screen.blit(text_element, text_element_rec)
        self.screen.blit(ICON, (half_width - 40, half_heigth -150))

    def handle_key_events_on_menu(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if events.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()


    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_imput = pygame.key.get_pressed()
        self.player.update(user_imput)
        self.obstacle_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_with:
            self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed