import numpy as np

def f(x):
    return x ** 2

a = 0
b = 2

N = 100000

x_random = np.random.uniform(a, b, N)
y_random = f(x_random)

integral_mc = (b - a) * np.mean(y_random)

print(f"Інтеграл (метод Монте-Карло): {integral_mc}")
