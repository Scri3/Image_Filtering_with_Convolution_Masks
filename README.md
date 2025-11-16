## Image Filtering with Convolution Masks

In this project, I have defined some 3x3 convolution filters such as edge
detection, blurring, sharpening, and original grayscale filter.\
First, name your desired picture as `'input.jpg'`, and put it in the same directorry as Mask.py file.\
By running the script, the image will be loaded and converted to grayscale. Then, a defined filter (`maskSharpen` in the current
    script) is applied to the image, and the ouput will be saved in the same directory named `'output.jpg'`.

## Defined Filters

### 1. `maskED1` -- **Edge Detection (Laplacian-like)**

    [-1, -1, -1]
    [-1,  8, -1]
    [-1, -1, -1]

This mask highlights areas of rapid intensity change by computing a
second‑order derivative. It detects edges in all directions and produces
high-contrast outlines.

### 2. `maskBlur` -- **Averaging Blur**

    [1, 1, 1]
    [1, 1, 1]
    [1, 1, 1] / 9

A simple uniform blurring filter. It averages surrounding pixels,
softening noise and reducing detail.

### 3. `maskSharpen` -- **Sharpening Filter**

    [ 0, -0.5, 0 ]
    [-0.5,  3, -0.5]
    [ 0, -0.5, 0 ]

This mask enhances edges and fine details by amplifying the center pixel
while subtracting neighboring values. It improves image clarity.

### 4. `maskED2` -- **Sobel Edge Detection (Horizontal)**

    [-1, 0, 1]
    [-2, 0, 2]
    [-1, 0, 1]

A horizontal Sobel operator. It emphasizes vertical edges by computing
the gradient in the x-direction.

### 5. `maskORG` -- **Original Grayscale**

    [0, 0, 0]
    [0, 1, 0]
    [0, 0, 0]

It returns the original image unchanged and serves
as a normal grayscaling filter.


## Notes

-   Only one mask is active at a time---modify the `filter2D`'s third parameter and apply your own desired filter from the filters above.
-   Ensure `input.jpg` is in the working directory.
-   The `output.jpg` will be saved in the same directory as `Mask.py` and `input.jpg` file.
