n=int(input("size of the array"))
array=[]


for i in range (n):
    n=int(input("emter elements"))
    array.append(n)

r=int(input("value which you want to remove"))

new_array=[]
for i in array:

    if i != r:
        new_array.append(i)

print(new_array)