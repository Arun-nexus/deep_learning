# # #You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

# # Return true if num is balanced, otherwise return false.

 

# # Example 1:

# # Input: num = "1234"

# # # Output: false

# # # Explanation:

# # # The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
# # # Since 4 is not equal to 6, num is not balanced.

# # n=input("enter the string")
# # k=[]
# # for i in range(0,len(n),+2):
# #     t=i+1
# #     k.append(int(n[i:t]))

# # print(k)
# # r=[]
# # for i in range(1,len(n),+2):
# #     z=i+1
# #     r.append(int(n[i:z]))

# # j=0
# # m=0

# # for i in k:
# #     j=j+i

# # for i in r:
# #     m=m+i
# # print(j,m)
# # if j==m:
# #     print("they are balanced")
# # else:
# #     print("they are not balanced")

# # Input the string of digits


# n=input("enter the string")

# odd=0
# even=0

# for i,  digit in enumerate(n):

#     if i%2==0:
#         odd+=int(digit)
#     elif i%2!=0:
#         even+=int(digit)

# if odd== even:
#     print("string is balanced")
# else:
#     print("strimg is imbalanced")
import tensorflow as tf
print("TF Version:", tf.__version__)
print("GPU Available:", tf.config.list_physical_devices('GPU'))
