from .level import Level
from .player import Player
from .apple import Apple
from time import perf_counter
from utils.coords import Vector2
import os
import random
import msvcrt

class Game:
    """
    Game instance responsible for game logic and keeping game state.
    """

    def __init__(self, width, height):
        self.height = height
        self.width  = width
        
        self.level = None
        self.player = None
        self.apple = None
        self.has_started = False
        self.will_restart = False

    @property
    def symbols(self):
        """
        Readonly property with symbols representing in-game entities and environment.
        """
        return {
        'player': '#',
        'apple': 'O',
        'h_wall': '-',
        'v_wall': '|',
        'empty': ' '
    }

    def start(self):
        """
        Method responsible for starting the game.
        It initiates the main "infinite" game-loop.
        """

        self.generate_level()
        self.spawn_player()
        self.spawn_food()

        start_time = perf_counter()
        tick_interval = 0.3

        self.render_frame()

        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                self.handle_input(key)

                if self.has_started == False:
                    self.has_started = True

            if perf_counter() - start_time >= tick_interval and self.has_started == True:
                self.move_player()
                
                if self.will_restart == True:
                    break
                
                self.render_frame()
                start_time = perf_counter()

        if self.will_restart == True:
            self.will_restart = False
            self.restart()

    def restart(self):
        self.level = None
        self.has_started = False
        self.player = None
        self.apple = None

        self.start()

    def move_player(self):

        last_tail_x, last_tail_y = self.player.tail.copy()

        new_pos = self.player.body[0] + self.player.direction

        if new_pos == self.apple.position:
            self.spawn_food()
            self.player.grow()
        elif self.level.get_position(new_pos.x, new_pos.y) != self.symbols['empty']:
            self.will_restart = True

        new_pos = self.player.move()
        
        self.level.update_position(new_pos.x, new_pos.y, self.player.symbol)

        if (last_tail_x != self.player.tail.x or last_tail_y != self.player.tail.y):
            self.level.update_position(last_tail_x, last_tail_y, self.symbols['empty'])



    def spawn_food(self):
        apple_pos = Vector2(0, 0)
        while self.level.get_position(apple_pos.x, apple_pos.y) != self.symbols['empty']:
            apple_pos = self.get_random_position()

        x, y = apple_pos
        self.level.update_position(x, y, self.symbols['apple'])
        self.apple = Apple(x, y)

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
        elif key == b'q':
            quit()

    def spawn_player(self):
        position = self.get_random_position()
        self.player = Player(self.symbols['player'], position)
        self.level.update_position(position.x, position.y, self.player.symbol)

    def generate_level(self):
        edge_row = [self.symbols['h_wall']] * self.width
        middle_row = [self.symbols['v_wall']] + [self.symbols['empty']] * (self.width - 2) + [self.symbols['v_wall']]
        
        self.level = Level([
            edge_row,
            *[middle_row.copy() for _ in range(self.height - 2)],
            edge_row
        ])

    def render_frame(self):
        # Clear view from previous render
        os.system("cls")
        print(self.level)

    def get_random_position(self):
        """
        Generates random x, y cordinates

        :return: Generated oordinates
        :rtype: coords.Vector2
        """
        return Vector2(random.randint(1, self.width - 2), random.randint(1, self.height - 2))
    