from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'dashboard/home.html')

def about(request):
    return render(request, 'dashboard/about.html')


@login_required
def subjects(request):
    return render(request, 'dashboard/subjects.html')