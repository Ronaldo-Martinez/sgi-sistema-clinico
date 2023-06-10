from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from modulo_control.views.login import registrar_empleado,editar_empleado,vista_adminitracion_empleados,lista_empleados, get_empleado,menu_estrategico,menu_tactico
from modulo_control.views.perfil import Perfil

from modulo_gerencial.views import Estrategico01,Estrategico02, Tactico01, Tactico02, Tactico03,bitacoraTacticos, bitacoraEstrategicos
from modulo_gerencial.views import bitacoraAdmin,bitacoraTacticos,bitacoraEstrategicos


from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('perfil', Perfil.as_view(), name='perfil'),
    path('registrar/empleado', registrar_empleado, name= 'registrarEmpleado'),
    path('editar/empleado/', editar_empleado, name= 'editarEmpleado'),
    # path('registrarLicLaboratorioClinico', registrarLicLaboratorioClinico, name= 'registrarLicLaboratorioClinico'),
    # path('agregarLicLaboratorioClinico', agregarLicLaboratorioClinico, name= 'agregarLicLaboratorioClinico'),
    # path('registrarSecretaria', registrarSecretaria, name= 'registrarSecretaria'),
    # path('agregarSecretaria', agregarSecretaria, name= 'agregarSecretaria'),
    path('empleados/', vista_adminitracion_empleados, name= 'vistaGestionEmpleados'),
    path('empleados/lista/', lista_empleados, name="listaEmpleados"),
    path('empleados/lista/<str:cod_empleado>', get_empleado, name='get_empleado'),
    path('reportes/MenúEstratégico', bitacoraEstrategicos, name= 'menuEstrategico'),
    path('reportes/MenúTáctico', bitacoraTacticos, name= 'menuTactico'),
    path('reportes/RE01/',login_required(Estrategico01.as_view()), name= 'vistaRE01'),
    path('reportes/RE02/',login_required(Estrategico02.as_view()), name= 'vistaRE02'),
    path('reportes/RT01/',login_required(Tactico01.as_view()), name= 'vistaRT01'),
    path('reportes/RT02/',login_required(Tactico02.as_view()), name= 'vistaRT02'),
    path('reportes/RT03/',login_required(Tactico03.as_view()), name= 'vistaRT03'),
   
    path('bitacora/Bitacora-Reportes-Estrategicos/',bitacoraEstrategicos, name= 'bitacoraRE'),
    path('bitacora/Bitacora-Reportes-Tacticos/',bitacoraTacticos, name= 'bitacoraRT'),
    path('bitacora/Bitacora-Reportes-Admin/',bitacoraAdmin, name= 'bitacoraRA'),

    
    
]
urlpatterns += staticfiles_urlpatterns()
