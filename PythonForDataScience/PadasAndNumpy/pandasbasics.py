import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

mydataset = pd.read_csv('mydataset\Hurricanes.csv')

print(mydataset)

#plt.plot([1,2,3,4])
#plt.show()

y = np.arange(10)*10
x = np.arange(10)
plt.plot([x/10 for x in y],y)
plt.plot(x,[a**2 for a in x])
plt.plot(x,[a**3 for a in x])
plt.show()