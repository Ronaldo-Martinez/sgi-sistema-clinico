from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Reporte
from datetime import datetime

# Create your views here.

def estrategico01(request):
    return render(request, 'RE01.html')

def estrategico02(request):
    return render(request, 'RE02.html')

def tactico02(request):
    return render(request, 'RT02.html')

def tactico03(request):
    return render(request, 'RT03.html')

class Tactico01(TemplateView):
    template_name = "RT01.html"
    login_url='/login/'  
    response={'type':'','title':'', 'info':''}

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    
    def post(self, request, *args, **kwargs):
        fecha_str=request.POST.get('fecha_inicio')
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        Reporte.objects.create(
            empleado=request.user,
            tipo_reporte=3,
            fecha_inicio=fecha
        )
        self.response['type']='success'
        self.response['title']='Se han almacenado los parametros del reporte.'
        print(fecha_str)
        return JsonResponse(self.response)

