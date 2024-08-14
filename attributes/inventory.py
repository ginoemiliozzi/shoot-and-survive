from objects import InventoryObject

class Inventory:
    """ Can hold objects to be consumed """

    def __init__(self, objects: set[InventoryObject]) -> None:
        self.items = objects

    def use_item(self, tag: str, *args, **kwargs):
        """ Uses one item for the given item tag - Returns True if an item was found and used """
        current_items = self.items.copy()
        for instance in current_items:
            if instance.tag() == tag:
                instance.use(*args, **kwargs)
                self.items.remove(instance)
                return True
        
        print(f"Item cannot be used - Inventory does not have any: {tag}")
        return False

    def count_by_tag(self, tag: str) -> int:
        """ Returns the amount of items for the given item tag """
        return sum(1 for item in self.items if item.tag() == tag)
