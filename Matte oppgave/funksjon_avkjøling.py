import matplotlib.pyplot as plt
import numpy as np

T_K = float(input("temperatur til omgivelser: "))
T_0 = float(input("starttemperatur til objektet: "))
a = -0.021


def avkjøling(t):
    return T_K + (T_0 - T_K) * np.exp(a*t)


x_verdier = np.linspace(0,90,10000)
y_verdier = avkjøling(x_verdier) 


plt.title('Newtons avkjølingslov')
plt.plot(x_verdier, y_verdier)
plt.xlabel("Tid i minutter")
plt.ylabel("Temperatur i celsius")
plt.grid()
plt.show()

