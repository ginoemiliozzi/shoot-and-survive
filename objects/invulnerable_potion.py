from attributes import HealthPoints
from .inventory_object import InventoryObject

class Potion_Invulnerable(InventoryObject):
    """ Makes the consumer invulnerable for a short time """

    ITEM_TAG = "INVULNERABLE_POTION"

    def __init__(self):
        self.invulnerable_seconds = 2
    
    def use(self, entity: HealthPoints):
        entity.become_invulnerable(self.invulnerable_seconds)

    def tag(self) -> str:
        return Potion_Invulnerable.ITEM_TAG

