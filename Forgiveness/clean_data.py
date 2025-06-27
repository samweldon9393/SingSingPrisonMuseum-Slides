import pandas as pd 
import numpy as np
import os

df = pd.read_json("data.json", orient="records", lines=True)


dirr = "./txt/"
for i, row in df.iterrows():
    path = dirr + row["Filename"] 
    if os.path.exists(path):
        print("File exists!")
    else:
        print(f"File does not exist: {row}")

#df = df.dropna(subset=["Parole Applicant Code"])
#df.to_json("d.json", orient="records", lines=True)
