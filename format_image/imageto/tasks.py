import os

from celery import shared_task


@shared_task
def delete_image(path):
    os.remove(path)
