from celery import shared_task
import os
from rembg import remove
from PIL import Image
from datetime import datetime, timedelta


@shared_task
def delete_image(path):
    os.remove(path)




