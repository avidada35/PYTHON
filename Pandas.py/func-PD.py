#- Identify the most common grade achieved by students.
import pandas as pd

x = pd.read_csv("D:\\Python\\Python.py\\__pycache__\\bio.csv")

common = x['grade'].mode()[0]
print(common)
print()

#- Find out the distribution of gender among the students.

dis = x['Gender'].value_counts()
print(dis)