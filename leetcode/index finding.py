n=int(input("size of the array"))

array=[]

for i in range(n):
    value=int(input("enter the values of the array"))
    array.append(value)
array=sorted(array)
target=int(input("enter the target"))
k=[]
for i in array:

    if i <=target:
        k.append(i)

print(len(k))
