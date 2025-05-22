import numpy as np

def heavy_compute():
    a = np.random.rand(3000, 3000)
    b = np.dot(a, a)
    print("Sum:", np.sum(b))

if __name__ == "__main__":
    heavy_compute()

