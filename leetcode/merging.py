n=int(input("size of the array"))
array=[]
array2=[]

for i in range (n):
    n=int(input("emter elements"))
    array.append(n)

m=int(input("size of another array"))
for i in range (m):
    n=int(input("emter elements"))
    array2.append(n)

array=(array+array2)
array=sorted(array)

array3=[]
for i in range(len(array)):
    if array[i] != 0:
        array3.append(array[i])

print(array3)