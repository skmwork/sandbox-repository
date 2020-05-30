#/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

N = 10000
T = np.linspace(0, 1000, N+1, dtype=np.float32)

a=2
b=3
X = np.cos(a*T)
Y = np.sin(b*T)

fig = plt.figure()
ax = plt.subplot()
ax.plot(X, Y, 'g-')
plt.title('Legend inside')

fig.savefig(f'liss_{a}_{b}.png')
plt.close(fig) 