from opensimplex import OpenSimplex
from tile import Tile

class Generator:
    def __init__(self, seed, grid_size):
        self.simplex = OpenSimplex(seed)
        self.grid_size = grid_size
    
    def tile(self, x, y):
        height = self.height(x, y)

        if height < -0.1: return Tile.WATER_DEEP
        elif height < +0.10: return Tile.WATER_SHALLOW
        elif height < +0.17: return Tile.SAND
        elif height < +0.45: return Tile.GRASS
        elif height < +0.70: return Tile.ROCK
        else: return Tile.LAVA

    def height(self, x, y):
        grid_size = self.grid_size
        h1 = self.simplex.noise2d(67 + x / (grid_size * 10), 67 + y / (grid_size * 10))
        h2 = self.simplex.noise2d(x / grid_size, y / grid_size)
        h3 = self.simplex.noise2d(11 + 10 * (x / grid_size), 11 + 10 * (y / grid_size))

        return (1 * h1 + 3 * h2 + 1 * h3) / 5
