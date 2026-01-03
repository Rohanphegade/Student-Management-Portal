from django import forms
from .models import Document
from django.core.exceptions import ValidationError


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['document_type', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')

        #  File must exist
        if not file:
            raise ValidationError("No file uploaded.")

        #  Only PDF allowed
        if not file.name.lower().endswith('.pdf'):
            raise ValidationError("Only PDF files are allowed.")

        #  File size limit: 10 MB
        max_size = 10 * 1024 * 1024  # 10 MB
        if file.size > max_size:
            raise ValidationError("File size must not exceed 10 MB.")

        return file

    