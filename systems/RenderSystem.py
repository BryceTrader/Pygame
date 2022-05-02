from dataclasses import dataclass
import pygame

@dataclass
class RenderSystem:
    window: pygame.Surface
    name: str = 'RenderSystem'
    
    def update(self, entities):
        for entity in entities:
            sprite = entity.components['SpriteComponent']
            sprite_image = sprite.sprite
            sizeX = sprite.sizeX
            sizeY = sprite.sizeY
            sprite_image = pygame.transform.scale(sprite_image, (sizeX, sizeY))
            x = entity.components['PositionComponent'].x
            y = entity.components['PositionComponent'].y
            self.window.blit(sprite_image, (x, y))
            pygame.display.update()