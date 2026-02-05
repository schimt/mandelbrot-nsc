"""
Mandelbrot Set Generator
Author : [Nikolai Schmidt Madsen]]
Course : Numerical Scientific Computing 2026
"""

import numpy as np

def mandelbrot(c):
    """
    Mandelbrot escape-time function.
    Parameters
    ----------
    c : complex
        Input complex number
    Returns
    -------
    int
        Iteration count
    """
    max_iter = 200
    z = 0j
    for n in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) > 4.0:
            return n
    return max_iter

    

def compute_mandelbrot_grid(width, height, max_iter=200):
    """
    Compute Mandelbrot iteration grid.
    Parameters
    ----------
    width : int
    height : int
    max_iter : int
    Returns
    -------
    np.ndarray
        2D array of iteration counts
    """
    re = np.linspace(-2.0, 1.0, width)
    im = np.linspace(-1.5, 1.5, height)

    grid = np.zeros((height, width), dtype=int)

    for i in range(height):
        for j in range(width):
            c = re[j] + 1j * im[i]
            grid[i, j] = mandelbrot(c)

    return grid

if __name__ == "__main__":
    grid = compute_mandelbrot_grid(100, 100)
    print(grid.shape)