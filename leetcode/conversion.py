#conversion into binary
date=input("enter the date in dd mm yyyy format")
list=[]
list.append(date)

day,month,year=map(int,date.split("-"))
print(type(day))
year=bin(year)[2:]
month=bin(month)[2:]
date=bin(day)[2:]

print(date,month,year)