import pandas
import torch
from caffe2.python.dataset import Dataset
from imblearn.over_sampling import SMOTE
from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("logs")
image_path = "dataset/train/bees/16838648_415acd9e3f.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array) )
print(img_array.shape)
# 高度 宽度 通道
writer.add_image("test", img_array, 2 ,dataformats="HWC")
# 标量
for i in range(100):
    writer.add_scalar("y=2x", 2 * i, i)

writer.close()


class Data(Dataset):
    def __init__(self):
        contains = pandas.read_csv("./creditcard.csv")
        self.np_data = np.array(contains).astype(dtype=np.float32)[::,1:-1:]
        # self.np_data = (self.np_data-np.min(self.np_data))/(np.max(self.np_data)-np.min(self.np_data))
        self.np_res = np.array(contains).astype(dtype=np.float32)[::,-1::]
        self.x_train, self.x_valid, self.y_train, self.y_valid = train_test_split(self.np_data, self.np_res, test_size=0.1, random_state=0)
        sm = SMOTE()
        # print(len(self.x_train))
        self.x_train, self.y_train = sm.fit_resample(self.x_train, self.y_train)

        # print(len(self.x_train))
        # print(self.y_train.sum())

class MyDataSet(Data):
    def __init__(self):
        super().__init__()

    def __len__(self):
        return len(self.x_train)

    def __getitem__(self, item):
        return (torch.tensor(self.x_train[item]),torch.tensor(np.array([self.y_train[item]])))