from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Reporte, FiltroReporte
from datetime import datetime

# Create your views here.

def estrategico01(request):
    return render(request, 'RE01.html')

class Estrategico01(TemplateView):
    template_name = "RE01.html"
    login_url='/login/'  
    response={'type':'','title':'', 'info':''}
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        fecha_inicio = datetime.strptime(request.POST.get('fecha_inicio'), "%Y-%m-%d").date()
        fecha_fin=datetime.strptime(request.POST.get('fecha_fin'), "%Y-%m-%d").date()
        idCategoria=request.POST.get('idCategoria')
        reporte=Reporte.objects.create(
            empleado=request.user,
            tipo_reporte=1,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        FiltroReporte.objects.create(
            reporte=reporte,
            valor=idCategoria
        )
        self.response['type']='success'
        self.response['title']='Se han almacenado los parametros del reporte.'
        return JsonResponse(self.response)

class Estrategico02(TemplateView):
    template_name = "RE02.html"
    login_url='/login/'  
    response={'type':'','title':'', 'info':''}
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        fecha_inicio = datetime.strptime(f"{request.POST.get('year')}-01-01", "%Y-%m-%d").date()
        fecha_fin=datetime.strptime(f"{request.POST.get('year')}-12-31", "%Y-%m-%d").date()
        idServicio=request.POST.get('idServicio')

        reporte=Reporte.objects.create(
            empleado=request.user,
            tipo_reporte=2,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        FiltroReporte.objects.create(
            reporte=reporte,
            valor=idServicio
        )

        self.response['type']='success'
        self.response['title']='Se han almacenado los parametros del reporte.'
        return JsonResponse(self.response)
    

def bitacoraEstrategicos(request):
    return render(request, 'BRE.html')

def bitacoraTacticos(request):
    return render(request, 'BRT.html')

def bitacoraAdmin(request):
    reportes = Reporte.objects.all()
    for reporte in reportes:
        reporte.filtros = reporte.filtroreporte_set.all()
    return render(request, 'BRA.html', {'reportes': reportes})

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
