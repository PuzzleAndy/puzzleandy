import numpy as np
import puzzleandy as pa
import matplotlib.pyplot as plt

x = np.linspace(0,255,256)

im = pa.read('-50.png')
im = pa.rgb_to_gray(im)
y1 = im[0,0::3]

im = pa.read('-25.png')
im = pa.rgb_to_gray(im)
y2 = im[0,0::3]

im = pa.read('0.png')
im = pa.rgb_to_gray(im)
y3 = im[0,0::3]

im = pa.read('25.png')
im = pa.rgb_to_gray(im)
y4 = im[0,0::3]

im = pa.read('50.png')
im = pa.rgb_to_gray(im)
y5 = im[0,0::3]

im = pa.read('75.png')
im = pa.rgb_to_gray(im)
y6 = im[0,0::3]

im = pa.read('100.png')
im = pa.rgb_to_gray(im)
y7 = im[0,0::3]

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)
plt.plot(x,y7)
plt.axis('equal')
plt.savefig('graph.png')