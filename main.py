import cv2
from utils.quantization import reduce_intensity_levels
from utils.smoothing import average_filter
from utils.rotation import rotate_image
from utils.resolution import block_average
import matplotlib.pyplot as plt

image = cv2.imread("inputs/input.jpg")

# Task 1 - Intensity Level Reduction
quantized = reduce_intensity_levels(image, 4)
cv2.imwrite("outputs/quantized.jpg", quantized)

# Task 2 - Smoothing
for k in [3, 10, 20]:
    blurred = average_filter(image, k)
    cv2.imwrite(f"outputs/blurred_{k}x{k}.jpg", blurred)

# Task 3 - Rotation
for angle in [45, 90]:
    rotated = rotate_image(image, angle)
    cv2.imwrite(f"outputs/rotated_{angle}.jpg", rotated)

# Task 4 - Resolution Reduction
for b in [3, 5, 7]:
    low_res = block_average(image, b)
    cv2.imwrite(f"outputs/lowres_{b}x{b}.jpg", low_res)
