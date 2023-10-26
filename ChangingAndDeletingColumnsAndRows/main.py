import pandas as pd
import numpy as np

list = ['A', 'B', 'C', 'D', 'E']
DataFrame = pd.DataFrame(np.random.rand(50, 5), np.arange(50))
print(DataFrame)
DataFrame.columns = list
print(DataFrame)
newdf = DataFrame.drop('D', axis=1)

newdf['A'][0] = 100.0
print(DataFrame)
