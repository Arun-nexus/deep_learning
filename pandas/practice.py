# # import pandas as pd
# # df=pd.read_excel("output.xlsx")
# # # print(df)
# # # print(df.info())
# # miss=df.fillna(24)
# # print(miss)
# # # print(df)

# import pandas as pd

# df=pd.DataFrame({
#     "name":["arun","jatin","rishab","ankit","rohit"],
#     "age" :[24,48,52,64,23],
#     "marks":[43,89,24,52,65]

# })
# print(df)
# df.to_excel("data.xlsx",index=False)

# df2=pd.read_excel("output.xlsx")
# print(df2)

# print(df2.iloc[0])

import pandas as pd

size=int(input("enter the length of the list"))
array=[]
for i in range(size):
    data=list(map(int,input("enter the value for insertion").split(" ")))
    array.append(data)

column=input("enter the column name with spaces").split(" ")

df=pd.DataFrame(array,columns=column)
print(df)
# list=(df.iloc[0]).tolist()
# print(list,type(list))

# print(df.loc[0])
# df.insert(0,"age",df["roll"]*0.5)
# print(df)

column=[]
for i in range(len(df)):
    data=input("enter the data for insertion")
    column.append(data)

df.insert(1,"practice",column)
print(df)