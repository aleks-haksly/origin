from enum import Enum
import pygame


CELL_SEIZE = 50
FPS = 30

class Cell(Enum):
    CROSS = 1
    ZERO = 0
    VOID = None


class GameFieldView:

    def __init__(self, field):
        self.field = field
        self.field_height = field.height * CELL_SEIZE
        self.field_width = field.width * CELL_SEIZE

    def get_coords(self, x, y):
        return x, y

    def check_coords(self, x, y):
        return True


class Player:
    def __init__(self, name, mark_type):
        self.name = name
        self.type = mark_type


class GameRoundManager:

    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self.currentPlayer = 0

    def handle_click(self, i, j):
        print(f'handled {i}, {j}')


class GameWindow:

    def __init__(self):
        pygame.init()
        self._height = 600
        self._width = 800
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("CrossZeros")
        self.game_widget = GameFieldView(GameField())
        self.game_manager = GameRoundManager(Player('Вася', Cell.CROSS), Player('Петя', Cell.ZERO))

    def main_loop(self):
        game_finished = False
        while not game_finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_finished = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if self.game_widget.check_coords(x, y):
                        i, j = self.game_widget.get_coords(x, y)
                        self.game_manager.handle_click(i, j)
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


class GameField:

    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID]*self.width for _ in range(self.height)]

def main():
    window = GameWindow()
    window.main_loop()

if __name__ == '__main__':
    main()
