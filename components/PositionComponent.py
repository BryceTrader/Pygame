from BaseComponent import BaseComponent

class PositionComponent(BaseComponent):
    def __init__(self, position) -> None:
        super().__init__("PositionComponent")
        self.x = position['x']
        self.y = position['y']
    
    def __repr__(self) -> str:
        return "".join([f'PositonComponent({self.name}, ', '{ ', f'"x" : {self.x}, "y" : {self.y}', ' })'])
    
test = PositionComponent({ "x": 0, "y": 0 })

print(test)