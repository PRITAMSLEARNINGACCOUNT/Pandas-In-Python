import pandas as pd
import numpy as np

Dataframe = pd.DataFrame(np.random.rand(5, 5))
print(Dataframe)
for i in range(5):
  Dataframe.loc[i, i] = None
  Dataframe.dropna(axis=1, inplace=True)
  print(Dataframe)
