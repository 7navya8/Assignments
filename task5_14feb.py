# create a file containing name,marks,subjects,department.requirement read.csv add new column ,add col avg,find top 2 students based on total department wise avg marks students scoring above 75 in all subjects handle missing value if any add total
import pandas as pd
import numpy as np

# Create sample data
data = {
    "Name": ["Asha", "Ravi", "Meera", "Kiran", "Divya", "Arun"],
    "Maths": [85, 70, 90, 76, np.nan, 88],
    "Science": [78, 65, 92, 80, 77, 95],
    "English": [82, 72, 85, 79, 80, 91],
    "Department": ["CS", "CS", "IT", "IT", "CS", "IT"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Handle missing values (fill with average of column)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Add new column: Total
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)

# Add new column: Average
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("Data with Total and Average:\n", df, "\n")

# Find top 2 students based on Total
top2 = df.nlargest(2, "Total")
print("Top 2 Students (Overall):\n", top2[["Name", "Total"]], "\n")

# Department-wise average marks
dept_avg = df.groupby("Department")[["Maths", "Science", "English"]].mean()
print("Department-wise Average Marks:\n", dept_avg, "\n")

# Students scoring above 75 in all subjects
above75 = df[(df["Maths"] > 75) & (df["Science"] > 75) & (df["English"] > 75)]
print("Students scoring above 75 in all subjects:\n", above75[["Name", "Maths", "Science", "English"]])