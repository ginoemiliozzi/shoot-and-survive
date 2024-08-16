import pygame
from entities import Player
from objects import Potion_HP
from typing import Callable
import config

class GameHUD:
    def __init__(self, screen: pygame.surface.Surface, player: Player, monsters: pygame.sprite.Group, current_level: Callable[[], int]):
        self.screen = screen
        self.player = player
        self.monsters = monsters
        self.body_font = pygame.font.SysFont(None, 24) 
        self.title_font = pygame.font.SysFont(None, 60)
        self.hp_bar_height = 10
        self.hp_bar_width = 100
        self.monsters_left_width = 100
        self.current_level = current_level
        

    def hp_bar(self, padding_x):
        bar_x = self.screen.get_width() - self.hp_bar_width - padding_x
        bar_y = 10

        current_hp_calc = int(self.hp_bar_width * (self.player.current_hp / self.player.max_hp))

        full_bar_surface = pygame.Surface((self.hp_bar_width, self.hp_bar_height))
        full_bar_surface.fill(config.COLOR_RED)

        current_hp_width = current_hp_calc if current_hp_calc > 0 else 0
        current_hp_surface = pygame.Surface((current_hp_width, self.hp_bar_height))
        current_hp_surface.fill(config.COLOR_GREEN)

        hp_text = self.body_font.render("HP", True, config.COLOR_WHITE)

        self.screen.blit(full_bar_surface, (bar_x, bar_y))
        self.screen.blit(hp_text, (bar_x - 30, bar_y))
         
        if current_hp_width > 0:
            self.screen.blit(current_hp_surface, (bar_x, bar_y))
        
        return self.hp_bar_width + hp_text.get_width()

    def monsters_left(self, padding_x):
        monsters_left = len(self.monsters.sprites())
        monsters_left_text = self.body_font.render(f"MONSTERS LEFT {monsters_left}", True, config.COLOR_WHITE)
        monsters_section_width = monsters_left_text.get_width()
        x = self.screen.get_width() - monsters_section_width - padding_x
        y = 10
        self.screen.blit(monsters_left_text, (x, y))

        return monsters_section_width
    
    def potions_left(self, padding_x):
        potions_left = self.player.inventory.count_by_tag(Potion_HP.ITEM_TAG)
        potions_left_text = self.body_font.render(f"HP POTIONS (E): {potions_left}", True, config.COLOR_WHITE)
        potions_section_width = potions_left_text.get_width()
        x = self.screen.get_width() - padding_x - potions_section_width
        y = 10
        self.screen.blit(potions_left_text, (x, y))

        return potions_section_width
    
    def level_info(self, padding_x):
        level_info_text = self.title_font.render(f"LEVEL {self.current_level()}", True, config.COLOR_WHITE)
        level_section_width = level_info_text.get_width()
        x = self.screen.get_width() - padding_x - level_section_width
        y = 10
        self.screen.blit(level_info_text, (x, y))

        return level_section_width

    def render(self):
        gap = 30
        acc_padding_right = 30
        acc_padding_right += self.hp_bar(acc_padding_right)
        acc_padding_right += gap
        acc_padding_right += self.monsters_left(acc_padding_right)
        acc_padding_right += gap
        acc_padding_right += self.potions_left(acc_padding_right)
        acc_padding_right += gap
        acc_padding_right += self.level_info(acc_padding_right)

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

