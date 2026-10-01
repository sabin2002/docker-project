import pandas as pd

data = {
    "Name": ["Sabin", "Milan", "Ram"],
    "Age": [23, 24, 22],
    "Major": ["IT", "IT", "Business"]
}

df = pd.DataFrame(data)

print("Student Information")
print(df)

print("\nAverage Age:", df["Age"].mean())