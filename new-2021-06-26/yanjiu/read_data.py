from torch.utils.data import Dataset
from PIL import Image
import os

help(Dataset)

dir_path = "new-2021-06-26/yanjiu/dataset/train"


class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(root_dir, label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)


ants_label_dir = "ants"

bees_label_dir = "bees"
ants_dataset = MyData(dir_path, ants_label_dir)
bees_dataset = MyData(dir_path, bees_label_dir)
train_dataset = ants_dataset+ bees_dataset