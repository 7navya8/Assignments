# create a dataset with columns age,missing values, salary,city like Hyderabad then experience some duplicates.perform remove duplicates handle missing values standardize city names apply min max scaling on age and salary show final cleaned data
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Step 1: Create dataset with duplicates and missing values
data = {
    "Name": ["Asha", "Ravi", "Meera", "Ravi", "Divya", "Arun"],
    "Age": [25, 30, np.nan, 30, 28, 35],
    "Salary": [50000, 60000, 55000, 60000, np.nan, 70000],
    "City": ["Hyderabad", "hyderabad", "Bangalore", "Hyderabad", "HYDERABAD", "Chennai"],
    "Experience": [2, 5, 3, 5, 4, 7]
}

df = pd.DataFrame(data)

print("Original Data:\n", df, "\n")

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Handle missing values (fill with column mean)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Step 4: Standardize city names (make lowercase and strip spaces)
df["City"] = df["City"].str.lower().str.strip()

# Step 5: Apply Min-Max scaling on Age and Salary
scaler = MinMaxScaler()
df[["Age", "Salary"]] = scaler.fit_transform(df[["Age", "Salary"]])

# Step 6: Show final cleaned data
print("Final Cleaned Data:\n", df)