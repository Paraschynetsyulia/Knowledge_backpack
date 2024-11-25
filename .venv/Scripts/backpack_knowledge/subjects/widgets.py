# widgets.py
from django.forms.widgets import FileInput

class MultipleFileInput(FileInput):
    input_type = 'file'

    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = kwargs.get('attrs', {})
        kwargs['attrs']['multiple'] = True  # Атрибут для завантаження кількох файлів
        super().__init__(*args, **kwargs)
