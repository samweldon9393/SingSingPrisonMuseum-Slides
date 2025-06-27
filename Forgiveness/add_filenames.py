import pandas as pd
import numpy as np
import json

def make_filename(code: str, date: str):
    return f"{code}-{date}.txt"


df = pd.read_json("data1.json")
df = df.T

#print(df['Parole Applicant Code'])
#print(df['Interview/Decision Date'])

df["Filename"] = df.apply(lambda row: make_filename(row["Parole Applicant Code"], row["Interview/Decision Date"]), axis=1)

df.to_json("data.json", orient="records", lines=True)
