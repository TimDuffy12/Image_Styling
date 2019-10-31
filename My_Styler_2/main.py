import torch.utils.data
import torchvision.datasets as datasets

from StyleCNN import *
from utils import *

# CUDA Configurations
dtype = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

# Content and style
style = image_loader(
    "C:\\Users\\timjd\OneDrive - SNHU\Documents\Sophomore_Software_Engineering\Images\\Colorful.jpg").type(dtype)
content = image_loader(
    "C:\\Users\\timjd\OneDrive - SNHU\Documents\Sophomore_Software_Engineering\Images\\Selfie-2.jpg").type(dtype)



num_epochs = 3
N = 4


def main():
    style_cnn = StyleCNN(style)

    # Contents
    coco = datasets.ImageFolder(root='C:\\Users\\timjd\Documents\GitHub\cocoapi', transform=loader)
    content_loader = torch.utils.data.DataLoader(coco, batch_size=N, shuffle=True)

    for epoch in range(num_epochs):
        for i, content_batch in enumerate(content_loader):
          iteration = epoch * i + i
          content_loss, style_loss, pastiches = style_cnn.train(content_batch, style)

          if i % 10 == 0:
              print("Iteration: %d" % (iteration))
              print("Content loss: %f" % (content_loss.data[0]))
              print("Style loss: %f" % (style_loss.data[0]))

          if i % 500 == 0:
              path = "outputs/%d_" % (iteration)
              paths = [path + str(n) + ".png" for n in range(N)]
              save_images(pastiches, paths)

              path = "outputs/content_%d_" % (iteration)
              paths = [path + str(n) + ".png" for n in range(N)]
              save_images(content_batch, paths)
              style_cnn.save()

main()