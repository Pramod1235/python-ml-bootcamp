import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "house_size": [1000, 1500, 2000, 2500, 1200, 1800, 2200, 3000],
    "bedrooms":   [2, 3, 3, 4, 2, 3, 4, 5],
    "price":      [50, 75, 100, 125, 60, 90, 110, 150]
}

df = pd.DataFrame(data)

print(df.head())

X = df[["house_size" , "bedrooms"]]
y = df["price"]
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.3 , random_state = 42)
