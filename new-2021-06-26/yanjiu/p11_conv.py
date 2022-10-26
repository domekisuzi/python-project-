import torch
import  torch.nn.functional as F
input = torch.tensor([[1,3,6,7,8],
                      [2,4,6,8,9],
                      [3,5,6,1,2],
                     [2,5,6,7,8],
                      [2,5,6,7,8]])

kernel  = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])

input = torch.reshape(input,(1,1,5,5))
kernel = torch.reshape(kernel,(1,1,3,3))
# print(input,kernel)
#  stride 一次卷一步
output  = F.conv2d(input,kernel,stride=1)
print( output )
output2  = F.conv2d(input,kernel,padding=1)
print(output2)