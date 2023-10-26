import pandas as pd
import numpy as np

Dictionary = {
    "A": [0, 2, 3],
    "B": [0, 215, 5],
    "B": [0, 215, 5],
}
DataFrame = pd.DataFrame(Dictionary)
print(DataFrame.describe())
print(DataFrame.mean())
print(DataFrame.corr())
print(DataFrame.count())
print(DataFrame.max())
print(DataFrame.min())
print(DataFrame.median())
print(DataFrame.std())
DataFrame.describe().to_csv("Describe.csv", index=False)
