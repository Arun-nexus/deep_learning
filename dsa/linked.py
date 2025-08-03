class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):
        self.start=None
    
    def insert(self):
        n=int(input("data for ht node"))
        newnode=node(n)
    
        newnode.next=self.start
        self.start=newnode
    
    def insertend(self):
        n=int(input("data for node"))
        newnode=node(n)

        if self.start is None: 
            print("list is empty data was stored in first element")
            newnode.next=self.start
            self.start=newnode
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            newnode.next=None
            temp.next=newnode

    def display(self):
        if self.start is None:
            print("list is empty")
        else:
             temp=self.start
             while temp.next is not None:
                 print(temp.data)
                 temp=temp.next
             print(temp.data)
    def __str__(self):
        if self.start is None:
            return "Empty Linked List"
        result = []
        current = self.start
        while current:
            result.append(str(current.data))
            current = current.next
        
if __name__ =="__main__":
    linked_list=[]


   
    
    while(1):
        h=int(input("enter the choice"))
        
        if h == 11:
            
            namei=linkedlist()
            while(1):
                 ch = int(input("enter the choice for linkeedlists"))
                 if ch == 1:
                     namei.insert()
                 elif ch == 2:
                     namei.insertend()
                 elif ch == 3:
                     namei.display()
                 elif ch == 4:
                     print(">>exiting")
                     break
                 else :
                    print("wrong choice")
            linked_list.append(namei)
            
        elif h == 22:
            print("All linked lists stored:")
            print(f"Linked List ")
            for i in linked_list:
                print(i)
        elif h == 33:
             print(">>exiting")
             break
        else :
            print("wrong choice")



            
        

    


             




        
    
            



        

        
        