from level import Level
import time
import os


class Game:
    """
    Game instance responsible for game logic and keeping game state.
    """

    level = None

    def __init__(self, width, height):
        self.height = height
        self.width  = width

    def start(self):
        """
        Method responsible for starting the game.
        It initiates the main "infinite" game-loop.
        """

        self.generate_level()
        self.spawn_player()

        while True:
            self.render_frame()
            # limit framerate
            time.sleep(0.5)

    def spawn_player(self):
        pass

    def generate_level(self):
        edge_row = ['-'] * self.width
        middle_row = ['|'] + [' '] * (self.width - 2) + ['|']
        
        self.level = Level([
            edge_row,
            *[middle_row.copy() for _ in range(self.height - 2)],
            edge_row
        ])

    def render_frame(self):
        # Clear view from previous render
        os.system("cls")
        print(self.level)