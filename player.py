class Player:

    def __init__(self, symbol, head_position, direction = [0, 0]):
        self.symbol = symbol
        self.direction = direction
        self.head = head_position

    def set_x_direction(self, x):
        self.direction = [x, 0]

    def set_y_direction(self, y):
        self.direction = [0, y]