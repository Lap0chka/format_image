from rembg import remove
from PIL import Image
from django.conf import settings
import os


def remove_background(file):
    input_file = Image.open(file)
    output = remove(input_file)
    return output



