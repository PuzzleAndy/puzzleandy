## Getting Started
```
pip install puzzleandy
```

## Example: Black and White
```
import puzzleandy as pa

im = pa.read('example.png')
im = pa.rgb_to_gray(im)
pa.show(im)
```

## Example: Black to Red Gradient Map
```
import puzzleandy as pa

im = pa.read('example.png')
im = pa.black_to_red(im)
pa.show(im)
```