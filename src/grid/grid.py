import numpy as np

class Grid:

    nx : int
    ny : int
    lx : float
    ly : float
    _grid : np.ndarray

    def __init__(self, nx, ny, lx, ly):
        self.nx = nx
        self.ny = ny
        self.lx = lx
        self.ly = ly
        self._grid = np.zeros([nx+2, ny+2, 4])

    @property
    def values(self):
        return self._grid[1:-1, 1:-1, :]

    @property
    def values_ghosts(self):
        return self._grid

def test_grid():
    grid_test = Grid(100, 100, 1, 1)
    print(grid_test.values)
