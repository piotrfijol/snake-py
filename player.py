from coords import Vector2

class Player:

    def __init__(self, symbol, head_position, direction = Vector2(0, 0)):
        self.symbol = symbol
        self.direction = direction
        self.head = head_position

    def set_x_direction(self, x):
        self.direction = Vector2(x, 0)

    def set_y_direction(self, y):
        self.direction = Vector2(0, y)

    def move(self):
        self.head.x += self.direction.x 
        self.head.y += self.direction.y

        return self.head