from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = 'add'),
    path('view', views.view, name = 'view'),
    path('delete', views.delete, name = 'delete'),
    path('edit', views.edit, name = 'edit'),
    path('edit_details', views.edit_details, name='edit_details'),
]