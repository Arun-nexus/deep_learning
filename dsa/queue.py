size=int(input("values"))
print("for inserting 1","\n","for delete 2","\n","for display 3","\n","for exiting 4")


f=-1
r=-1

q=[]

def insert():
    global f
    global r
    if (f==size):
        print("queue is full")
    

    else:
        if (f==r):
            f=-1
            r=-1
        
        n=int(input("value for insertion"))
        f=f+1
        q.append(n)
        if (r==-1):
            r=r+1

def delete():
    global r
    if(f==-1):
        print("queue is empty")
    
    else:
        print("deleted element is",q[r])
        r=r+1

def display():
      if(f==-1):
        print("queue is empty")
      else:
        for i in range(f+1):
            print(q[i])

while(1):
    
    ch=int(input(""))
    if (ch==1):
        insert()
    
    elif (ch==2):
        delete()

    elif (ch==3):
        display()   
    elif (ch==4):
        break
    else:
        print("wrong choice")
