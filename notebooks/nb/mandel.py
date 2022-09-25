import numpy as np
import matplotlib.pyplot as plt

def mandel(c, z=0, max_iter=100):
    for k in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return k
    return k
def mandelbrot(w, h, xl=-1.5, xu=0.5, yl=-1, yu=1):
    img = np.zeros((h, w)).astype('int')
    for i, real in enumerate(np.linspace(xl, xu, w)):
        for j, imag in enumerate(np.linspace(yl, yu, h)):
            c = complex(real, imag)
            img[j, i] = mandel(c)
    return img



img = mandelbrot(w=400, h=400)
plt.grid(False)
plt.imshow(img, cmap=plt.cm.jet)
plt.show()


