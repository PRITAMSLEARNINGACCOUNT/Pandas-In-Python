import pandas as pd
import numpy as np

list = ['A', 'B', 'C', 'D', 'E']
DataFrame = pd.DataFrame(np.random.rand(20, 5))
DataFrame.columns = list
print(DataFrame)
print(DataFrame.loc[(DataFrame['A'] < 0.90)])
print(DataFrame.iloc[0, 4])
print(DataFrame.iloc[[0, 4], [0, 2]])
