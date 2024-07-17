import numpy as np
import scipy.signal as signal


class GameOfLife:
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    def __init__(self, state=None, grid_shape=10):
        self.grid_shape = grid_shape
        if state is None:
            self.grid = np.random.randint(0, 2, (grid_shape, grid_shape))
        else:
            self.grid = state
        # self.grid = np.zeros((grid_shape, grid_shape))
        # self.grid[3:6, 3] = 1

    def update(self):
        neighbor_count = signal.convolve2d(self.grid, self.kernel, mode="same")
        ones = np.multiply(neighbor_count, self.grid)
        ones[ones < 2] = 0
        ones[ones > 3] = 0
        ones[ones != 0] = 1

        zeros = np.multiply(
            neighbor_count, np.ones_like(self.grid) - self.grid)
        zeros[zeros != 3] = 0
        zeros[zeros == 3] = 1
        self.grid = np.add(ones, zeros)

    def get_grid(self):
        return self.grid

    def get_state(self):
        return self.grid

    def set_state(self, state):
        self.grid = state

    def reset(self):
        self.grid = np.random.randint(0, 2, self.grid.shape)

    def print_board(self, truncate=True):
        if truncate:
            x, y = np.where(self.grid == 1)
            temp_grid = self.grid[min(x):max(x)+1, min(y):max(y)+1]
        else:
            temp_grid = self.grid

        for row in temp_grid:
            for col in row:
                if col == 0:
                    print('□ ', end='')
                else:
                    print('■ ', end='')
            print()


if __name__ == '__main__':
    game = GameOfLife()
    round_count = 0
    while True:
        print(f'Round {round_count}:')
        game.print_board()
        game.update()
        round_count += 1
        input()
