from django.shortcuts import render
from .models import PreviousWork

# Create your views here.


def work(request):
    gallery = PreviousWork.objects.all()
    context = {}
    return render(request, 'work.html', {'gallery': gallery})
