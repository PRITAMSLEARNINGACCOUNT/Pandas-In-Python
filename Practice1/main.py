import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(5, 5))
print(df)
for i in range(5):
  df.drop(i, axis=1, inplace=True)
  print(df)

df = pd.DataFrame(np.random.rand(5, 5))
print(df)
i = 4
while i >= 0:
  df.drop(i, axis=1, inplace=True)
  print(df)
  i = i - 1
