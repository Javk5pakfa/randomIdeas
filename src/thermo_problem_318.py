import numpy as np
import math
import pandas as pd
import matplotlib as mpl
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
            temperature.append('NAN')
    elif i == len(Omega) - 1:
        temperature.append(0)
    i += 1

# Find heat capacity. Cv = dU/dT
heat_capacity = []
i = 0
while i < len(Omega):
    if i == 0:
        heat_capacity.append('NAN')
    elif 0 < i < len(Omega) - 1:
        Udiff = Uen[i + 1] - Uen[i - 1]
        if temperature[i + 1] != 'NAN' and temperature[i - 1] != 'NAN':
            Tdiff = temperature[i + 1] - temperature[i - 1]
        else:
            Tdiff = 'NAN'

        if Tdiff != 'NAN' and temperature[i] != 'NAN':
            heat_capacity.append(Udiff / Tdiff / 100)
        else:
            heat_capacity.append('NAN')
    elif i == len(Omega) - 1:
        heat_capacity.append('NAN')
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

print(result_table)

# Plotting various graphs.
