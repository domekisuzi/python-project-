import torchvision
from torch.utils.tensorboard import SummaryWriter

datset_transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
train_Set = torchvision.datasets.CIFAR10(root="./dataset",train=True,download=True,transform=datset_transform)
test_set = torchvision.datasets.CIFAR10(root="./dataset",train=False,download=True,transform=datset_transform)
# print(test_set[0])
# print(test_set.classes)
# img,target  = test_set[0]
# print(img)
# print(target)
# img.show()
# print(test_set[0])
writer = SummaryWriter("p10")
for i in range(10):
    img,target = test_set[i]
    writer.add_image("test_set",img,i)


writer.close()