from django import forms
from .models import UploadedFile

class PredictForm(forms.ModelForm):
    file = forms.FileField(
        label='Selecione o arquivo CSV',
        widget=forms.FileInput(
            attrs={
                'class': 'block w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-400 focus:outline-none',
                'accept': '.csv'
            }
        )
    )

    class Meta:
        fields = ['file']
        model = UploadedFile