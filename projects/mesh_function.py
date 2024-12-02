import numpy as np
import matplotlib.pyplot as plt

def mesh_function(f, t):
    #t = [1, 2, 3, 4]
    #f = [func(t_1), func(t_2), func(t_3), func(t_4)]
    f_val = []
    for t_val in t:
        f_val.append(f(t_val))
    return f_val

def func(t):
    if ((0 <= t) & (t <= 3)):
        return np.exp(-t)
    elif ((3 < t) & (t <= 4)):
        return np.exp(-3*t)
    else:
        raise ValueError("t is outside of domain")

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()

    # t = n*dt
    dt = 0.1 
    n = 40
    t = np.linspace(0, n*dt, n)
    fun = mesh_function(func, t)
    plt.plot(fun, t)
    plt.show()