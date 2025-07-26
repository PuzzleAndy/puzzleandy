import puzzleandy as pa

im = pa.read('chelsea.png')
im = pa.rgb_to_gray(im)
pa.show(im)