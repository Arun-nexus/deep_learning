# l1=[]
# l2=[]
# l3=[]
# size=int(input("size of the array"))
# for i in range(size):
#     n=int(input("values for the list"))
#     l1.append(n)

# for i in range(size):
#     n=int(input("values for the list"))
#     l2.append(n)

# for i in range(size-1,-1,-1):
  
#     m=l1[i]
#     n=l2[i]
#     c=m+n
#     l3.append(c)

# print(l3)

import numpy as np

data=list(map(int,(input("enter the list in list ").split( ))))

data2=list(map(int,(input("enter the list in list ").split( ))))
array1=np.array(data)
array2=np.array(data2)
add=array1+array2
print(add)