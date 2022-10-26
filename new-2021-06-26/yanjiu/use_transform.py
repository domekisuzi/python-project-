from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision.transforms import transforms

img_path = "dataset/train/ants/0013035.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("ToTensor", img_tensor)


# 归一化
# output[channel] = (input[channel] - mean[channel]) / std[channel]
trans_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = trans_norm(img_tensor)

# Resize
print(img.size)
trans_resize = transforms.Resize((512,512))
img_resize = trans_resize(img)

img_resize = trans_totensor(img_resize)
writer.add_image("Resize",img_resize, 0  )
print(img_resize)


# compose
trans_resize2 = transforms.Resize(512)
trans_compose = transforms.Compose([trans_resize2,trans_totensor])
img_resize2 = trans_compose(img)
writer.add_image("Resize",img_resize,1)

# RandomCrop
trans_random= transforms.RandomCrop(512)
trans_compose2 = transforms.Compose([trans_resize2,trans_totensor])
img_cop = trans_compose(img)
writer.add_image("Random",img_resize,2)
writer.close()
