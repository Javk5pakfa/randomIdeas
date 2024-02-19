import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

NUp = np.linspace(100, 0, 101)
Uen = np.linspace(-100, 100, 101)
Mag = np.linspace(1, -1, 101)
Omega = [math.factorial(int(100)) / (math.factorial(int(x)) * math.factorial(int(100 - x))) for x in NUp]
Sentro = [math.log(x) for x in Omega]

# Find temperature.
temperature = []
i = 0
while i < len(Omega):
    if i == 0:
        temperature.append(0)
    elif 0 < i < len(Omega) - 1:
        Udiff = Uen[i + 1] - Uen[i - 1]
        Sdiff = Sentro[i + 1] - Sentro[i - 1]

        if Sdiff != 0:
            temperature.append(Udiff / Sdiff)
        else:
            temperature.append(np.nan)
    elif i == len(Omega) - 1:
        temperature.append(0)
    i += 1

# Find heat capacity. Cv = dU/dT
heat_capacity = []
i = 0
while i < len(Omega):
    if i == 0:
        heat_capacity.append(np.nan)
    elif 0 < i < len(Omega) - 1:
        Udiff = Uen[i + 1] - Uen[i - 1]
        if temperature[i + 1] != np.nan and temperature[i - 1] != np.nan:
            Tdiff = temperature[i + 1] - temperature[i - 1]
        else:
            Tdiff = np.nan

        if Tdiff != np.nan and math.isnan(temperature[i]) is False:
            heat_capacity.append(Udiff / Tdiff / 100)
        else:
            heat_capacity.append(np.nan)
    elif i == len(Omega) - 1:
        heat_capacity.append(np.nan)
    i += 1

result_d = dict()
result_d['NUp'] = NUp
result_d['Uen'] = Uen
result_d['Mag'] = Mag
result_d['Omega'] = Omega
result_d['Sentro'] = Sentro
result_d['temperature'] = temperature
result_d['heat_capacity'] = heat_capacity

result_table = pd.DataFrame(data=result_d)
# print(result_table.to_string())

# Write to file?
with open('table.txt', 'w') as fs:
    fs.write(result_table.to_string())

# Plotting various graphs.

# Entropy vs. Energy.
plt.subplot(2, 2, 1)
plt.scatter(Uen, Sentro, marker='.')
plt.title('Entropy vs. Energy')

# Temperature vs. Energy.
plt.subplot(2, 2, 2)
plt.scatter(Uen, temperature, marker='.')
plt.title('Temperature vs Energy')

# Heat capacity vs. temperature.
plt.subplot(2, 2, 3)
plt.scatter(temperature, heat_capacity, marker='.')
plt.title('Heat capacity vs. Temperature')

# Magnetization vs. temperature.
plt.subplot(2, 2, 4)
plt.scatter(temperature, Mag, marker='.')
plt.title('Magnetization vs. Temperature')

plt.tight_layout()
plt.savefig('thermo_problem_318.pdf')
# plt.show()
