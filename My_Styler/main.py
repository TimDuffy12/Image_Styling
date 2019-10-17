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




num_epochs = 31


def main():
    pastiche = image_loader(
        "C:\\Users\\timjd\OneDrive - SNHU\Documents\Sophomore_Software_Engineering\Images\\Selfie-2.jpg").type(dtype)
    pastiche.data = torch.randn(pastiche.data.size()).type(dtype)

    style_cnn = StyleCNN(style, content, pastiche)

    for i in range(num_epochs):
        pastiche = style_cnn.train()

        if i % 10 == 0:
            print("Iteration: %d" % (i))

            path = "C:\\Users\\timjd\OneDrive - SNHU\Documents\Sophomore_Software_Engineering\Images\outputs\%d.png" % (i)
            pastiche.data.clamp_(0, 1)
            save_image(pastiche, path)


main()