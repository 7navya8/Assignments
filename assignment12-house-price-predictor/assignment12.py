# Assignment (09/03/2026)
# Assignment Name: House Price Predictor
# Description: Train a Linear Regression model, predict prices, and test with new input.
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Size": [1000, 1500, 2000, 2500, 3000],
    "Bedrooms": [2, 3, 3, 4, 4],
    "Price": [150000, 200000, 250000, 300000, 350000]
}
df = pd.DataFrame(data)

X = df[["Size", "Bedrooms"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

new_house = [[2200, 3]]
predicted_price = model.predict(new_house)
print("Predicted Price:", predicted_price[0])