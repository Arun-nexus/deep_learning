a=int(input("size"))

list=[]

for i in range(a):
    b=int(input("values"))
    list.append(b)                                              #  6 7 8 9 3 

print("printing the list",list)

small=list[0]

for i in range(a):
    if (list[i]<small):
        small=list[i]

print("printing the smallest element",small)

large=list[0]

for i in range(a):
    if (list[i]>large):
        large=list[i]


print("printing the largest element",large)

sum=0

for i in range(a):
    sum+=list[i]
    print(sum)


average=sum/a

print(average)