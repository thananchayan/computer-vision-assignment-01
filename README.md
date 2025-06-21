# 🎯 Computer Vision and Image Processing - Take Home Assignment 1

This repository contains solutions for the **EE7204 – Computer Vision and Image Processing** Take Home Assignment 1. The project demonstrates basic image processing operations using **Python** and **OpenCV**.

---

## 📂 Folder Structure

```
computer-vision-assignment-01/
├── main.py                     # Main script to run all tasks
├── utils/                      # Contains modular implementations
│   ├── quantization.py         # Task 1: Intensity reduction
│   ├── smoothing.py            # Task 2: Average filtering
│   ├── rotation.py             # Task 3: Image rotation
│   └── resolution.py           # Task 4: Block averaging
├── inputs/
│   └── input.jpg               # Original input image
├── outputs/                    # Generated result images
├── README.md                   # This file
```

---

## ✅ Tasks Implemented

### 1. Intensity Level Reduction

Reduces the number of intensity levels in the image to any input power of 2 (e.g., 2, 4, 8...).

### 2. Average Filtering (Smoothing)

Applies a 3×3, 10×10, and 20×20 average (mean) filter to smooth the image.

### 3. Image Rotation

Rotates the image by 45° and 90° using affine transformation.

### 4. Block Averaging (Spatial Resolution Reduction)

Reduces spatial resolution by averaging non-overlapping 3×3, 5×5, and 7×7 blocks.

---

## 🖼️ Output Samples

Output images are saved in the `outputs/` folder and include:

- `quantized.jpg`
- `blurred_3x3.jpg`, `blurred_10x10.jpg`, `blurred_20x20.jpg`
- `rotated_45.jpg`, `rotated_90.jpg`
- `lowres_3x3.jpg`, `lowres_5x5.jpg`, `lowres_7x7.jpg`

---

## 🚀 How to Run

### Prerequisites

- Python 3.x
- VS Code or any Python IDE

### Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate       # For Windows
```

### Install Required Libraries

```bash
pip install opencv-python numpy matplotlib
```

### Run the Project

```bash
python main.py
```

---
