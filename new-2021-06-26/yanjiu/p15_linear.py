import torchvision
from torch import nn
import  torch
from torch.nn import ReLU, Sigmoid, Linear
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# input = torch.tensor([[1,-0.5],
#                     [-1,3]
#                       ])
# input = torch.reshape(input,(-1,1,2,2))
#
# print(input.shape)

dataset = torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor(),download=False)

dataloader =DataLoader(dataset,batch_size=64)

class Tudui(nn.Module):

    def __init__(self) -> None:
        super(Tudui,self).__init__()
        self.linear1   = Linear(1966608,10)


    def forward(self,input):
        output = self.linear1(input)
        return output

tudui =  Tudui()
writer =SummaryWriter("./logs_linear")
step = 0
for data in dataloader:
    imgs,targets = data
    writer.add_images("input",imgs,global_step= step)
    output = torch.flatten(imgs)

    print(output.shape)
    output =  tudui(imgs)
    writer.add_images("output",output,global_step=step)
    step+=1

writer.close()