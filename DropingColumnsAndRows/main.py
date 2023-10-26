import pandas as pd
import numpy as np

list = ['A', 'B', 'C', 'D']
df = pd.DataFrame(np.random.rand(5, 5), index=np.arange(5))
print(df)
newdf = df.drop(0)
newdf = newdf.drop(0, axis=1)
print(newdf)
newdf.columns = list
print(newdf)
newdf = newdf.drop('A', axis=1)
print(newdf)
newdf.drop('C', axis=1, inplace=True)
print(newdf)
