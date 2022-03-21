from django.shortcuts import render

from project11.settings import TEMPLATES_DIR

# Create your views here.
def msr(request):
    return render(request,'h1.html')