import pandas as pd 
import numpy as np

df = pd.read_json("data.json")
df = df.T

print(df.columns)
