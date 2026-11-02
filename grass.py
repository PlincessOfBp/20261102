from itertools import count

from pico2d import load_image


class Grass:
    count = 0

    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        if self.count == 0:
            self.image.draw(400, 30)
        else:
            self.image.draw(400, 40)

    def update(self):
        pass
