from BaseComponent import BaseComponent

class ValueComponent(BaseComponent):
    def __init__(self, value) -> None:
        super().__init__(ValueComponent)
        self.value = value
        
    def __repr__(self):
        return f'ValueComponent({self.name}, {self.value})'
