from entities.shot import Shot
import pygame
import random
import config

class Monster(pygame.sprite.Sprite):
    def __init__(self, image_path, shots_group: pygame.sprite.Group, players_group: pygame.sprite.GroupSingle):
        super().__init__()
        self.normal_img = pygame.transform.scale(pygame.image.load(image_path), (110, 110))
        self.damaged_img = pygame.transform.scale(pygame.image.load(config.monster_damaged_img), (110, 110))
        self.damaged_time = 0
        self.damage_display_duration = 500
        self.image = self.normal_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(110, config.SCREEN_WIDTH), random.randint(110, config.SCREEN_HEIGHT))
        self.shots_group = shots_group
        self.players_group = players_group
        self.hp = 3
        self.dmg = 1

    def update(self):
        player = self.players_group.sprite
        self.move_towards(player)

        # Receive dmg from shots
        hits = pygame.sprite.spritecollide(self, self.shots_group, dokill=True)
        for shot in hits:
            self.take_damage(shot.dmg)

        # Do damage to player
        damaged_players = pygame.sprite.spritecollide(self, self.players_group, dokill=False)
        for player in damaged_players:
            player.take_damage(self.dmg)

        if self.image == self.damaged_img and pygame.time.get_ticks() - self.damaged_time > self.damage_display_duration:
            self.image = self.normal_img

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
        else:
            self.image = self.damaged_img
            self.damaged_time = pygame.time.get_ticks()  

    def move_towards(self, player):
        if not player:
            return
        # Calculate direction vector towards the player
        direction_x = player.rect.centerx - self.rect.centerx
        direction_y = player.rect.centery - self.rect.centery

        # Normalize direction to maintain consistent speed
        distance = max(1, (direction_x**2 + direction_y**2) ** 0.5)
        direction_x /= distance
        direction_y /= distance

        # Move monster towards player
        speed = 1  # Adjust the speed as needed
        self.rect.x += direction_x * speed
        self.rect.y += direction_y * speed