import pandas as pd
import numpy as np

DataFrame = pd.DataFrame(np.random.rand(5, 5), index=np.arange(5))
DataFrame.to_excel("Normal DataFrame.xlsx", index=False)

New_Df = DataFrame.sort_index(axis=0, ascending=False)
New_Df.to_excel("Descending Order DataFrame.xlsx", index=False)

New_DataFrame = DataFrame.sort_index(axis=1, ascending=False)

New_DataFrame = New_DataFrame.sort_index(axis=0, ascending=False)
print(New_DataFrame)
New_DataFrame.to_excel("Final DataFrame.xlsx")
