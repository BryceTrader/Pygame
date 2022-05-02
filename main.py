import pygame
from GameManager import GameManager
from systems.RenderSystem import RenderSystem
from Entity import Entity
from components.PositionComponent import PositionComponent
from components.SpriteComponent import SpriteComponent


WIDTH, HEIGHT = 320, 180
SCALE = 4
SWIDTH = WIDTH * SCALE
SHEIGHT = HEIGHT * SCALE
WIN = pygame.display.set_mode((SWIDTH, SHEIGHT))
pygame.display.set_caption('Slime Clicker')
FPS = 60
GM = GameManager()
GM.add_system(RenderSystem(WIN))
Slime = Entity('Slime', PositionComponent(x=SWIDTH/2 - (32*SCALE/2),y=SHEIGHT/2 - (32*SCALE/2)), SpriteComponent(sprite='slime', sizeX=32*SCALE, sizeY=32*SCALE))
GM.add_entity(Slime)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        GM.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    
if __name__ == '__main__':
    main()
    