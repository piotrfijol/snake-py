class Level:

    state = []

    def __init__(self, level):
        self.state = level

    def __str__(self):
        return '\n'.join(map(lambda x: ''.join(x), self.state))