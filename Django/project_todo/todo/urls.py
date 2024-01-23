from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = 'add'),
    path('view', views.view, name = 'view'),
    path('delete', views.delete, name = 'delete'),
    path('edit', views.edit, name = 'edit'),
    path('edit/status', views.edit_status, name = 'edit_status'),   
    path('edit/title', views.edit_title, name = 'edit_title'),
    path('edit/body', views.edit_body, name = 'edit_body')
]