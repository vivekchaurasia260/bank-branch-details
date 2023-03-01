import pandas as pd

data = pd.read_csv("bank_branches.csv")
df = pd.DataFrame(data)
# Below lines is to check data coming from CSV.
# for i, ifs in enumerate(df.ifsc, start=0):
#     if ifs == "YESB0YUCB18":
#         print(df.loc[i])
