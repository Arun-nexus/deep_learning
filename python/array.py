a=int(input("size of the array :"))
j=[]
# k=[]
#taking first array
for i in range(a):
     n=int(input("values of the array:"))
     j.append(n)

smallest=map(lambda x:x**2,j)
print(list(smallest))
#taking secomd array
# for i in range(a):
#     m=int(input("values"))
#     k.append(m)

#multiplication of 2 array
# array=[j[i]*k[i] for i in range(a)]
# print(array) 

#taking two array 

# for i in range(a):
#     row=[]
#     for j in range(a):

#        n=int (input("value of the array"))
#        row.append(n)
    
#     k.append(row)

#     print(k) 
    
# size=int(input("size of the array"))
# array=[]
# array3=[]

# for i in range(size):
#    row=[]
#    for j in range(size):
#        n=int(input("value of the array"))
#        row.append(n)
#    array.append(row)

# for row in array:
#    print(row)


# for i in range(size):
#    row_2=[]
#    for j in range(size):
#        n=int(input("value of the array"))
#        row_2.append(n)
#    array3.append(row_2)

# for row_2 in array3:
#    print(row_2)

# array2=[]

# for i in range(size):
#    row3=[]
#    for j in range(size):
#       row3.append(array[i][j]+array3[i][j])
#    array2.append(row3)


# print("after addition of the values")
# for row in  array2:
#    print (row)

# size=int(input("size of the arrays:"))

# first=[]
# second=[]

# for i in range(size):
#    row=[]
#    for j in range(size):
#       n=int(input("values of the array"))
#       row.append(n)
#    first.append(row)


# for i in range(size):
#    row2=[]
#    for j in range(size):
#       n=int(input("values of the array"))
#       row2.append(n)
#    second.append(row2)

# result=[[0 for _ in range(size)] for _ in range (size)]

# for i in range(size):
#    for j in range(size):
#       for k in range(size):
#          result[i][j]+=first[i][k]*second[k][j]

# print("ans of the multiplication")
# for row in result:
#    print(row)