import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 256)
pixels.fill((0,0,0))
