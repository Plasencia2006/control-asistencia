from django.contrib import admin
from .models import Clase, Asistencia

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ['curso', 'fecha', 'docente', 'aula']
    list_filter = ['fecha', 'docente']
    search_fields = ['curso', 'docente']
    date_hierarchy = 'fecha'

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'estado', 'clase', 'fecha_registro']
    list_filter = ['estado', 'clase', 'fecha_registro']
    search_fields = ['alumno', 'clase__curso']