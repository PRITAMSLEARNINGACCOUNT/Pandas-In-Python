import pandas as pd

Dict_1 = {
    "Person Name": ["Pritam"],
    "City Name": ["Kolkata"],
    "Charecter Type": ["Good"]
}
DataFrame = pd.DataFrame(Dict_1)
print(DataFrame)
DataFrame.to_excel("Test.xlsx")
