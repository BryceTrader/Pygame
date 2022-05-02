from dataclasses import dataclass, field
from Entity import Entity

@dataclass
class GameManager:
    entities: list = field(default_factory=list)
    systems: list = field(default_factory=list)
    
    def add_entity(self, entity: Entity):
        self.entities.append(entity)
        
    def add_system(self, system):
        self.systems.append(system)
        
    def update(self):
        for system in self.systems:
            system.update(self.entities)