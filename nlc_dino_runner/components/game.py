import pygame

from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from nlc_dino_runner.utils.constants import (TITTLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, GAME_SPEED)
from nlc_dino_runner.components.heards.dino_lives import Hearts


class Game:
    def __init__(self):
        pygame.init()
        self.playing = False
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 400
        self.game_speed = GAME_SPEED
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.dino_lives = Hearts()
        self.points = 0
        self.death_count = 0
        self.running = False
        self.death_count = 0
        self.death_count_print = False

    def score(self):
        self.points += 1
        if self.points % 20 == 0:
            self.game_speed += .5

        score_element, score_element_rec = text_utils.get_score_element(self.points, )
        self.screen.blit(score_element, score_element_rec)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_width = SCREEN_WIDTH // 2
        half_heigth = SCREEN_HEIGHT //2
        if self.death_count == 0:
            text_element, text_element_rec = text_utils.get_centered_message('Press any key to Start')
            self.screen.blit(text_element, text_element_rec)
        else:
            text_element, text_element_rec = text_utils.get_centered_message('Press any key to Restart')
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centered_message('Deaths: ' +str(self.death_count), height= 350)
            self.screen.blit(text_element, text_element_rec)
        self.screen.blit(ICON, (half_width - 40, half_heigth - 150))

    def handle_key_events_on_menu(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
            if events.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.points = 0
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
        self.power_up_manager.update(self.points, self.game_speed, self.player)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.dino_lives.draw_hearts(self.screen)
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