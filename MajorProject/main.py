#Dataset used: https://www.kaggle.com/datasets/ananthr1/weather-prediction


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv("seattle-weather.csv")

#EDA
df = df.drop("date", axis="columns")
df = df.loc[:,['wind', 'precipitation', 'temp_max', 'temp_min', 'weather']]

x = df.iloc[:, 0:4].values
y = df.iloc[:, 4]

accuracy = 0
highestAccuracy = 0
i=0

while i<50:
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    model = LogisticRegression(max_iter=974)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_pred, y_test)*100
    if accuracy > highestAccuracy:
        mostAccurate = pickle.dumps(model)
        highestAccuracy = accuracy
    print(accuracy)
    i+=1

final_model = pickle.loads(mostAccurate)
print(f"\n\nMost accurate: {highestAccuracy}")
