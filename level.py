class Level:

    state = []

    def __init__(self, level):
        self.state = level

    def __str__(self):
        return '\n'.join(map(lambda x: ''.join(x), self.state))
    
    def update_position(self, x, y, ascii_symbol):

        if len(ascii_symbol) != 1:
            raise ValueError("Function expects a single ascii character symbol.")

        self.state[y][x] = ascii_symbol

    def get_position(self, x, y):
        return self.state[y][x]