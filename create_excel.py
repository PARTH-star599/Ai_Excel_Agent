import pandas as pd

data = {
    "Name": ["Parth", "Rahul", "Amit", "Sneha", "Priya"],
    "Branch": ["CSE", "CSE", "CSE", "CSE", "CSE"],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

df.to_excel("students.xlsx", index=False)

print("students.xlsx created successfully!")