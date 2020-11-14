import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


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

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        self.grid = self.life.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_grid()
            self.draw_lines()

            self.grid = self.life.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()
