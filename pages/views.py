from django.shortcuts import render
from django.views import View
from .forms import PredictForm
from django.views.generic.edit import FormView
from .utils import CreateDataFromCSV

# Create your views here.
class HomePageView(View):
    def get(self, request):
        form = PredictForm()

        context = {
            'form': form
        }
        return render(request, 'home.html', context)
    def post(self, request):
        form = PredictForm(request.POST, request.FILES)
        if form.is_valid():
            test = form.save()

            result = CreateDataFromCSV().read_csv(test.file.url)
            context = {
                'form': form,
                'message': 'File uploaded successfully!'
            }
            return render(request, 'home.html', context)
        else:
            context = {
                'form': form,
                'message': 'Failed to upload file. Please try again.'
            }
            return render(request, 'home.html', context)
