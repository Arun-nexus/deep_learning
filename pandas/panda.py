import pandas as pd
#creating the data frame 
df=pd.DataFrame({
    "name":['aman','bhavya',None,'chetan'],
    "age":[24,23,None,51],
    "performance":[None,64,25,52]
})
miss=df.dropna()
print(miss)
# #creating the data file
# df.to_excel("output.xlsx",index=False)
# #printing the first two rows
# print("first two rows of the dataframe")
# show=df.head(2)
# print(show)
# #printing the column name
# print ("the column name of the dataframe")
# column=df.columns
# print(column)
# #printing multiple columns
# print("printing the multiple columns")
# col=df["age"],df["performance"]
# print(col)
# #printing the personn whose age is greater than 25
# print("printing the personn whose age is greater than 25")
# age_25=df[df["age"]>25]
# print(age_25)
# #adding the new column

# df["score"]=[78,88,90,79]
# print(df)
# #adding the new column
# df["city"]=' '
# print(df)
# df.describe()