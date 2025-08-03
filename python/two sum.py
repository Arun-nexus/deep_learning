a=[]
n=int(input("size"))

for i in range(n):
    n=int(input("values for the array"))
    a.append(n)

g=int(input("give me the target"))
found=False               
for j in range(n):
        m=a[j]
        for i in range(j+1,n):
            k=a[i]
            if m+k == g:
                print("element was found",a[i],a[j])
            found=True

if found==False:
    print("array doesnt have that pair")

            
            
                 
                 
        
