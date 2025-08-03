# to find the longest substring without repetation

n=input("enter the string")
l=[]
print(len(n))
k=[  ]

for i in range(len(n)):                 #  4  5  6  3
                                        #  
    j=i+1
    z=n[i:j]
    l.append(z)

print(k)
for r in l:
    if r in k:
        break
    k.append(r)
    
print(k)



    
    

    

