import numpy as np
from scipy import signal


class GameOfLife:
    """
    Conway's Game of Life
    """
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    def __init__(self, state=None, grid_shape=10):
        """
        Initialize the GameOfLife object.

        Args:
            state (numpy.ndarray, optional): The initial state of the game. Defaults to None.
            grid_shape (int, optional): The shape of the game grid. Defaults to 10.

        Returns:
            None
        """
        self.grid_shape = grid_shape
        if state is None:
            self.grid = np.random.randint(0, 2, (grid_shape, grid_shape))
        else:
            self.grid = state
        # self.grid = np.zeros((grid_shape, grid_shape))
        # self.grid[3:6, 3] = 1

    def update(self):
        """
        Updates the state of the GameOfLife grid based on Conway's Game of Life rules.

        Args:
            self: The GameOfLife object.

        Returns:
            None
        """
        neighbor_count = signal.signal.convolve2d(
            self.grid, self.kernel, mode="same")
        ones = np.multiply(neighbor_count, self.grid)
        ones[ones < 2] = 0
        ones[ones > 3] = 0
        ones[ones != 0] = 1

        zeros = np.multiply(
            neighbor_count, np.ones_like(self.grid) - self.grid)
        zeros[zeros != 3] = 0
        zeros[zeros == 3] = 1
        self.grid = np.add(ones, zeros)

    def reset(self):
        """
        Resets the grid of the GameOfLife object with random integers 0 or 1.
        """
        self.grid = np.random.randint(0, 2, self.grid.shape)

    def print_board(self, truncate=True, symbols=['□ ', '■ ']):
        """
        Prints the GameOfLife grid to the console.

        Args:
            truncate (bool, optional): Whether to truncate the grid to the bounding box of live cells. Defaults to True.
            symbols (List[str], optional): The symbols to use for representing live and dead cells. Defaults to ['□ ', '■ '].

        Returns:
            None
        """
        if truncate:
            x, y = np.where(self.grid == 1)
            temp_grid = self.grid[min(x):max(x)+1, min(y):max(y)+1]
        else:
            temp_grid = self.grid

        for row in temp_grid:
            for col in row:
                if col == 0:
                    print(symbols[0], end='')
                else:
                    print(symbols[1], end='')
            print()


if __name__ == '__main__':
    game = GameOfLife()
    round_counter = 0
    while True:
        print(f'Round {round_counter}:')
        game.print_board(False)
        game.update()
        round_counter += 1
        input()
