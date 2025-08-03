class node:

    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class tree:

        def __init__(self,root=None):
            self.root=root

        def insert(self):

            n=int(input("value"))
            newnode=node(n)
            if self.root is None:
                self.root=newnode
            
            else:
                current=self.root
                while True:

                    if n < current.value:
                        if current.left is None  :
                           current.left = newnode
                           break

                        current=current.left 
                    elif n > current.value:
                        if current.right is None:
                            current.right=newnode
                            break
                        current=current.right

        def display(self):

            if self.root is None:
                print("tree is empty")

            else:
                print("tree ",end=" ")
                self.inorder(self.root)

        def inorder(self,node):
                    
                    if node is not None:

                        self.inorder(node.left)
                        print(node.value,end=" ")
                        self.inorder(node.right)
       
       
        def delete(self):

            n=int(input("value for deletion"))
            self.root = self._delete(self.root,n)
        
        def _delete(self,node,n):

            if node is None:
                print("tree is empty")
                return node

            #travesing between the node

            if n>node.value:
                node.right=self._delete(node.right,n)
            elif n<node.value:
                node.left=self._delete(node.left,n)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
            
            temp = self._minvaluenode(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
        
            return node
        def _minvaluenode(self,node):
            current=node
            while current.left is not None:
                current=current.left
            return current


if __name__=="__main__":
    t=tree()
    
    while (1):
        ch=int(input("choice"))
        if ch == 1:
            t.insert()
        elif ch== 2:
            t.display()
        elif ch== 3:
            t.delete()
        elif ch == 4:
            print("..exiting")
            break

        else:
            print("wrong choice")

        
        
        

                    
        

            
        