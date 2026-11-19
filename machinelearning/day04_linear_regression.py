import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    "house_size": [1000, 1500, 2000, 2500, 1200, 1800, 2200, 3000],
    "price": [50, 75, 100, 125, 60, 90, 110, 150]
}

df = pd.DataFrame(data)

X = df[["house_size"]]

y = df[["price"]]

X_train , X_test , y_train , y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = LinearRegression()

print(X_train)
print(y_train)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(mean_squared_error(predictions, y_test))


