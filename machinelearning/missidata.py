import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

miss = pd.read_csv('missdata.csv',header= None)

print(miss)