from django.db import models
from django.urls import reverse

class Clase(models.Model):
    curso = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    fecha = models.DateField(verbose_name="Fecha de Clase")
    docente = models.CharField(max_length=100, verbose_name="Nombre del Docente")
    # ✅ CAMBIO: URL en lugar de ImageField
    foto_url = models.URLField(verbose_name="Link de la Imagen", blank=True, null=True, 
                               help_text="Ej: https://ejemplo.com/imagen.jpg")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio", default="08:00")
    aula = models.CharField(max_length=50, verbose_name="Aula", default="A-101")
    
    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.curso} - {self.fecha}"
    
    def get_absolute_url(self):
        return reverse('clase_detail', kwargs={'pk': self.pk})

class Asistencia(models.Model):
    ESTADOS = [
        ('P', 'Presente'),
        ('A', 'Ausente'),
        ('T', 'Tardanza'),
        ('J', 'Justificado'),
    ]
    
    alumno = models.CharField(max_length=100, verbose_name="Nombre del Alumno")
    estado = models.CharField(max_length=1, choices=ESTADOS, verbose_name="Estado de Asistencia")
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='asistencias', verbose_name="Clase")
    # ✅ CAMBIO: URL en lugar de ImageField
    foto_url = models.URLField(verbose_name="Link de la Foto", blank=True, null=True,
                               help_text="Ej: https://ejemplo.com/foto-alumno.jpg")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    observaciones = models.TextField(verbose_name="Observaciones", blank=True, null=True)
    
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return f"{self.alumno} - {self.get_estado_display()}"
    
    def get_absolute_url(self):
        return reverse('asistencia_detail', kwargs={'pk': self.pk})