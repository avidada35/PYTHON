import pandas as pd
#- Calculate the average age of students in the DataFrame.

x = pd.read_csv("D:\\Python\\Python.py\\__pycache__\\bio.csv")
avg_age = x['age'].mean()
print(x)
print()
print('average value of age is =',avg_age)