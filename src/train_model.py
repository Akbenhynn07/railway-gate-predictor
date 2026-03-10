import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("data/train_data.csv")

X = df[["train_speed","distance_to_crossing","delay_minutes"]]
y = df["gate_closure_time"]

model = LinearRegression()
model.fit(X,y)

with open("gate_model.pkl","wb") as f:
    pickle.dump(model,f)

print("Model trained")
