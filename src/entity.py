# entity.py #
class Entity:
    _id_counter = 0
    def __init__(self):
        self.id = Entity._id_counter
        Entity._id_counter += 1
        self.components = {}
        
    def addComponent(self, component):
        self.components[type(component)] = component
        
    def getComponent(self, component_typ):
        return self.components.get(component_typ)