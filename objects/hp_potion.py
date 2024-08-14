from attributes import HealthPoints
from .inventory_object import InventoryObject

class Potion_HP(InventoryObject):
    """ Heals an entity with HealthPoints"""

    ITEM_TAG = "HP_POTION"

    def __init__(self):
        self.heal_amount = 10
    
    def use(self, entity: HealthPoints):
        entity.heal(self.heal_amount)

    def tag(self) -> str:
        return Potion_HP.ITEM_TAG

