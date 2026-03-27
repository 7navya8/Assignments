# Assignment (24/02/2026)

# Assignment Name : Dataset Detective
# Description : Load a dataset, display top rows,
# find highest value column, count missing values, share 5 insights.

import pandas as pd
train_df = pd.read_csv(r"C:\Users\navya\OneDrive\Desktop\assignment\assignment7\train.csv")

print(train_df.head())

print(train_df.isnull().sum())
print(train_df.max(numeric_only=True))

print(f"Total passengers: {len(train_df)}")
print(f"Survivors: {train_df['Survived'].sum()}")
print(f"Non-survivors: {len(train_df) - train_df['Survived'].sum()}")
print(f"Average age: {train_df['Age'].mean():.2f}")
print(f"Number of women: {(train_df['Sex'] == 'female').sum()}")
print(f"Number of men: {(train_df['Sex'] == 'male').sum()}")