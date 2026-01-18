from level import Level
from time import perf_counter
from player import Player
import os
import random
import msvcrt

class Game:
    """
    Game instance responsible for game logic and keeping game state.
    """

    level = None
    player = None

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

        start_time = perf_counter()
        tick_interval = 0.5

        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                self.handle_input(key)

            if perf_counter() - start_time >= tick_interval:
                self.render_frame()
                self.move_player()
                start_time = perf_counter()

    def move_player(self):
        position    = self.player.head
        direction   = self.player.direction
        symbol = self.player.symbol
        new_x = position[0] + direction[0]
        new_y = position[1] + direction[1]
        self.level.update_position(new_x, new_y, symbol)
        position[0] = new_x
        position[1] = new_y

    def handle_input(self, key):
        keys = {
            'UP': b'w',
            'RIGHT': b'd',
            'DOWN': b's',
            'LEFT': b'a'
        }

        if key == keys['UP']:
            self.player.set_y_direction(-1)
        elif key == keys['DOWN']:
            self.player.set_y_direction(1)
        elif key == keys['RIGHT']:
            self.player.set_x_direction(1)
        elif key == keys['LEFT']:
            self.player.set_x_direction(-1)

    def spawn_player(self):
        x, y = self.pick_random_position()
        self.player = Player('#', [x, y])
        self.level.update_position(x, y, self.player.symbol)

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

    def pick_random_position(self):
        """
        Generates random x, y cordinates

        :return: [x,y] coordinates as list 
        """
        return [random.randint(1, self.width - 2), random.randint(1, self.height - 2)]
    