from xml.sax import SAXNotRecognizedException
from pygame import image
from os import path

def get_image(file):
    return image.load(path.join('..', 'assets', f'{file}.png'))

class SpriteComponent:
    def __init__(self, sprite, sizeX, sizeY):
        self.name = "SpriteComponent"
        self.sprite = get_image(sprite)
        self.sizeX = sizeX
        self.sizeY = sizeY