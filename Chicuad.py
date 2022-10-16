import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

#Grados de libertad
deg_fredom = 3
#Nivel de significancia
alpha = 0.01
#Punto critico
critic = chi2.ppf(1-alpha, deg_fredom)
x = np.arange(0, 20, 0.001)
plt.plot(x, chi2.pdf(x, df = deg_fredom, scale=1.3))
section = np.arange(critic,20,0.001)

plt.fill_between(section, chi2.pdf(section, df = deg_fredom, scale=1.3), color="red")
plt.yticks([])
plt.xlim(0,20)
plt.show()