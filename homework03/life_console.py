import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.rows = len(self.life.curr_generation)
        self.cols = len(self.life.curr_generation[0])

    def draw_borders(self, screen) -> None:
        screen.border()

    def draw_grid(self, screen) -> None:
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                symbol = "*" if self.life.curr_generation[i][j] else " "
                screen.addch(i, j, symbol)

    def run(self) -> None:
        screen = curses.initscr()
        # PUT YOUR CODE HERE
        curses.endwin()
