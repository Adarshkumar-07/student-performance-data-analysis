import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("Dataset")
print(df)

print("\nAverage Marks")
print(df[['Math','DBMS','Python','OS']].mean())

print("\nVariance")
print(df[['Math','DBMS','Python','OS']].var())

print("\nStandard Deviation")
print(df[['Math','DBMS','Python','OS']].std())

print("\nGender Wise Performance")
print(df.groupby("Gender").mean())

df[['Math','DBMS','Python','OS']].mean().plot(kind='bar')
plt.title("Average Marks Per Subject")
plt.ylabel("Marks")
plt.show()