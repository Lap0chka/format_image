from django.shortcuts import render
from .forms import ImageForm
from .tasks import remove_background


def save_uploaded_file(original_image):
    file_name = original_image.name
    with open(f'media/{file_name}', 'wb') as destination:
        for chunk in original_image.chunks():
            destination.write(chunk)

    return file_name


def index(request):
    original_image = None

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            original_file = request.FILES['original_file']
            original_image = save_uploaded_file(original_file)
            output_name = form.cleaned_data['output_name']
            is_del_background = form.cleaned_data['is_del_background']
            if is_del_background:
                output = remove_background(original_file)
                output.save(f'{output_name}.png')

    else:
        form = ImageForm()
    return render(request, 'imageto/base.html', {'form': form, 'original_image': original_image})
