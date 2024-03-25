from django.shortcuts import render
from .forms import ModelForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        mf = ModelForm(request.POST)
        if dc.is_valid():
            dc.save()
        mf = ModelForm()

    else:
        mf = ModelForm()