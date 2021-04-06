# pylint: disable=no-member
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pygame
import life
from life import GameOfLife
from pygame.locals import *
from ui import UI
import pathlib


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.cell_size = cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(len(self.life.curr_generation)):
            for j in range(len(self.life.curr_generation[i])):
                if self.life.curr_generation[i][j] == 0:
                    cell_colour = pygame.Color("white")
                else:
                    cell_colour = pygame.Color("green")
                rect = pygame.Rect(
                    j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size
                )
                pygame.draw.rect(self.screen, cell_colour, rect)

    def change_cell_value(self, cell: life.Cell) -> None:

        c_x = cell[0] // self.cell_size
        c_y = cell[1] // self.cell_size
        if self.life.curr_generation[c_x][c_y]:
            self.life.curr_generation[c_x][c_y] = 0
        else:
            self.life.curr_generation[c_x][c_y] = 1

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        self.life.curr_generation = self.life.create_grid(randomize=True)

        running = True
        pause = False
        while running:
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (
                        y_c,
                        x_c,
                    ) = pygame.mouse.get_pos()
                    self.change_cell_value((x_c, y_c))
                    self.draw_grid()
                    self.draw_lines()
                    pygame.display.flip()
                    clock.tick(self.speed)
                    continue
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pause:
                            pause = False
                        else:
                            pause = True
                    if event.key == pygame.K_s:
                        self.life.save(pathlib.Path("save.txt"))
                    if event.key == pygame.K_l:
                        self.life.from_file(pathlib.Path("save.txt"))

            if pause:
                continue
            # Отрисовка списка клеток
            self.draw_grid()
            self.draw_lines()

            # Выполнение одного шага игры (обновление состояния ячеек)
            self.life.step()

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()


def main():
    game = GameOfLife(size=(48, 64))
    app = GUI(game)
    app.run()


if __name__ == "__main__":
    main()
