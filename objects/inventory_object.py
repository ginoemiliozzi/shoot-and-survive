from abc import abstractmethod

class InventoryObject:
    """ Can be part of the inventory and can be used"""
    
    @abstractmethod
    def tag(self, *args, **kwargs) -> str:
        pass

    @abstractmethod
    def use(self, *args, **kwargs):
        pass