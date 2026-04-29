# 2D Graphics Transformation Engine

A lightweight, interactive Python tool built from scratch to visualize 2D affine transformations using pure linear algebra. 

Instead of relying on pre-built graphics libraries to do the heavy lifting, this engine calculates translations, rotations, scaling, and shearing by constructing standard 3x3 homogeneous matrices and applying them to coordinate geometry via dot products.

## ✨ Features
* **Custom Matrix Factories:** Modular functions that generate math-perfect transformation matrices.
* **Transformation Pipeline:** Stack multiple transformations (e.g., Rotate -> Translate -> Scale) before rendering the final result.
* **Smart Rendering:** Uses Matplotlib with automatic bounds detection and forced equal aspect ratios to prevent shape warping.
* **Automatic Shape Closing:** Intelligently connects polygon vertices for clean visual output.

## 🛠️ Built With
* **Python 3.10+** (Utilizes modern `match...case` architecture)
* **NumPy:** For matrix generation and vector multiplication.
* **Matplotlib:** For rendering the Cartesian coordinate grid and geometric shapes.

## 🚀 How to Run
Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/buster_call_Root/PyTransform2D.git](https://github.com/buster_call_Root/PyTransform2D.git)
cd PyTransform2D
pip install numpy matplotlib
```
