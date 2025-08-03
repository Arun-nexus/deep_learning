# n=(int(input("enter the size of the board")))

# board=[]

# for i in range(n):
#     row=[]
#     for j in range(n):
#         if (i+j)%2==0:
#             row.append("black")
#         else:
#             row.append("white")
       
#     board.append(row)
# for row in board:

#     print(row)

# compare1=(input("enter the first element"))
# compare2=(input("enter the second element"))

# row1,col1=map(int,compare1.split(","))
# row2,col2=map(int,compare2.split(","))

# try:
#     take= board[row1][col1]
#     retake= board[row1][col2]

#     if take==retake:    
#         print("colors are same",take)
#     else:
#         print("colors are not same",take,retake)
# except:
#     print("wrong index enters")

import numpy as np

size=int(input("enter the size of the board"))

array=np.zeros((size,size), dtype=object)

array[1::2,::2]="black"            
array[1::2,1::2]="white"           
array[::2,1::2]="black"            
array[::2,::2]="white"     

print(array)
try:

    choice1=input("enter the row and column and seperate it with , ")
    choice2=input("enter the row and column and seperate it with , ")
    row1,col1=map(int,choice1.split(","))
    row2,col2=map(int,choice2.split(","))

    take=array[row1][col1]
    retake=array[row2][col2]

    if take==retake:
        print("both points are same",take)
    else:
        print("incompatible key points",take,retake)
except:
    print("wrong indexes choosen")