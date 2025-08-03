#removing the repeating elemet in array
while(1):
    l=int(input("size of the array"))
    array=[]
    for i in range(l):
        z=int(input("values of the array"))
        array.append(z)
    k=[]
    for i in array:
        if i not in k:
            k.append(i)

    print(k)
