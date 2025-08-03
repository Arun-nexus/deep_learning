# num=int(input("num:"))
# i=1
# while (i !=11):
#     print(num,"*", i ,"=",num*i)
#     i+=1

# #table of multiplication
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")
