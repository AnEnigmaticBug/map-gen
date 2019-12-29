from pygame import image, transform

class TileLoader:
    def __init__(self, tile_size):
        self.images = [
            transform.scale(image.load('assets/water-deep.png'), (tile_size, tile_size)),
            transform.scale(image.load('assets/water-shallow.png'), (tile_size, tile_size)),
            transform.scale(image.load('assets/sand.png'), (tile_size, tile_size)),
            transform.scale(image.load('assets/grass.png'), (tile_size, tile_size)),
            transform.scale(image.load('assets/rock.png'), (tile_size, tile_size)),
            transform.scale(image.load('assets/lava.png'), (tile_size, tile_size)),
        ]
    
    def image(self, tile):
        return self.images[tile]
