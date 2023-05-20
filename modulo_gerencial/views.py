from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def estrategico01(request):
    return render(request, 'RE01.html')

def estrategico02(request):
    return render(request, 'RE02.html')

@login_required(login_url='/login/')
def tactico01(request):
    return render(request, 'RT01.html')

def tactico02(request):
    return render(request, 'RT02.html')

def tactico03(request):
    return render(request, 'RT03.html')



