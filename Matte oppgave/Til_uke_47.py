import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Laster inn datasettet fra forsøket
df=pd.read_csv('newton_avkjøling_matte.csv', comment='#', sep=';', decimal='.')

# Konverterer eventuelle strenger i kolonnene til tall
df['Tid'] = pd.to_numeric(df['Tid'], errors='coerce')
df['Temperatur'] = pd.to_numeric(df['Temperatur'].str.replace(',', '.'), errors='coerce')


# Konverterer kolonnene med data til lister.
tid=df['Tid'].tolist()
temperatur=df['Temperatur'].tolist()

xstart=tid[0]
ystart=temperatur[0]
xslutt=tid[-1]

T_OMGIVELSER = 22.2
T_START = temperatur[0]


def finn_propo(i):
    return -np.log(abs(temperatur[i] - T_OMGIVELSER)/(ystart - T_OMGIVELSER))/tid[i]


a = finn_propo(45)


def avkjøling(t):
    return T_OMGIVELSER + (T_START - T_OMGIVELSER) * np.exp(-a*t)

x_verdier = np.linspace(0,90)
y_verdier = avkjøling(x_verdier) 

forskjell = []
for i in range(len(tid)):
    d =  avkjøling(x_verdier[i]) - temperatur[i]
    forskjell.append(abs(d))



print(f"Proposjonalitetskonstanten er {-a:.6f}")


# Tegner grafen med spenning som funksjon av tid
plt.figure(1)
plt.title("Newtons avkjølingslov")
plt.plot(tid, temperatur,'-', color='red', label='Praktisk modell')
plt.plot(x_verdier, y_verdier, color='blue', label='Teoretisk modell')
plt.xlabel("Tid i minutter")
plt.ylabel("Temperatur i celsius")
plt.legend()
plt.grid()
plt.xlim(0, 90)
plt.ylim(10, 55)


plt.figure(2)
plt.title("Forskjell mellom teoretisk og praktisk modell")
plt.plot(tid, forskjell, color='brown')
plt.xlabel("Tid i minutter")
plt.ylabel("Temperaturforskjell i celsius")
plt.xlim(0, 90)
plt.ylim(0, 5)
plt.grid()
plt.show()


