import numpy as np

# # array=np.array([1,4,3,2])
# # print(type(array))
# ##### array creation by using eval function####
# # n=input("enter the list ")
# # elements=eval(n)

# # array=np.array(elements)

# # print(array)
# ##### taking a simple array by the user in numpy#####
# # n=input("enter the list by using space between them")

# # array=np.array(list(map(int,n.split( ))))
# # print (type(array))

# #####taking an 2d array by the user####

# row= int(input("enter the no of rows"))
# matrix=[]
# for i in range(row):
#     rows=list(map(int,input(f"enter the rows{i+1} elements was divided by the spaces").split( )))
#     matrix.append(rows)

# array=np.array(matrix)
# print(array)
# element=input("enter the elements with commas")
# row,col=map(int,element.split(","))
# print(array[row][col])
# ##### addition of 2 arrays

# n=list(map(int,input("enter the first array by differentiate by using spaces").split( )))
# m=list(map(int,input("enter the first array by differentiate by using spaces").split( )))

# array1=np.array(n)
# array2=np.array(m)
# print(array1)
# print(array2)
# add=array1+array2
# mult=array1*array2
# mul=reduce(lambda x,y:x*y,mult)
# print("additionis",add,"\n","multiplication is ",mul)

# n=int(input("enter the size of the array"))
# array=[]
# for i in range(n):
#     rows=[]
#     for j in range(n):
#         row=list(map(int,input("enter the first row of the array with commas").split(" ")))
#         rows.append(row)
#     array.append(rows)

# arrat=np.array(array)

# print(array)

array=(list(map(int,input("enter the array").split(","))))

# element=int(input("enter the element which you wznt to access"))
# print(array[element])
rarray=np.reshape(array,(2,4))


rarray=np.where(rarray==0,1,rarray)

print(rarray)