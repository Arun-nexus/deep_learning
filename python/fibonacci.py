#0 1 1 2 3 5 8

size=int(input("last element"))
a,b=0,1
d=[0,1]
for i in range(size):
    c=a+b
    # changing the  values
    a,b=b,c
    if b > size :
        break 
    d.append(b)
print(f"fibonaci series for element {size} is ",d)