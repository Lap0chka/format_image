from django import forms


class ImageForm(forms.Form):
    original_file = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'inputFields',
            'id': 'fileInput'
        })
    )
    output_name = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'inputFields',
            'id': 'output',
            'placeholder': 'Output file name',
            'required': 'required'
        })
    )
    is_del_background = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'id': 'hidcheck',
            'hidden': 'hidden'
        })
    )
    options = [
        ('', 'Select a format'),
        ('jpg', 'JPG'),
        ('png', 'PNG'),
        # Добавьте другие варианты по мере необходимости
    ]
    format_choice = forms.ChoiceField(choices=options, widget=forms.Select(attrs={'class': 'inputFields'}))