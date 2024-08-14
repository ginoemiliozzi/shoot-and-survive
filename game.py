import pygame
import config
from typing import Tuple
from entities import Player, Monster, GameHUD

class Game:

    def __init__(self, monsters_amount):
        pygame.init()
        screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        terrain = pygame.transform.scale(pygame.image.load(config.terrain_img), (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        players = pygame.sprite.GroupSingle()
        shots = pygame.sprite.Group()
        monsters = pygame.sprite.Group()
        player = Player(screen, shots)
        players.add(player)

        for _ in range(0, monsters_amount):
            m = Monster(config.monster_img, shots, players)
            monsters.add(m)

        hud = GameHUD(screen, player, monsters)

        self.screen = screen
        self.players = players
        self.shots = shots
        self.monsters = monsters
        self.hud = hud
        self.terrain = terrain


    def get_components(self) -> Tuple[pygame.surface.Surface, pygame.sprite.GroupSingle, pygame.sprite.Group, pygame.sprite.Group, GameHUD, pygame.surface.Surface]:
        return (self.screen, self.players, self.shots, self.monsters, self.hud, self.terrain)

    