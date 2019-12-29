from generator import Generator
from pygame import display, init, K_LEFT, K_UP, K_RIGHT, K_DOWN, QUIT
from random import randint
from viewer import Viewer

init()
display.set_caption('PCG Viewer')

Viewer(Generator(randint(0, 100), 32), 20, K_LEFT, K_UP, K_RIGHT, K_DOWN).loop()
