import pandas as pd
import numpy as np

DataFrame = pd.DataFrame(np.random.rand(50, 10))
print(DataFrame)
newdf = DataFrame
newdf[0][0] = int(2)
print(DataFrame)
newdf_2 = DataFrame.copy()
newdf_2[0][0] = "A"
print(newdf_2)
print(type(newdf_2[0][0]))
print(type(newdf_2[0][2]))
