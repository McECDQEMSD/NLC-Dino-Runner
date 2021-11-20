import pygame
from nlc_dino_runner.utils.constants import SCREEN_WIDTH


class HammerToolManager:
    def __init__(self):
        self.hammer_tools = []
        self.dino_status = False  # Does the dino has the hammer power up?
        self.hammer_tool_status = False  # Is any hammer tool in use?
        self.temporal_hammer = None  # The hammer in current use
        self.hammer_collision = False  # Has the hammer collide with any object?

    def update(self, keyboard_input, game):
        if self.dino_status:
            if keyboard_input[pygame.K_SPACE] and not self.hammer_tool_status:  # Has the dino thrown the hammer?
                self.hammer_tool_status = True
                self.temporal_hammer = self.hammer_tools.pop()
                self.temporal_hammer.rect.x = game.player.dino_rect.x
                self.temporal_hammer.rect.y = game.player.dino_rect.y
                print('Hammer thrown. Remain:', len(self.hammer_tools))

                if not self.hammer_tools:
                    game.player.hammer = False
                    game.player.hammer_end = True

            if self.hammer_tool_status:
                self.temporal_hammer.update()  # update hammer coord
                if self.temporal_hammer.rect.colliderect(game.obstacle_manager.obstacle_position):
                    self.hammer_collision = True
                else:
                    self.hammer_collision = False

                if self.temporal_hammer.rect.x >= SCREEN_WIDTH:
                    self.hammer_collision = False
                    self.hammer_tool_status = False

            if not self.hammer_tools and not self.hammer_tool_status:  # Dino has no more tools :(
                self.reset()

    def draw(self, screen):
        if self.hammer_tool_status:
            self.temporal_hammer.draw(screen)

    def reset(self):
        self.dino_status = False
        self.hammer_collision = False
        self.hammer_tools = []
