import numpy as np
import matplotlib.pyplot as plt
import cmath
plt.style.use('dark_background')

plt.rcParams['figure.figsize'] = [8, 8]

x_1 = np.array([2, 3, -1, 4])
N_1 = np.size(x_1)
X_1 = np.zeros(N_1, dtype = 'complex_')
for n in range (0,N_1):
  for m in range (0,N_1):
    X_1[n] = X_1[n] + x_1[m]*cmath.exp(-1j*np.pi/2*n*m)

plt.subplots_adjust(hspace=1.5)
fig, axs = plt.subplots(3, 1, constrained_layout=False)
axs[0].stem(x_1)
#axs[0].set_title('subplot 1')
axs[0].set_xlabel('time')
axs[0].set_ylabel('signal')
fig.suptitle('Task 1 Output', fontsize=16)

axs[1].stem(X_1.real)
axs[1].set_xlabel('frequency')
#axs[1].set_title('real')
axs[1].set_ylabel('Real')

axs[2].stem(X_1.imag)
axs[2].set_xlabel('frequency')
#axs[1].set_title('real')
axs[2].set_ylabel('Imaginary')


plt.show()