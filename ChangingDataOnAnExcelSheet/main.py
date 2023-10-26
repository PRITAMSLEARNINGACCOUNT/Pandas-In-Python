import pandas as pd

Var = pd.read_excel("Test.xlsx")
Var["Name"][0] = "Hello Fucker"
Var.to_excel("Var.xlsx")
