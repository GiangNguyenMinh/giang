import numpy as np
import pandas as pd

df = pd.read_csv("UNSW_NB15_training-set.csv",header=0)
# print(df)
print(df["id"])# in ra cot 3
df = df["id"]
df.to_csv("datatraningrow3.csv")