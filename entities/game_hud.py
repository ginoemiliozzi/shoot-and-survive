import pygame
from entities import Player

import config

class GameHUD:
    def __init__(self, screen: pygame.surface.Surface, player: Player, monsters: pygame.sprite.Group):
        self.screen = screen
        self.player = player
        self.monsters = monsters
        self.body_font = pygame.font.SysFont(None, 24) 
        self.title_font = pygame.font.SysFont(None, 60)
        self.hp_bar_width = 100
        self.hp_bar_height = 10
        

    def hp_bar(self):
        bar_x = self.screen.get_width() - self.hp_bar_width - 10
        bar_y = 10

        current_hp_width = int(self.hp_bar_width * (self.player.hp / self.player.max_hp))

        full_bar_surface = pygame.Surface((self.hp_bar_width, self.hp_bar_height))
        full_bar_surface.fill(config.COLOR_RED)

        current_hp_surface = pygame.Surface((current_hp_width, self.hp_bar_height))
        current_hp_surface.fill(config.COLOR_GREEN)

        hp_text = self.body_font.render("HP", True, config.COLOR_WHITE)

        self.screen.blit(full_bar_surface, (bar_x, bar_y))
        self.screen.blit(hp_text, (bar_x - 30, bar_y - 2))
         
        if current_hp_width > 0:
            self.screen.blit(current_hp_surface, (bar_x, bar_y))

    def monsters_left(self):
        x = self.screen.get_width() - self.hp_bar_width - 300
        y = 10
        monsters_left = len(self.monsters.sprites())
        monsters_left_text = self.body_font.render(f"MONSTERS LEFT {monsters_left}", True, config.COLOR_WHITE)
        self.screen.blit(monsters_left_text, (x, y))

    def render(self):
        self.hp_bar()
        self.monsters_left()

    def game_over(self):
        game_over_text = self.title_font.render("GAME OVER", True, config.COLOR_RED)
        
        text_rect = game_over_text.get_rect()
        text_x = (self.screen.get_width() - text_rect.width) // 2
        text_y = (self.screen.get_height() - text_rect.height) // 2

        self.screen.blit(game_over_text, (text_x, text_y))

    def game_won(self):
        game_won_text = self.title_font.render("YOU WIN", True, config.COLOR_GREEN)
        
        text_rect = game_won_text.get_rect()
        text_x = (self.screen.get_width() - text_rect.width) // 2
        text_y = (self.screen.get_height() - text_rect.height) // 2

        self.screen.blit(game_won_text, (text_x, text_y))

