from django.shortcuts import render
from .forms import svform
from django.views import View
from django.http import HttpResponse
from .models import svModel

# Create your views here.
def get_index(request):
    auF = svModel.objects.all()
    return render(request, 'home/index.html',{'auF':auF})

class get_formsv(View):
    def get(self, request):
        svF = svform
        return render(request, 'home/formsv.html', {'svF':svF})
    def post(self, request):
        form = svform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Save File success!')
        else:
            return HttpResponse('Save File Failed!')