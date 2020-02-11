import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

df = pd.Series(np.arange(51))
df = pd.DataFrame({'a':pd.Series(np.arange(1,102)),'b':pd.Series(np.arange(51,102))})
#print(df)
print(df.values)
print(df.keys())
print(df.axes)