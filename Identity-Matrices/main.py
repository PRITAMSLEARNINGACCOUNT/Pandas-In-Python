import pandas as pd
import numpy as np

DataFrame = pd.DataFrame(np.identity(45))
DataFrame.to_excel("Identity Matrices.xlsx", index=False)
