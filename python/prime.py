while(1):
    c=0
    n=int(input("values"))
    for i in range(2,n):
        if(n%i==0):
             c+=1
        elif(n%i!=0):
            c+=0


    if(c==0):
            print("number is prime")
    else:
        print("the number is not prime")