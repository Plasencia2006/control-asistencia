from django import forms
from .models import Clase, Asistencia

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['curso', 'fecha', 'docente', 'foto_curso', 'hora_inicio', 'aula']
        widgets = {
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del curso'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'docente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del docente'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'aula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de aula'}),
        }

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['alumno', 'estado', 'clase', 'foto_alumno', 'observaciones']
        widgets = {
            'alumno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del alumno'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'clase': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }