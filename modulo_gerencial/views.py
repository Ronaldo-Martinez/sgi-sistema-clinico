from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Reporte, FiltroReporte
from datetime import datetime

# Create your views here.

def estrategico01(request):
    return render(request, 'RE01.html')

def estrategico02(request):
    return render(request, 'RE02.html')

def bitacoraEstrategicos(request):
    return render(request, 'BRE.html')

def tactico02(request):
    return render(request, 'RT02.html')

def tactico03(request):
    return render(request, 'RT03.html')

def bitacoraTacticos(request):
    return render(request, 'BRT.html')

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

class Tactico02(TemplateView):
    template_name = "RT02.html"
    login_url='/login/'  
    response={'type':'','title':'', 'info':''}

    def post(self, request, *args, **kwargs):
        fecha_inicio = datetime.strptime(request.POST.get('fecha_inicio'), "%Y-%m-%d").date()
        fecha_fin=datetime.strptime(request.POST.get('fecha_fin'), "%Y-%m-%d").date()
        idExamen=request.POST.get('id_examen')
        reporte=Reporte.objects.create(
            empleado=request.user,
            tipo_reporte=4,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        FiltroReporte.objects.create(
            reporte=reporte,
            valor=idExamen
        )
        self.response['type']='success'
        self.response['title']='Se han almacenado los parametros del reporte.'
        return JsonResponse(self.response)

class Tactico03(TemplateView):
    template_name = "RT03.html"
    login_url='/login/'  
    response={'type':'','title':'', 'info':''}

    def post(self, request, *args, **kwargs):
        fecha_inicio = datetime.strptime(request.POST.get('fecha_inicio'), "%Y-%m-%d").date()
        fecha_fin=datetime.strptime(request.POST.get('fecha_fin'), "%Y-%m-%d").date()
        Reporte.objects.create(
            empleado=request.user,
            tipo_reporte=5,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        self.response['type']='success'
        self.response['title']='Se han almacenado los parametros del reporte.'
        return JsonResponse(self.response)
