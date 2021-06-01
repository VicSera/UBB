from os import listdir

import torch
import PIL.Image
from torch.utils.data import Dataset
from torchvision import transforms

device = torch.device('cuda:0' if torch.cuda.is_available() else
                      'cpu')


class ImageClassifierDataset(Dataset):
    def __init__(self, image_list, image_classes):
        self.images = []
        self.labels = []
        self.classes = list(set(image_classes))
        self.class_to_label = {c: i for i, c in enumerate(self.classes)}
        self.image_size = 32
        self.transforms = transforms.Compose([
            transforms.Resize(self.image_size),
            transforms.CenterCrop(self.image_size),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
        for image, image_class in zip(image_list, image_classes):
            transformed_image = self.transforms(image)
            self.images.append(transformed_image)
            label = self.class_to_label[image_class]
            self.labels.append(label)


    def __getitem__(self, index):
        return self.images[index], self.labels[index]


    def __len__(self):
        return len(self.images)


def get_dataset(basedir):
    imgs, classes = [], []
    for directory in (basedir + '/male', basedir + '/female'):
        for filename in listdir(directory):
            img = PIL.Image.open(directory + "/" + filename).convert('RGB')
            img.thumbnail((200, 200))
            imgs.append(img)
            classes.append("human")
    for filename in listdir(basedir + '/nonhuman'):
        img = PIL.Image.open(basedir + '/nonhuman/' + filename).convert('RGB')
        img.thumbnail((200, 200))
        imgs.append(img)
        classes.append("nonhuman")

    return ImageClassifierDataset(imgs, classes)