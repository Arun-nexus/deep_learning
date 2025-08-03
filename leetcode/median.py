n=int(input("size"))

a=[]
b=[]
c=[]
for i in range(n):
    k=int(input("values of the array"))
    a.append(n)

m=int(input("size of the second array"))

for i in range(m):
    z=int(input("values of the array"))
    b.append(n)

j=n+m
c1=sorted(a+b)

if j%2!=0:
    c=c1[j//2]
elif j%2 == 0:
    c=c1[((j//2)+((j//2)-1))//2]




print("the median of the array is",c1[c])



