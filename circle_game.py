import arcade
import random


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
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
            {   # top
                'x': random.randint(1+self.radius, SCREEN_WIDTH-self.radius-1),
                'y': SCREEN_HEIGHT-self.radius-1,
                'dx': random.choice([-5, -4, -3, -2, 2, 3, 4, 5]),
                'dy': random.randint(-5, -2)
            },
            {   # bottom
                'x': random.randint(1 + self.radius, SCREEN_WIDTH - self.radius - 1),
                'y': self.radius + 1,
                'dx': random.choice([-5, -4, -3, -2, 2, 3, 4, 5]),
                'dy': random.randint(2, 5)
            }
        ]
        side = random.choice(sides)
        self.center_x = side['x']
        self.center_y = side['y']
        self.change_x = side['dx']
        self.change_y = side['dy']
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.update_sides()

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.update_sides()

    def update_sides(self):
        self.left = self.center_x - self.radius
        self.right = self.center_x + self.radius
        self.top = self.center_y + self.radius
        self.bottom = self.center_y - self.radius

class Player(Circle):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.RED_DEVIL
        self.change_x = 0
        self.change_y = 0
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)
        arcade.set_background_color(arcade.color.BLACK)
        self.circles = []
        self.player = None
        self.status = True
        width, heigth = self.get_size()
        self.set_viewport(0, width, 0, height)
        self.left, self.screen_width, self.bottom, self.screen_height = self.get_viewport()

    def update(self, delta_time):
        if self.status:
            if self.check_for_collision():
                circle = self.check_for_collision()
                if self.player.radius > circle.radius:
                    self.replace_circle(circle)
                    self.player.radius += 1
                    if self.player.radius >= 80:
                        self.status = False
                else:
                    self.status = False
            for circle in self.circles:
                if circle.right < 0 or circle.left > SCREEN_WIDTH or circle.top < 0 or circle.bottom > SCREEN_HEIGHT:
                    self.replace_circle(circle)
                circle.update()



    def setup(self):
        self.player = Player()
        for i in range(10):
            self.circles.append(Circle(random.randint(5, self.player.radius+40)))


    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        for circle in self.circles:
            circle.draw()


    def replace_circle(self, circle):
        # узнаем номер шарика в списке
        index = self.circles.index(circle)
        self.circles.pop(index)
        self.circles.append(Circle(random.randint(5, self.player.radius+40)))

    def on_mouse_motion(self, x, y, dx, dy):
        if self.status:
            self.player.center_x = x
            self.player.center_y = y

    def check_for_collision(self):
        for circle in self.circles:
            distance = self.player.radius + circle.radius
            if self.player.center_x > circle.center_x and self.player.center_y > circle.center_y:
                if self.player.center_x - circle.center_x <= distance and self.player.center_y - circle.center_y <= distance:
                    return circle
            elif self.player.center_x > circle.center_x and self.player.center_y <= circle.center_y:
                if self.player.center_x - circle.center_x <= distance and circle.center_y - self.player.center_y <= distance:
                    return circle
            elif self.player.center_x <= circle.center_x and self.player.center_y > circle.center_y:
                if circle.center_x - self.player.center_x <= distance and self.player.center_y - circle.center_y <= distance:
                    return circle
            elif self.player.center_x <= circle.center_x and self.player.center_y <= circle.center_y:
                if circle.center_x - self.player.center_x <= distance and circle.center_y - self.player.center_y <= distance:
                    return circle


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()

arcade.run()
