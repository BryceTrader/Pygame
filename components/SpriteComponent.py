from BaseComponent import BaseComponent

class SpriteComponent(BaseComponent):
    def __init__(self, sprite) -> None:
        super().__init__("SpriteComponent")
        self.sprite = sprite
        
    def __repr__(self) -> str:
        return f'SpriteComponent({self.name}, {self.sprite})'