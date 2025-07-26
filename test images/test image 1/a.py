import numpy as np
import puzzleandy as pa

width = 256*3
height = 150
gray_vals = np.linspace(0,255,width,dtype=np.uint8)
im = np.tile(gray_vals,(height,1))
pa.write(im,'test.png')