from utils.coords import Vector2

class Player:

    body = []

    def __init__(self, symbol, position, direction = Vector2(0, 0)):
        self.symbol = symbol
        self.body.append(position)
        self.direction = direction

    @property
    def head(self):
        if self.body_length > 0:
            return self.body[0]

        return None

    @property
    def tail(self):
        if len(self.body) > 0:
            return self.body[-1]
        
        return None

    def set_x_direction(self, x):
        self.direction = Vector2(x, 0)

    def set_y_direction(self, y):
        self.direction = Vector2(0, y)

    def move(self):
        head = self.body[0]
        if len(self.body) > 1:
            for i in range(0, len(self.body) - 1):
                self.body[-1 - i] = self.body[-2 - i].copy()
        
        head.x += self.direction.x
        head.y += self.direction.y

        return head
    
    def grow(self):
        tail_pos = self.body[-1].copy()
        self.body.append(tail_pos) 
