from django.db import models
from django.utils.timezone import now
from datetime import datetime

# Create your models here.
class Reporte(models.Model):
    OPCIONES_TIPO_REPORTE=(
        (1,'Reporte Estrategico 01'),
        (2,'Reporte Estrategico 02'),
        (3,'Reporte Tactico 01'),
        (4,'Reporte Tactico 02'),
        (5,'Reporte Tactico 03')
    )
    id_reporte=models.AutoField(primary_key=True)
    empleado=models.ForeignKey('modulo_control.Empleado', on_delete=models.CASCADE)
    tipo_reporte=models.IntegerField(choices=OPCIONES_TIPO_REPORTE, blank=False,null=False)
    fecha_hora_reporte=models.DateTimeField(auto_now_add=True, blank=True)
    fecha_inicio=models.DateField(default=now, blank=True)
    fecha_fin=models.DateField(default=now, blank=True)
    def __str__(self):
        return f'{self.empleado.nombres} - {self.get_tipo_reporte_display()}'

class FiltroReporte(models.Model):
    id_filtro_reporte=models.AutoField(primary_key=True)
    reporte=models.ForeignKey('Reporte', on_delete=models.CASCADE)
    valor=models.TextField(null=True, blank=True)