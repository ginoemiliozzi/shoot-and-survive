import pygame
import config

def apply_invulnerable_overlay(image):
    shield_radius = 3
    shield_color = config.COLOR_WHITE
    image_rect = image.get_rect()
    
    # Create a new surface with space for the shield
    shield_surface = pygame.Surface((image_rect.width + shield_radius * 2, image_rect.height + shield_radius * 2), pygame.SRCALPHA)
    
    # Calculate the position to center the image on the new surface
    image_position = (shield_radius, shield_radius)
    
    # Draw the shield (a circle around the image)
    pygame.draw.circle(shield_surface, shield_color, (image_rect.width // 2 + shield_radius, image_rect.height // 2 + shield_radius), max(image_rect.width, image_rect.height) // 2 + shield_radius)
    
    # Blit the original image onto the shield surface
    shield_surface.blit(image, image_position)
    
    return shield_surface


def apply_red_overlay(image):
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