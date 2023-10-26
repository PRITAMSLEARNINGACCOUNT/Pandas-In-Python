import pandas as pd
import numpy as np

DataFrame = pd.DataFrame(np.random.rand(5, 5))
DataFrame.loc[0, 0] = None
print(DataFrame)
# DataFrame.to_excel("Hello_World_1.xlsx",index=False)
# print(DataFrame[0].isnull())
# DataFrame.isnull().to_excel("HelloWorld.xlsx",index=False)
# DataFrame.dropna(axis=1,inplace=True)
# print(DataFrame)
list = ["Hello Fucker", "Hello World"]
DataFrame.loc[0, 0] = list
print(DataFrame.shape)
