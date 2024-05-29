from django.shortcuts import render

from .forms import ImageForm
from .function import remove_background


def index(request):
    output_image = None
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            original_file = request.FILES['original_file']
            output_name = form.cleaned_data['output_name']
            is_del_background = form.cleaned_data['is_del_background']
            format_choice = form.cleaned_data['format_choice']
            output_image = remove_background(original_file, output_name, format_choice, is_del_background)
    else:
        form = ImageForm()
    return render(request, 'imageto/base.html', {'form': form, 'output_image': output_image})
