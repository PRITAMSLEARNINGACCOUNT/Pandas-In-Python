import pandas as pd
import numpy as np

hello = pd.Series(np.random.rand(50))
print(hello)
print(type(hello))

DataFrame = pd.DataFrame(np.random.rand(500, 5), index=np.arange(500))
print(DataFrame)
DataFrame.to_excel("DataFrame.xlsx")
