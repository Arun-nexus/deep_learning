#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

n=int(input("size of the array"))
array=[]


for i in range (n):
    n=int(input("emter elements"))
    array.append(n)

for i in range(len(array)-1,-1,-1):
    if array[i]== 9:
        array[i]=0
    else:
        array[i]+=1
        break
else:
    array.insert(0,1)
print(array)
    
        