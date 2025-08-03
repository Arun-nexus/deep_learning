n=input("enter the string")

possible =set()
possible.add(n)

for i in range(1,len(n)):
    
    if n[i]==n[i-1]:
        new=n[:i]+n[i+1:]
        possible.add(new)
       
print(len(possible))
print(possible)