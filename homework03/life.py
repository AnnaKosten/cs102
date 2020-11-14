import pathlib
import random
import typing as tp
from copy import deepcopy
import pygame

import json
from itertools import product

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        return [
            [random.randint(0, 1) if randomize else 0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def get_neighbours(self, cell: Cell) -> Cells:

        neighbours = []

        dif = [-1, 0, 1]
        for x, y in product(dif, dif):
            if (x, y) == (0, 0):
                continue

            row = cell[0] + y
            col = cell[1] + x

            if 0 <= row < len(self.curr_generation) and 0 <= col < len(self.curr_generation[0]):
                neighbours.append(self.curr_generation[row][col])

        return neighbours

    def get_next_generation(self) -> Grid:

        new_grid = deepcopy(self.curr_generation)

        for i in range(len(new_grid)):
            for j in range(len(new_grid[i])):
                alive_neighbours = sum(self.get_neighbours((i, j)))

                if alive_neighbours == 3 or (
                    self.curr_generation[i][j] == 1 and alive_neighbours == 2
                ):
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0

        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation == self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, "r") as f:
            curr_generation = json.load(f)

        size = len(curr_generation), len(curr_generation[0])
        game = GameOfLife(size=size, randomize=False)
        game.curr_generation = curr_generation

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as f:
            json.dump(self.curr_generation, fp=f)
