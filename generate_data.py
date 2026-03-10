import pandas as pd
import numpy as np

np.random.seed(42)

age = np.random.randint(20,60,100)
salary = np.random.randint(20000,100000,100)

purchase = []

for i in range(100):
    if salary[i] > 50000 and age[i] > 30:
        purchase.append(1)
    else:
        purchase.append(0)

df = pd.DataFrame({
    "Age":age,
    "Salary":salary,
    "Purchase":purchase
})

df.to_csv("data/data.csv",index=False)

print("Dataset created")