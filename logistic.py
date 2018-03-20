import numpy as np
import time
import math
v = np.random.rand(100)

tic = time.time()
u = np.zeros((100,1))
for i in range(100):
    for j in range(100):
        u[i] = math.exp(v[i])
toc = time.time()

print("Not vectorized:" + str(1000*(toc-tic)) + "ms")


tic = time.time()
u = np.exp(v)
toc = time.time()

print("Vectorized:" + str(1000*(toc-tic)) + "ms")

