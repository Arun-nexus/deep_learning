import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\Arun\Downloads\students.csv",encoding="latin 1")
print(df)

marks=df["Total"]
marks=np.array(marks)
highest=np.max(marks)
average=np.mean(marks)
topper=df.loc[df["Total"]==highest]
print(topper)
name=input("emter the name of the student")
try:
    student=df.loc[df["Name"]==name]
    print(student)
except:
    print("wrong name")

subject = ["Math","Science","English","History","Computer"]
best=np.max(student[subject])
best_subject=(student[subject].idxmax())
print(f"{best},{best_subject}")
