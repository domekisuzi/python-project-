import torchvision
from torch import nn
import  torch
from torch.nn import ReLU, Sigmoid, Linear, Conv2d, MaxPool2d, Flatten, Sequential
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


dataset = torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor(),download=False)

dataloader =DataLoader(dataset,batch_size=64)




class Tudui(nn.Module):

    def __init__(self) -> None:
        super(Tudui,self).__init__()
        # self.conv1 = Conv2d(3,32,5,padding=2)
        # self.maxppol1= MaxPool2d(2)
        # self.conv2 = Conv2d(32,32,5,padding=2)
        # self.maxppol2 = MaxPool2d(2)
        # self.conv3 = Conv2d(32,64,5,padding=2)
        # self.maxppol3 = MaxPool2d(2)
        # self.flattern = Flatten()
        # self.linear1 = Linear(1024,64)
        # self.linear2 = Linear(64,10)
        self.model1 =  Sequential(
            Conv2d(3,32,5,padding=2),
            MaxPool2d(2)  ,
            Conv2d(32, 32, 5, padding=2) ,
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10))

    def forward(self,x):
        # x = self.conv1(x)
        # x = self.maxppol1(x)
        # x = self.conv2(x)
        # x = self.maxppol2(x)
        # x = self.conv3(x)
        # x = self.maxppol3(x)
        # x =  self.flattern(x)
        # x = self.linear1(x)
        # x = self.linear2(x)
        x = self.model1(x)
        return x

tudui =  Tudui()
# writer =SummaryWriter("./logs_linear")
print(tudui)
# output = tudui(dataloader)
# step = 0
input = torch.ones((64,3,32,32))
output = tudui(input)
print(output.shape)
# for data in dataloader:
#     imgs,targets = data
#     writer.add_images("input",imgs,global_step= step)
#     output = torch.flatten(imgs)
#
#     print(output.shape)
#     output =  tudui(imgs)
#     writer.add_images("output",output,global_step=step)
#     step+=1
#
# writer.close()