from dataclasses import dataclass

@dataclass(kw_only=True)
class PositionComponent:
    name: str = 'PositionComponent'
    x: int = 0
    y: int = 0