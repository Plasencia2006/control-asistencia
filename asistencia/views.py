from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Clase, Asistencia
from .forms import ClaseForm, AsistenciaForm

# Vistas para Clase
class ClaseListView(ListView):
    model = Clase
    template_name = 'asistencia/clase_list.html'
    context_object_name = 'clases'
    paginate_by = 10

class ClaseDetailView(DetailView):
    model = Clase
    template_name = 'asistencia/clase_detail.html'
    context_object_name = 'clase'

class ClaseCreateView(CreateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'asistencia/clase_form.html'
    success_url = reverse_lazy('clase_list')

class ClaseUpdateView(UpdateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'asistencia/clase_form.html'
    success_url = reverse_lazy('clase_list')

class ClaseDeleteView(DeleteView):
    model = Clase
    template_name = 'asistencia/clase_confirm_delete.html'
    success_url = reverse_lazy('clase_list')

# Vistas para Asistencia
class AsistenciaListView(ListView):
    model = Asistencia
    template_name = 'asistencia/asistencia_list.html'
    context_object_name = 'asistencias'
    paginate_by = 10

class AsistenciaDetailView(DetailView):
    model = Asistencia
    template_name = 'asistencia/asistencia_detail.html'
    context_object_name = 'asistencia'

class AsistenciaCreateView(CreateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'asistencia/asistencia_form.html'
    success_url = reverse_lazy('asistencia_list')

class AsistenciaUpdateView(UpdateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'asistencia/asistencia_form.html'
    success_url = reverse_lazy('asistencia_list')

class AsistenciaDeleteView(DeleteView):
    model = Asistencia
    template_name = 'asistencia/asistencia_confirm_delete.html'
    success_url = reverse_lazy('asistencia_list')

# Vista principal
def home(request):
    clases_count = Clase.objects.count()
    asistencias_count = Asistencia.objects.count()
    clases_recientes = Clase.objects.order_by('-fecha')[:5]
    return render(request, 'asistencia/home.html', {
        'clases_count': clases_count,
        'asistencias_count': asistencias_count,
        'clases_recientes': clases_recientes
    })