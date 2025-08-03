import matplotlib.pyplot as py
import numpy as np
x=(list(map(int,input("enter the x axis").split(" "))))
y=(list(map(int,input("enter the y axis").split(" "))))


py.bar(x,y,color='green',label="line")
py.scatter(x,y,color="blue",label="circle")
py.title("practice")
py.xlabel("x-axis")
py.ylabel("y-axis")
py.legend()
py.show()
