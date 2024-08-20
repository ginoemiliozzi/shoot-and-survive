import pygame


class HealthPoints:
    """ Has HP - can take damage and heal"""

    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.last_damaged_tick = 0  # Track when the player was last damaged
        self.damage_display_duration = 500
        self.is_invulnerable = False
        self.remove_invulnerability_tick = 0  # Track when to remove invulnerability
        
    def take_damage(self, dmg) -> bool:
        """ Takes damage to reduce current_hp - Returns True if the damaged killed the entity and False otherwise"""
        if self.is_invulnerable:
            return False
        self.current_hp -= dmg
        self.last_damaged_tick = pygame.time.get_ticks()
        
        return self.current_hp <= 0
    
    def heal(self, heal) -> bool:
        """ Heals HP - Returns True if remains full health """
        new_hp = self.current_hp = heal
        reach_max = new_hp <= self.max_hp
        self.current_hp = self.max_hp if reach_max else new_hp
        return reach_max
    
    def become_invulnerable(self, duration_seconds):
        """ Makes the entity invulnerable to damage """
        self.is_invulnerable = True
        self.remove_invulnerability_tick = pygame.time.get_ticks() + (duration_seconds * 1000)

    def should_display_invulnerable(self):
        """ Returns True if the entity is invulnerable - otherwise returns False and changes self property """
        current_ticks = pygame.time.get_ticks()
        if current_ticks > self.remove_invulnerability_tick:
            self.is_invulnerable = False
            return False
        else:
            return True

    def should_display_dmg(self) -> bool:
        """ Returns true if we are in the time window to display the damage received """
        elapsed_time = pygame.time.get_ticks() - self.last_damaged_tick
        return elapsed_time < self.damage_display_duration and self.last_damaged_tick != 0 and not self.is_invulnerable
    