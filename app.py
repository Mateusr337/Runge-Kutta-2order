import numpy as np
import matplotlib.pyplot as plt

# Runge Kutta 2 - decaimento duplo

m0 = 100
t0 = 0
t_final = 10
delta_t = 0.01


def f_line(fx):
    lamb = 1
    return - lamb * fx


def Runge_kutta(t_final, delta_t, f0, t0, f_line):

    results = [f0]
    time = [t0]
    f = f0

    for t in np.arange(delta_t, t_final, delta_t):
        newf_2 = f + f_line(f) * delta_t / 2
        newf = f + f_line(newf_2) * delta_t

        f = newf

        results.append(newf)
        time.append(t)

    plt.plot(time, results)
    plt.show()
    return


Runge_kutta(t_final, delta_t, m0, t0, f_line)
