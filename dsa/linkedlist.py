class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.start=None

    def insert(self):
        d=int(input("value"))                  
        newnode=node(d)
        newnode.next=self.start
        self.start=newnode

    def insertend(self):
        if self.start is None:
            print("list is empty inserting the element to starting")
            d=int(input("value"))                  
            newnode=node(d)
            newnode.next=self.start
            self.start=newnode
        else:
            p=self.start
            while p.next is not None:
                p=p.next
            n=int(input("value"))
            newnode=node(n)
            newnode.next=None
            p.next=newnode


    def delete(self):
        if self.start is None:
            print ("list is empty")
        else:
            print(self.start.data)
            self.start=self.start.next

    def display(self):
        if self.start is None:
            print ("list is empty")
        else:
            temp=self.start
            while temp is not None:
                print(temp.data)
                temp=temp.next

if __name__=="__main__":
    l1=linkedlist()

    while(1):

        n=int(input("choice"))


        if (n == 1):
            l1.insert()

        elif (n ==5):
            l1.insertend()

        elif (n == 2):
            l1.delete()
        elif (n == 3):
            l1.display()
        elif (n == 4):
            print("exiting")
            break
        else:
            print("wrong choice")