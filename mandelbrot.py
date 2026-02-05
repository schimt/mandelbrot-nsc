"""
Mandelbrot Set Generator
Author : [Nikolai Schmidt Madsen]]
Course : Numerical Scientific Computing 2026
"""
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


if __name__ == "__main__":
    assert mandelbrot(0+0j) == 200