top=-1
a=[]

size=int(input("sizeof the top"))

def insert():
    global top
    if(top==size):
        
        print("stack is full")
    else:
         n=int(input("elements of the stack"))
         
         a.append(n)
         top=top+1
         print(n,"inserted in stack")


def delete():
    global top
    if(top==-1):
        print("stack is empty")
    else:
        print(a[top])
        top=top-1
    
def display():
    if(top==-1):
        print("stack is empty")
    else:
        for i in range(top+1):
            print(a[i])


while(1):
    ch=input("choice")

    if (ch=="insert"):
        insert()
    
    elif (ch=="delete"):
        delete()

    elif (ch=="display"):
        display()   
    elif (ch=="exit"):
        break
    else:
        print("wrong choice")