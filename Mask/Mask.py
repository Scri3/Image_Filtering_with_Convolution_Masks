import cv2
import numpy as np

# Load the image
img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

cv2.destroyAllWindows()# Define a 3x3 matrix mask
maskED1 = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

maskBlur = np.array([
    [1, 1, 1],
    [1,  1, 1],
    [1, 1, 1]
], dtype=float) /9

maskSharpen = np.array([
    [0, -0.5, 0],
    [-0.5,  3, -0.5],
    [0, -0.5, 0]
], dtype=float) 

maskED2 = np.array([
    [-1, 0, 1],
    [-2,  0, 2],
    [-1, 0, 1]
], dtype=float) 

maskORG = np.array([
    [0, 0, 0],
    [0,  1, 0],
    [0, 0, 0]
], dtype=float) 


# Apply the mask to the image
output_img = cv2.filter2D(img, -1, maskSharpen)

# Save the new image
cv2.imwrite('output.jpg', output_img)
