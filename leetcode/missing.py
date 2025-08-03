# finding the missing number between the array

n=int(input("size of the array"))
array=[]


for i in range (n):
    n=int(input("emter elements"))
    array.append(n)

array=sorted(array)
print(array)
i=array[0]

for k in range(n):
    
    if i != array[k]:
        print(i)
        
    
    i=i+1

