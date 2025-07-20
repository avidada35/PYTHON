#Handle missing values in the DataFrame, 
#Replace missing ages with the median age and missing grades with the mode of grades.

import pandas as pd

data = pd.read_csv('D:\\Python\\Python.py\\__pycache__\\bio.csv')

meadian = data['age'].median()
mod = data['grade'].mode()[0]

data['age'].fillna(meadian,inplace=True)
data['grade'].fillna(mod,inplace=True)

print(data)