from django import forms
from .models import UploadedFile

class PredictForm(forms.ModelForm):
    file = forms.FileField(
        label='Selecione o arquivo CSV',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file',
                'accept': '.csv'
            }
        )
    )

    class Meta:
        fields = ['file']
        model = UploadedFile