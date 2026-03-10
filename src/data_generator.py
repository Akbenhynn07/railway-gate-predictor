import pandas as pd
import numpy as np

np.random.seed(42)

samples = 500

data = {
    "train_speed": np.random.uniform(40,120,samples),
    "distance_to_crossing": np.random.uniform(0.5,10,samples),
    "delay_minutes": np.random.uniform(0,15,samples)
}

df = pd.DataFrame(data)

df["gate_closure_time"] = (
    df["distance_to_crossing"] / df["train_speed"] * 60
) + df["delay_minutes"]

df.to_csv("data/train_data.csv",index=False)

print("Dataset generated")
