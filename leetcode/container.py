
# Container With Most Water
size=int(input("enter the size of the array"))
array=[]
for i in range(size):
    inzert=int(input("enter the elemant of the array"))
    array.append(inzert)

volume=0
print(array)
print(len(array))

for i in range(len(array)):
    for j in range(len(array)):
        if volume<(min(array[i],array[j]))*(j-i):
            volume=(min(array[i],array[j]))*(j-i)

print(volume)