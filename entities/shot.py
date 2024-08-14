import pygame
import config

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, direction: pygame.math.Vector2):
        super().__init__()
        original_direction = pygame.math.Vector2(1, 0) # Right
        shot_surface = pygame.transform.scale(pygame.image.load(config.base_projectile_image), (30, 7))
        rotation_angle = direction.angle_to(original_direction) 
        self.image = pygame.transform.rotate(shot_surface, rotation_angle)
        self.rect = self.image.get_rect()
        
        self.rect.centerx = x
        self.rect.centery = y
        self.dmg = 1
        self.velocity = direction * 10

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        if self.rect.right < 0 or self.rect.left > config.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > config.SCREEN_HEIGHT:
            self.kill()  # Remove the bullet if it goes off-screen
