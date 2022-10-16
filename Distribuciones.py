import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

#Grados de libertad 
degg_fredom = 15
rv = t(df=degg_fredom, loc=0, scale=1.2)
#Nivel de significancia 
alpha = 0.05
#Punto critico
critic = t.ppf(1-alpha/2, degg_fredom)
x = np.linspace(rv.ppf(0.0001), rv.ppf(0.9999), 1000)
y = rv.pdf(x) 
section = np.arange(-4.9,-critic,0.001)
plt.fill_between(section, rv.pdf(section), color="red")
section = np.arange(critic,4.9,0.001)
plt.fill_between(section, rv.pdf(section), color="red")
plt.yticks([])
plt.xlim(-5,5)
plt.plot(x,y)
plt.show()