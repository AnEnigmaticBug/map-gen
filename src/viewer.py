from pygame import display, event, key, QUIT
from pygame.time import Clock
from tile_loader import TileLoader

class Viewer:
    def __init__(self, generator, tile_size, lt, up, rt, dn):
        self.generator = generator
        self.tile_loader = TileLoader(tile_size)
        self.clock = Clock()
        self.pos_x = 0
        self.pos_y = 0
        self.tile_size = tile_size
        self.lt = lt
        self.up = up
        self.rt = rt
        self.dn = dn
        res = tile_size * generator.grid_size
        self.screen = display.set_mode((res, res))
    
    def loop(self):
        self.repaint()

        running = True
        while running:
            for e in event.get():
                if e.type == QUIT: running = False
            
            keys = key.get_pressed()

            should_repaint = False

            if keys[self.lt]:
                self.pos_x -= 1
                should_repaint = True
            if keys[self.up]:
                self.pos_y -= 1
                should_repaint = True
            if keys[self.rt]:
                self.pos_x += 1
                should_repaint = True
            if keys[self.dn]:
                self.pos_y += 1
                should_repaint = True
            
            if should_repaint: self.repaint()

            self.clock.tick(30)
    
    def repaint(self):
        for y in range(0, self.generator.grid_size):
            for x in range(0, self.generator.grid_size):
                tile = self.generator.tile(self.pos_x + x, self.pos_y + y)

                img = self.tile_loader.image(tile)
                pos = (x * self.tile_size, y * self.tile_size)

                self.screen.blit(img, pos)
        
        display.update()

                
    