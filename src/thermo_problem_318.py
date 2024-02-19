import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

NUp = np.linspace(100, 0, 101)
Uen = np.linspace(-100, 100, 101)
Mag = np.linspace(1, -1, 101)
Omega = [math.factorial(int(100)) / (math.factorial(int(x)) * math.factorial(int(100 - x))) for x in NUp]
Sentro = [math.log(x) for x in Omega]

# print(Uen)

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

print(temperature)

# Find heat capacity.
