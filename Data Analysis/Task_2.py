"""
TASK - 2: Data Manipulation with Pandas
"""

import pandas as pd

data = pd.read_csv('V:/Coding/Internship/Data Analysis internship/01.Data Cleaning and Preprocessing.csv')

# Data Summary
data.info()
print(data.head())


# Handling missing data
updated_data = data.fillna(data.mean(numeric_only=True))
print(updated_data.head(10))

#Summary statistics
print(data.describe)

print("Performing stats on Column BlowFlow")
print("Mean: ", round(data['BlowFlow'].mean(), 3))
print("Median: ", round(data['BlowFlow'].median(), 3))
print("MAX value: ", round(data['BlowFlow'].max(), 3))
print("MIN Value: ", round(data['BlowFlow'].min(), 3))

q1, q2, q3 = round(data['BlowFlow'].quantile(0.25), 2), round(data['BlowFlow'].quantile(0.50), 2), round(data['BlowFlow'].quantile(0.75), 2)
IQR = round((q3 - q1), 3)
print("Inter quartile range on Column BlowFlow: ", IQR)
