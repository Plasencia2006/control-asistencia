from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs para Clase
    path('clases/', views.ClaseListView.as_view(), name='clase_list'),
    path('clases/<int:pk>/', views.ClaseDetailView.as_view(), name='clase_detail'),
    path('clases/crear/', views.ClaseCreateView.as_view(), name='clase_create'),
    path('clases/<int:pk>/editar/', views.ClaseUpdateView.as_view(), name='clase_update'),
    path('clases/<int:pk>/eliminar/', views.ClaseDeleteView.as_view(), name='clase_delete'),
    
    # URLs para Asistencia
    path('asistencias/', views.AsistenciaListView.as_view(), name='asistencia_list'),
    path('asistencias/<int:pk>/', views.AsistenciaDetailView.as_view(), name='asistencia_detail'),
    path('asistencias/crear/', views.AsistenciaCreateView.as_view(), name='asistencia_create'),
    path('asistencias/<int:pk>/editar/', views.AsistenciaUpdateView.as_view(), name='asistencia_update'),
    path('asistencias/<int:pk>/eliminar/', views.AsistenciaDeleteView.as_view(), name='asistencia_delete'),
]