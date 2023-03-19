#!/usr/bin/env python
# coding: utf-8

# In[90]:




import argparse
import torch
import matplotlib.pyplot as plt
from utils.data import NoisyBSDSDataset
from utils.argument import Args
from models.team08_RUNOOB import DnCNN, UDnCNN, DUDnCNN
import nntools as nt
from utils.utils import DenoisingStatsManager, plot


# In[91]:


args = Args()
args.plot = True


# In[92]:


vars(args)


# In[93]:


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
# dataset
train_set = NoisyBSDSDataset(
    args.root_dir, image_size=args.image_size, sigma=args.sigma)
test_set = NoisyBSDSDataset(
    args.root_dir, mode='test', image_size=args.test_image_size, sigma=args.sigma)

# model

net = DUDnCNN(args.D, C=args.C).to(device)

# optimizer
adam = torch.optim.Adam(net.parameters(), lr=args.lr)

# stats manager
stats_manager = DenoisingStatsManager()

# experiment
exp = nt.Experiment(net, train_set, test_set, adam, stats_manager, batch_size=args.batch_size,
                    output_dir=args.output_dir, perform_validation_during_training=True)


# ## Testing on other image

# In[94]:


from PIL import Image
import torchvision as tv
import numpy as np
import matplotlib.pyplot as plt


# In[95]:


def image_preprocess(img_path):
    img = Image.open(img_path).convert('RGB')  
    transform = tv.transforms.Compose([
        #tv.transforms.Resize(300),
        # convert it to a tensor
        tv.transforms.ToTensor(),
        # normalize it to the range [−1, 1]
        tv.transforms.Normalize((.5, .5, .5), (.5, .5, .5))
        ])
    img = transform(img)
    return img


# In[96]:


import os
plt.close()
plt.axis('off')

model = exp.net.to(device)
file_root = '../test/LSDIR_DIV2K_Test_Sigma50/'  # 当前文件夹下的所有图片
file_list = os.listdir(file_root)
save_out = "../test/outputpic/" # 保存图片的文件夹名称
for img_name in file_list:
    img_path = file_root + img_name
    imgp = image_preprocess(img_path=img_path)
    imgp = imgp.unsqueeze(0).to(device)
    model.eval()
    with torch.no_grad():
        y = model.forward(imgp)
    plt.imshow(y[0].permute(1,2,0))
    out_name = img_name.split('.')[0]
    save_path = save_out + out_name + '.png'
    plt.savefig(save_path, bbox_inches='tight',pad_inches = 0)

