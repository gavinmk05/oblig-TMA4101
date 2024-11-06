import pandas as pd
import matplotlib.pyplot as plt
import math

# Load dataset from the experiment
df = pd.read_csv('newton_avkjøling_matte.csv', comment='#', sep=';', decimal=',')

# Convert columns with data to lists
tid = df['Tid'].tolist()
temperatur = df['Temperatur'].tolist()

# Initial values for simulation
xstart = tid[0]
ystart = temperatur[0]
xslutt = tid[-1]
delta_x = 1
k = -0.0146  # Cooling constant
T = 20       # Ambient temperature

# Lists for calculated values
xverdier = []
yverdier = []
x = xstart
y = ystart




# Perform calculations based on Newton's law of cooling
while x <= xslutt:
    xverdier.append(x)
    yverdier.append(y)
    x = x + delta_x
    y = y + delta_x * k * (y - T)

# Plotting the data and model
plt.plot(tid, temperatur, 'o-', label='Eksperimentell data')  
plt.plot(xverdier, yverdier, '-', label='Model (Newtons avkjøling)')

# Adding labels and title
plt.xlabel("Tid i minutter")
plt.ylabel("Temperatur i grader Celsius")
plt.title("Newtons avkjølingslov")
plt.legend()
plt.show()
