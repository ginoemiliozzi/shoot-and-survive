from entities.shot import Shot
from objects import Potion_HP
from attributes import Inventory, HealthPoints
import pygame

class Player(pygame.sprite.Sprite, HealthPoints):
    def __init__(self, screen, shots_group):
        pygame.sprite.Sprite.__init__(self)
        HealthPoints.__init__(self, max_hp=100)

        self.container_screen = screen
        self.player_directions = {
                "UP": {
                    "direction_vector": pygame.math.Vector2(0, -1),
                    "direction_images": [
                        pygame.transform.scale(pygame.image.load("assets/player-left1.png").convert_alpha(), (100, 120)),
                        pygame.transform.scale(pygame.image.load("assets/player-left2.png").convert_alpha(), (100, 120)),
                    ]
                },
                "DOWN": {
                    "direction_vector": pygame.math.Vector2(0, 1),
                    "direction_images": [
                        pygame.transform.scale(pygame.image.load("assets/player-right1.png").convert_alpha(), (100, 120)),
                        pygame.transform.scale(pygame.image.load("assets/player-right2.png").convert_alpha(), (100, 120)),
                    ]
                },
                "LEFT": {
                    "direction_vector": pygame.math.Vector2(-1, 0),
                    "direction_images": [
                        pygame.transform.scale(pygame.image.load("assets/player-left1.png").convert_alpha(), (100, 120)),
                        pygame.transform.scale(pygame.image.load("assets/player-left2.png").convert_alpha(), (100, 120)),
                    ]
                },
                "RIGHT": {
                    "direction_vector": pygame.math.Vector2(1, 0),
                    "direction_images": [
                        pygame.transform.scale(pygame.image.load("assets/player-right1.png").convert_alpha(), (100, 120)),
                        pygame.transform.scale(pygame.image.load("assets/player-right2.png").convert_alpha(), (100, 120)),
                    ]
                }
            } 
        self.images = self.player_directions["RIGHT"]["direction_images"]
        self.image = self.images[0]
        self.current_frame = 0
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.shots_group = shots_group
        self.speed = 5
        self.direction = self.player_directions["RIGHT"]["direction_vector"]
        self.inventory = Inventory({
            Potion_HP() for _ in range(0, 3)
        })

    def update(self, keys, events):
        # Movement
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.direction = self.player_directions["UP"]["direction_vector"]
            self.images = self.player_directions["UP"]["direction_images"]
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.direction = self.player_directions["DOWN"]["direction_vector"]
            self.images = self.player_directions["DOWN"]["direction_images"]
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = self.player_directions["LEFT"]["direction_vector"]
            self.images = self.player_directions["LEFT"]["direction_images"]
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = self.player_directions["RIGHT"]["direction_vector"]
            self.images = self.player_directions["RIGHT"]["direction_images"]

        # Shooting event
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot()
                if event.key == pygame.K_e:
                    self.inventory.use_item(Potion_HP.ITEM_TAG, self)

        # Handle damage state
        if self.should_display_dmg():
            # Apply red overlay to images while damaged
            self.images = [self.apply_red_overlay(image) 
                           for image in self.player_directions[self.get_current_direction()]["direction_images"]]
        else:
            # Restore original images after damage duration
            current_direction = self.get_current_direction()
            self.images = self.player_directions[current_direction]["direction_images"]

        self.current_frame += 0.1
        if self.current_frame >= len(self.images):
            self.current_frame = 0

        self.image = self.images[int(self.current_frame)]


    def apply_red_overlay(self, image):
        # Create a copy of the original image to apply the overlay
        damaged_image = image.copy()

        # Lock the image for pixel access
        damaged_image.lock()

        # Iterate over each pixel in the image
        for x in range(damaged_image.get_width()):
            for y in range(damaged_image.get_height()):
                # Get the current pixel color and alpha value
                r, g, b, a = damaged_image.get_at((x, y))

                # If the pixel is not fully transparent, apply the red overlay
                if a > 0:
                    # Calculate the new color with the red overlay
                    new_r = min(r + 100, 255)  # Increase the red channel
                    new_color = (new_r, g, b, a)
                    damaged_image.set_at((x, y), new_color)

        # Unlock the image after modifications
        damaged_image.unlock()

        return damaged_image
            

    def get_current_direction(self):
        if self.direction == self.player_directions["UP"]["direction_vector"]:
            return "UP"
        elif self.direction == self.player_directions["DOWN"]["direction_vector"]:
            return "DOWN"
        elif self.direction == self.player_directions["LEFT"]["direction_vector"]:
            return "LEFT"
        elif self.direction == self.player_directions["RIGHT"]["direction_vector"]:
            return "RIGHT"

    def shoot(self):
        shot = Shot(self.rect.centerx, self.rect.top, self.direction)
        self.shots_group.add(shot)
