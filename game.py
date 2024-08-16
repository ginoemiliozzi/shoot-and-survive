import pygame
import config
from typing import Tuple
from entities import Player, Monster, GameHUD

class Game:

    def __init__(self, monsters_amount):
        pygame.init()
        self.current_level = 1
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.terrain = pygame.transform.scale(pygame.image.load(config.terrain_img), (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.players = pygame.sprite.GroupSingle()
        self.shots = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        
        player = Player(self.screen, self.shots)
        self.hud = GameHUD(self.screen, player, self.monsters, lambda : self.current_level)
        self.players.add(player)
        self.add_monsters(monsters_amount)
     
    def get_components(self) -> Tuple[pygame.surface.Surface, pygame.sprite.GroupSingle, pygame.sprite.Group, pygame.sprite.Group, GameHUD, pygame.surface.Surface]:
        return (self.screen, self.players, self.shots, self.monsters, self.hud, self.terrain)

    def add_monsters(self, monsters_amount: int):
        for _ in range(0, monsters_amount):
            m = Monster(config.monster_img, self.shots, self.players)
            self.monsters.add(m)

    def next_level(self):
        self.current_level += 1
        self.add_monsters(self.current_level*2)