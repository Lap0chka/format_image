from rembg import remove
from PIL import Image
from datetime import datetime, timedelta
from .tasks import delete_image


# def save_uploaded_file(original_image):
#     file_name = original_image.name
#     with open(f'media/{file_name}', 'wb') as destination:
#         for chunk in original_image.chunks():
#             destination.write(chunk)
#
#     return file_name


def remove_background(file_path, output_name, format_image, is_delete=False):
    input_file = Image.open(file_path)
    path = f'media/{output_name}.png' if is_delete else f'media/{output_name}.{format_image}'
    if is_delete:
        format_image = 'png'
        output = remove(input_file)
        output.save(path)
    else:
        input_file.save(path, exif=input_file.info.get('exif', b''))

    eta_time = datetime.now() + timedelta(minutes=10)
    delete_image.apply_async(args=[path], eta=eta_time)

    return f'{output_name}.{format_image}'


