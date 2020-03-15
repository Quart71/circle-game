import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'circle_game'

class Circle:
    def __init__(self, radius=15):
        self.radius = radius
        sides = [
            {   # left
                'x': 1+self.radius,
                'y': random.randint(1+self.radius, SCREEN_HEIGHT-self.radius-1),
                'dx': random.randint(2, 5),
                'dy': random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
            },
            {   # right
                'x': SCREEN_WIDTH-self.radius-1,
                'y': random.randint(1+self.radius, SCREEN_HEIGHT-self.radius-1),
                'dx': random.randint(-5, -2),
                'dy': random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
            },
        ]

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BANANA_MANIA)
        self.circles = []
        self.player = None

    def update(self, delta_time):
        pass

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()

arcade.run()
