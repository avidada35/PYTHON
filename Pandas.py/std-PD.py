import pandas as pd

x = pd.read_csv("D:\\Python\\Python.py\\__pycache__\\bio.csv")
grade_map = {'O+': 'Pass', 'O': 'Pass', 'B': 'Fail', 'A': 'Fail','C':'Fail'}
# Add a new column 'Passed' indicating Pass/Fail based on the grade map
x['Passed'] = x['grade'].map(grade_map)
print(x)
print()
female = x[(x['Gender']=='female') & (x['age']>=13)]
print(female)