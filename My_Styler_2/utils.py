import torchvision.transforms as transforms
from torch.autograd import Variable

from PIL import Image
import scipy.misc

imsize = 256

loader = transforms.Compose([
    transforms.Resize((imsize, imsize)),
    transforms.ToTensor()
])

unloader = transforms.ToPILImage()


def image_loader(image_name):
    image = Image.open(image_name)
    image = loader(image)
    image = image.unsqueeze(0)
    return image


def save_image(input, path):
    image = input.data.clone().cpu()
    image = image.view(3, imsize, imsize)
    image = unloader(image)
    scipy.misc.imsave(path, image)