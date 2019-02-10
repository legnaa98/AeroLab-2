import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('2412.csv', sep=',')
x = data['x']
y = data['y']

plt.plot(x,y,'k-',linewidth=0.85)
plt.axis('off')
plt.xlim([-0.01,1.01])
plt.ylim([5*np.min(y),5*np.max(y)])
plt.show()