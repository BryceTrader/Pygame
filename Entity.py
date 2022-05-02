class Entity:
    def __init__(self, name, *components) -> None:
        self.components = {}
        self.name = name
        
        for component in components:
            self.add_component(component)
    
    def __repr__(self) -> str:
        return f'Entity({self.name}, {self.components})'
        
    def add_component(self, component) -> None:
        key = component['name']
        self.components[key] = component