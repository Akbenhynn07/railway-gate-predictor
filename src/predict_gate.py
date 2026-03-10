import pickle
import numpy as np

model = pickle.load(open("gate_model.pkl","rb"))

sample = np.array([[80,5,3]])

prediction = model.predict(sample)

print("Predicted gate closure time:",prediction[0],"minutes")
